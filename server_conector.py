import os

from elasticsearch import Elasticsearch

from flask import Flask

app = Flask(__name__)


class ServerConector ():

    def __init__(self, **kwargs):
        self.res = {
            'status': None,
            'status_code': None
        }
        try:
            server = os.environ.get('ELASTIC_SERVER')
            self.el = Elasticsearch(
                [{'host': server,
                  'port': 9200}])
            if not self.el.ping():
                self.res['status'] = 'Error'
                self.res['status_code'] = 503
        except Exception as e:
            self.res['status'] = 'Error'
            self.res['status_code'] = 503
            app.logger.error('Error Conecting Elasticserch')
            app.logger.error('Error detail: {}'.format(e))

    def insert_el(self, index, data):
        try:
            resp_dict = self.el.index(
                index=index,
                body=data,
                refresh=True
            )
            self.res['doc_id'] = resp_dict['_id']
            self.res['status'] = 'Success'
            self.res['status_code'] = 200
        except Exception as e:
            self.res['status'] = 'Error'
            if not self.res['status_code']:
                self.res['status_code'] = 400
            self.res['doc_id'] = None

            app.logger.error(self.res['status'])
            app.logger.error(
                'Error inserting document in index {}. \
                    Error detail: {}'.format(index, e))
        return self.res

    def update_el(self, index, _id, data):
        try:
            self.el.update(
                index=index,
                id=_id,
                body={'doc': data},
                refresh=True
            )

            self.res['status'] = 'Success'
            self.res['status_code'] = 200
        except Exception as e:
            self.res['status'] = 'Error'
            if not self.res['status_code']:
                self.res['status_code'] = 400
            app.logger.error(self.res['status'])
            app.logger.error(
                'Error updating document in index {}. \
                Error detail: {}'.format(index, e))
        return self.res

    def retrieve_id_el(self, index, _id, model=None):
        try:
            if not model:
                model = {}

            self.res = self.el.get(
                index=index,
                id=_id)

            model['doc_id'] = _id
            for key in self.res['_source']:
                model[key] = self.res['_source'][key]

            self.res = model
            self.res['status'] = 'Success'
            self.res['status_code'] = 200

        except Exception as e:
            self.res['status'] = 'Error'
            if not self.res['status_code']:
                self.res['status_code'] = e.status_code
            app.logger.error(self.res['status'])
            app.logger.error(
                'Error getting document in index {}. \
                Error detail: {}'.format(index, e))
        return self.res

    def retrieve_el(self, index, unique_hash_field,
                    unique_hash_value, model=None):
        try:
            if not model:
                model = {}

            self.res = self.el.search(
                index=index,
                body={'query':
                      {'match_phrase': {
                          unique_hash_field: unique_hash_value}}})
            self.res['status'] = 'Success'
            self.res['status_code'] = 200

            self.res['resp_list'] = []

            for doc in self.res['hits']['hits']:

                resp_dict = model.copy()

                for key in doc['_source']:
                    resp_dict[key] = doc['_source'][key]

                resp_dict['doc_id'] = doc['_id']

                self.res['resp_list'].append(resp_dict)

            if not self.res['resp_list']:
                self.res['status_code'] = 404

            return {'resp_list': self.res['resp_list'],
                    'status': self.res['status'],
                    'status_code': self.res['status_code']}

        except Exception as e:
            self.res['status'] = 'Error'
            if not self.res['status_code']:
                self.res['status_code'] = e.status_code
            app.logger.error(self.res['status'])
            app.logger.error(
                'Error getting document in index {}. \
                Error detail: {}'.format(index, e))
        return self.res

    def retrieve_all_el(self, index):
        try:

            self.res = self.el.search(
                index=index,
                body={'query':
                      {'match_all': {}}})
            self.res['status'] = 'Success'
            self.res['status_code'] = 200

            if self.res['status'] == 'Success':

                self.res['resp_list'] = []

                for doc in self.res['hits']['hits']:

                    resp_dict = {}

                    resp_dict['doc_id'] = doc['_id']

                    for key in doc['_source']:
                        resp_dict[key] = doc['_source'][key]

                    self.res['resp_list'].append(resp_dict)

                if not self.res['resp_list']:
                    self.res['status_code'] = 404

                return {'resp_list': self.res['resp_list'],
                        'status': self.res['status'],
                        'status_code': self.res['status_code']}

        except Exception as e:
            self.res['status'] = 'Error'
            if not self.res['status_code']:
                self.res['status_code'] = e.status_code
            app.logger.error(self.res['status'])
            app.logger.error(
                'Error getting document in index {}. \
                Error detail: {}'.format(index, e))
        return self.res

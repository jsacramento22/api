import datetime

from flask import Flask, jsonify

import server_conector

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class ErrorCodesView():

    def __init__(self, **kwargs):
        self.el = server_conector.ServerConector()

    def retrieve_all(self, request, **kwargs):
        resp_list = []

        resp_list = self.el.retrieve_all_el(
            index='sysm_plataform_error_codes')

        return jsonify(resp_list['resp_list']), resp_list['status_code']

    def retrieve_id(self, request, **kwargs):
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        res = self.el.retrieve_id_el(
            index='sysm_plataform_error_codes',
            id=_id)

        return jsonify(res), res['status_code']

    def retrieve_code(self, error_code, **kwargs):
        resp_dict = {}

        res = self.el.retrieve_el(
            unique_hash_field='error_code',
            unique_hash_value=error_code,
            index='sysm_plataform_error_codes')

        if res['resp_list']:
            resp_dict = res['resp_list'][0]
        else:
            resp_dict['error_message'] = 'Erro não cadastrado'
        return resp_dict

    def update(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        for key in data:
            resp_dict[key] = data[key]

        resp_dict['last_update'] = datetime.datetime.now()

        res = self.el.update_el(
            index='sysm_plataform_error_codes',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao editar documento.'
        else:
            resp_dict['status_desc'] = 'Documento editado com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def insert(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        if not data.get('error_category', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo error_category não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        if not data.get('error_type', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo error_type não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        if not data.get('error_code', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo error_code não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        if not data.get('error_message', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo error_message não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        if not data.get('error_solution_description', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo error_solution_description ' + \
                'não especificado.'
            return jsonify(resp_dict), 400

        if not data.get('error_notes', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo error_notes não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        for key in data:
            resp_dict[key] = data[key]

        resp_dict['record_status'] = 'Active'
        resp_dict['creation_date'] = datetime.datetime.now()
        resp_dict['last_update'] = resp_dict['creation_date']

        res = self.el.insert_el(
            index='sysm_plataform_error_codes', data=resp_dict)

        resp_dict['status'] = res['status']
        resp_dict['doc_id'] = res['doc_id']

        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao inserir documento.'
        else:
            resp_dict['status_desc'] = 'Documento inserido com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def deactivate(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_dict['record_status'] = 'Inactive'
        resp_dict['last_update'] = datetime.datetime.now()
        resp_dict['last_update_user'] = data.get('last_update_user', '')

        res = self.el.update_el(
            index='sysm_plataform_error_codes',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao desativar documento.'
        else:
            resp_dict['status_desc'] = 'Documento desativado com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def activate(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_dict['record_status'] = 'Active'
        resp_dict['last_update'] = datetime.datetime.now()
        resp_dict['last_update_user'] = data.get('last_update_user', '')

        res = self.el.update_el(
            index='sysm_plataform_error_codes',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao ativar documento.'
        else:
            resp_dict['status_desc'] = 'Documento ativado com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def delete(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_dict['record_status'] = 'Deleted'
        resp_dict['last_update'] = datetime.datetime.now()
        resp_dict['last_update_user'] = data.get('last_update_user', '')

        res = self.el.update_el(
            index='sysm_plataform_error_codes',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao deletar documento.'
        else:
            resp_dict['status_desc'] = 'Documento deletado com sucesso.'

        return jsonify(resp_dict), res['status_code']

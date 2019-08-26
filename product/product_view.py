import datetime

from flask import Flask, jsonify

from models.product.product_model import ProductModel

import server_conector

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class ProductView(ProductModel):

    def __init__(self, **kwargs):
        self.el = server_conector.ServerConector()

    def retrieve(self, request, **kwargs):
        resp_list = []
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        field = data.pop('field', None)
        if not field:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo field não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        value = data.pop('value', None)
        if not value:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo value não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_list = self.el.retrieve_el(
            index='shop_product',
            unique_hash_field=field,
            unique_hash_value=value,
            model=self.get_index_fields())

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
            index='shop_product',
            _id=_id,
            model=self.get_index_fields())

        return jsonify(res), res['status_code']

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
            index='shop_product',
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

        unique_personal_hash = data.get('unique_personal_hash', '')
        if not unique_personal_hash:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo unique_personal_hash não ' + \
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

        resp_dict['unique_product_hash'] = self.unique_product_hash_string(
            unique_personal_hash)

        res = self.el.insert_el(
            index='shop_product', data=resp_dict)

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
            index='shop_product',
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
            index='shop_product',
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
            index='shop_product',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao deletar documento.'
        else:
            resp_dict['status_desc'] = 'Documento deletado com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def unique_product_hash_string(self, unique_personal_hash):
        import json
        import hashlib

        txt_plate_prefix = unique_personal_hash[:3]
        txt_plate_sufix = unique_personal_hash[-3:]
        creation_date = datetime.datetime.now()

        # Transform the date in a Tuple
        date_tuple = creation_date.timetuple()

        txt_salt_0 = date_tuple[0]  # year
        txt_salt_1 = date_tuple[1]  # month
        txt_salt_2 = date_tuple[2]  # day
        txt_salt_3 = date_tuple[3]  # hour
        txt_salt_6 = date_tuple[6]  # day of week

        # Create Hash String
        txt_username = str(txt_salt_6) + txt_plate_prefix + \
            str(txt_salt_0) + '@' + \
            str(txt_salt_1) + txt_plate_sufix + \
            str(txt_salt_2) + str(txt_salt_3)

        # ----------------------------------------------------------------------
        # Using SHA256 -> Pure
        # ----------------------------------------------------------------------
        block_string = json.dumps(txt_username, sort_keys=True).encode()
        unique_product_hash = hashlib.sha256(block_string).hexdigest()

        return unique_product_hash

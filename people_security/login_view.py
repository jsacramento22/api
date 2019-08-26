import datetime
import hashlib
import json
import re

from flask import Flask, jsonify

from models.people_security.login_model import LoginModel

from system.logger_view import LoggerView

import server_conector

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class LoginView(LoginModel):

    def __init__(self, **kwargs):
        self.el = server_conector.ServerConector()

    def retrieve(self, request, **kwargs):
        from people_profile.profile_view import ProfileView

        resp_list = []
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        username = data.pop('username', None)
        if not username:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo username não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_list = self.el.retrieve_el(
            index='myid_people_security_login',
            unique_hash_field='username',
            unique_hash_value=username,
            model=self.get_index_fields())

        return jsonify(resp_list['resp_list']), resp_list['status_code']

    def retrieve_id(self, request, **kwargs):
        resp_dict = {}

        data = request.get_json()
        logger = LoggerView(data)
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            logger.insert_error_message(
                system_category=logger.get_category_operational(),
                system_module=logger.get_module_user(),
                system_activity=logger.get_actinity_read(),
                error_code=1001,
                log_description=resp_dict['status_desc'],
                notify=True)
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            logger.insert_error_message(
                system_category=logger.get_category_operational(),
                system_module=logger.get_module_user(),
                system_activity=logger.get_actinity_read(),
                error_code=1001,
                log_description=resp_dict['status_desc'],
                notify=True)
            return jsonify(resp_dict), 400

        res = self.el.retrieve_id_el(
            index='myid_people_security_login',
            _id=_id,
            model=self.get_index_fields())

        return jsonify(res), res['status_code']

    def update(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        logger = LoggerView(data)
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            logger.insert_error_message(
                system_category=logger.get_category_operational(),
                system_module=logger.get_module_user(),
                system_activity=logger.get_actinity_update(),
                error_code=1001,
                log_description=resp_dict['status_desc'],
                notify=True)
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
            index='myid_people_security_login',
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

        email_account = data.get('email_account', '')
        if not email_account:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo email_account não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        username = data.get('username', '')
        if not username:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo username não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        # ---------------------------------------------------------------------
        #  Creation Date
        # ---------------------------------------------------------------------
        dt_login_creation_date = datetime.datetime.now()

        dt_login_expire_date = dt_login_creation_date + \
            datetime.timedelta(days=90)

        # ---------------------------------------------------------------------
        # Validate if Username already exists
        # ---------------------------------------------------------------------
        retrieve_resp = self.retrieve(request)[0]
        profile = retrieve_resp.get_json()
        profile_email = self.search_profile_email(request)[0].get_json()

        # if user does not exists
        if profile:
            status_code = 400
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Usuário já existe'

        elif profile_email:
            status_code = 400
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'E-mail já existe'

        else:

            # -----------------------------------------------------------------
            # Create Hash
            # -----------------------------------------------------------------
            txt_unique_personal_hash = self.create_unique_personal_hash(
                email_account, dt_login_creation_date)

            # -----------------------------------------------------------------
            # Create Password
            # -----------------------------------------------------------------
            txt_password = self.validade_user_password('Pl4c3h0ld3r!')

            resp_dict['unique_personal_hash'] = \
                txt_unique_personal_hash
            resp_dict['email_account'] = email_account
            resp_dict['username'] = username
            resp_dict['password'] = txt_password['hash_password']

            resp_dict['attemp_qtd'] = 0
            resp_dict['attemp_limit'] = 3

            resp_dict['login_status'] = 'CONFIRMATION'
            resp_dict['password_expire_date'] = \
                dt_login_expire_date

            resp_dict['record_status'] = 'Active'
            resp_dict['creation_date'] = dt_login_creation_date
            resp_dict['last_update'] = dt_login_creation_date
            resp_dict['last_update_user'] = username

            res = self.el.insert_el(
                index='myid_people_security_login', data=resp_dict)
            resp_dict['status'] = res['status']
            if res['status'] == 'Error':
                resp_dict['status_desc'] = 'Erro ao inserir documento.'
            else:
                resp_dict['status_desc'] = \
                    'Documento inserido com sucesso.'

            status_code = res['status_code']
            print(res['doc_id'])
            resp_dict['doc_id'] = res['doc_id']

        return jsonify(resp_dict), status_code

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
            index='myid_people_security_login',
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
            index='myid_people_security_login',
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
            index='myid_people_security_login',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao deletar documento.'
        else:
            resp_dict['status_desc'] = 'Documento deletado com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def unique_personal_hash_string(self, email_account, creation_date):

        txt_email_account = email_account.split('@')
        txt_user_prefix = txt_email_account[0]
        txt_email_domain = txt_email_account[1]
        user_creation_date = creation_date

        # Transform the date in a Tuple
        date_tuple = user_creation_date.timetuple()

        txt_salt_0 = date_tuple[0]
        txt_salt_1 = date_tuple[1]
        txt_salt_2 = date_tuple[2]
        txt_salt_3 = date_tuple[3]
        txt_salt_6 = date_tuple[6]

        # Create Hash String
        txt_username = str(txt_salt_6) + txt_user_prefix + \
            str(txt_salt_0) + '@' + str(txt_salt_1) + \
            txt_email_domain + str(txt_salt_2) + str(txt_salt_3)

        return txt_username

    def create_unique_personal_hash(self, email_account, creation_date):

        txt_username = self.unique_personal_hash_string(
            email_account, creation_date)

        # --------------------------------------------------------------------
        # Using SHA256 -> Pure
        # --------------------------------------------------------------------
        block_string = json.dumps(txt_username, sort_keys=True).encode()
        txt_unique_personal_hash = hashlib.sha256(block_string).hexdigest()

        return txt_unique_personal_hash

    def validade_user_password(self, password):
        """
        Verify the strength of 'password'.

        Returns a dict indicating the wrong criteria
        A password is considered strong if:
            8 characters length or more
            1 digit or more
            1 symbol or more
            1 uppercase letter or more
            1 lowercase letter or more
        """
        # calculating the length
        length_error = 'A senha precisa ter ao menos oito caracteres' \
            if len(password) < 8 else False

        # searching for digits
        digit_error = 'A senha precisa ter ao menos um número' \
            if not re.search(r'\d', password) else False
        # searching for uppercase
        uppercase_error = 'A senha precisa ter ao menos um caractere ' + \
            'maiúsculo' if not re.search(r'[A-Z]', password) else False

        # searching for lowercase
        lowercase_error = 'A senha precisa ter ao menos um caractere ' + \
            'minúsculo' if not re.search(r'[a-z]', password) else False

        # searching for symbols
        symbol_error = 'A senha precisa ter ao menos um  dos caracteres ' + \
            'especiais: !@#$%&\'()*+,-./[\\]^_`{|}~' \
            if not re.search(
                r'[ !@#$%&\'()*+,-./[\\\]^_`{|}~' + r']', password) else False

        # overall result
        password_ok = not (
            length_error or digit_error or
            uppercase_error or lowercase_error or symbol_error)

        if password_ok:
            # -----------------------------------------------------------------
            # Using SHA256 -> Pure
            # -----------------------------------------------------------------
            txt_password = self.return_user_password_hash(password)

        else:
            txt_password = None

        return {
            'password_ok': password_ok,
            'length_error': length_error,
            'digit_error': digit_error,
            'uppercase_error': uppercase_error,
            'lowercase_error': lowercase_error,
            'symbol_error': symbol_error,
            'hash_password': txt_password,
        }

    # -----------------------------------------------------------------------------
    # Return the Hash of Password
    # -----------------------------------------------------------------------------
    def return_user_password_hash(self, password):

        txt_password = password

        # ---------------------------------------------------------------------
        # Using SHA256 -> Pure
        # ---------------------------------------------------------------------
        block_string = json.dumps(txt_password, sort_keys=True).encode()
        txt_password = hashlib.sha256(block_string).hexdigest()

        return txt_password

    def search_profile_email(self, request):

        resp_list = []
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        email_account = data.pop('email_account', None)
        if not email_account:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo email_account não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_list = self.el.retrieve_el(
            index='myid_people_security_login',
            unique_hash_field='email_account',
            unique_hash_value=email_account,
            model=self.get_index_fields())

        return jsonify(resp_list['resp_list']), resp_list['status_code']

    # -------------------------------------------------------------------------
    # User Login Attempt
    # -------------------------------------------------------------------------
    def validate_login(self, request):
        from people_profile.profile_view import ProfileView
        # Trace Variables
        # system_category = 'PEOPLE'
        # system_module = 'USER_LOGIN'
        # system_activity = 'LOGIN_ATTEMPT'
        # log_category = None
        # log_description = None

        resp_dict = {}
        status_code = 200

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        password = data.get('password', '')
        if not password:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo password não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        username = data.get('username', '')
        if not username:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo username não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        '''
            All the API functions return a tuple with the first value being
            the response object and the second a HTML status code.
            resp_dict gets the response object and the json inside it.
            All the API self.retrive() functions returns a list of values,
            so it gets the first object.
        '''
        resp_list = self.retrieve(request)[0].get_json()
        if resp_list:
            resp_dict = resp_list[0]
            doc_id = resp_dict['doc_id']

            # Add Attempt Login
            if resp_dict is None:
                resp_dict['attemp_qtd'] = 0

            resp_dict['attemp_qtd'] = resp_dict['attemp_qtd'] + 1

            # Validate Status
            if resp_dict['login_status'].upper() != 'ACTIVE':

                # log_category = 'UNSUCESS'

                resp_dict['status'] = 'Error'
                resp_dict['status_desc'] = 'Usuário bloqueado até: ' + \
                    str(resp_dict['login_blocked_until'])

            else:

                if int(resp_dict['attemp_qtd']) > resp_dict['attemp_limit']:

                    # log_category = 'ERROR'

                    resp_dict['status'] = 'Error'
                    resp_dict['status_desc'] = 'Tentativas de login excessivas'

                    resp_dict['login_blocked_until'] = \
                        datetime.datetime.now() + datetime.timedelta(days=30)
                    resp_dict['login_status'] = 'BLOCKED'

                else:

                    # Validate Password
                    if resp_dict['password'] != self.return_user_password_hash(
                            password):

                        # log_category = 'ERROR'

                        resp_dict['status'] = 'Error'
                        resp_dict['status_desc'] = \
                            'Nome de usuário e/ou Senha inválido(s)'

                    else:

                        # resp_dict[ 'password' ] = password

                        # Validate Blocked Until Date
                        if resp_dict['login_blocked_until'] is None or \
                                resp_dict['login_blocked_until'] < \
                                datetime.datetime.now():

                            # log_category = 'SUCESS'
                            resp_dict['status'] = 'Success'
                            resp_dict['status_desc'] = 'Acesso concedido'

                            resp_dict['attemp_qtd'] = 0
                            resp_dict['last_login_sucessfull'] = \
                                datetime.datetime.now()

                            profile_dict = ProfileView().retrieve_constructor(
                                resp_dict['unique_personal_hash'])[0].get_json()

                            if profile_dict:
                                resp_dict = {
                                    **profile_dict[0],
                                    **resp_dict}

            # -----------------------------------------------------------------
            # Update Login Data
            # -----------------------------------------------------------------
            res = self.el.update_el(
                index='myid_people_security_login',
                _id=doc_id,
                data={
                    'last_login_sucessfull':
                        resp_dict['last_login_sucessfull'],
                    'last_login_attempt':
                        resp_dict['last_login_attempt'],
                    'attemp_qtd':
                        resp_dict['attemp_qtd'],
                    'login_status':
                        resp_dict['login_status'],
                    'login_blocked_until':
                        resp_dict['login_blocked_until']
                })
            '''
                res is a tuple with two values: the first is a response
                and the second a HTML status code.
                if the status code from res isn't 200, return it
            '''
            if res['status_code'] != status_code:
                status_code = res['status_code']

        else:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Login inválido'

            resp_dict['username'] = username
            resp_dict['password'] = password

        # login_trace.user_login_trace( es_object, log_category, \
            # resp_dict['unique_personal_hash'] , resp_dict['username'], \
            # system_category, system_module, \
            # system_activity, log_description)

        return jsonify(resp_dict), status_code

    # -------------------------------------------------------------------------
    # User Login First Validate - Just For Logins with Status = CONFIRMATION
    # -------------------------------------------------------------------------
    def validade_first_login(self, request):

        # Trace Variables
        # system_category = 'PEOPLE'
        # system_module = 'USER_LOGIN'
        # system_activity = 'LOGIN_CONFIRMATION'
        # log_category = None
        # log_description = None

        resp_dict = {}
        resp_profile = {}
        status_code = 200

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        password_old = data.get('password_old', '')
        if not password_old:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo password_old não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        password_new = data.get('password_new', '')
        if not password_new:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo password_new não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        password_retype = data.get('password_retype', '')
        if not password_retype:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo password_retype não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        username = data.get('username', '')
        if not username:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo username não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        email_account = data.get('email_account', '')
        if not email_account:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo email_account não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        first_name = data.get('first_name', '')
        if not first_name:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo first_name não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        last_name = data.get('last_name', '')
        if not last_name:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_name não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_list = self.retrieve(request)[0].get_json()

        # If user Exists
        if resp_list:
            resp_dict = resp_list.pop()

            # Check Old Password
            if resp_dict['password'] != self.return_user_password_hash(
                    password_old):
                # log_category = 'ERROR'
                resp_dict['status'] = 'Error'
                resp_dict['status_desc'] = \
                    'Nome de usuário e/ou Senha inválido(s)'

            else:
                # If login status is CONFIRMATION
                if resp_dict['login_status'] == 'CONFIRMATION':
                    # if new password not equal then old password
                    if password_old != password_new:
                        # if new password match with retype password
                        if password_new == password_retype:
                            # -------------------------------------------------
                            # Create Password
                            # -------------------------------------------------
                            txt_password = self.validade_user_password(
                                password_new)

                            # if new password is OK
                            if txt_password['password_ok']:
                                # log_category = 'SUCESS'

                                resp_dict['status'] = 'Success'
                                resp_dict['status_desc'] = \
                                    'Login validado com sucesso'

                                # ---------------------------------------------
                                # Update Login Data
                                # ---------------------------------------------
                                try:
                                    self.el.update_el(
                                        index='myid_people_security_login',
                                        _id=resp_dict['doc_id'],
                                        data={
                                            'password':
                                                txt_password[
                                                    'hash_password'],
                                            'attemp_qtd': 0,
                                            'login_status': 'ACTIVE',
                                            'last_update':
                                                datetime.datetime.now(),
                                            'last_update_user': username
                                        })
                                    resp_dict['login_status'] = 'ACTIVE'
                                except Exception as e:
                                    print(e)

                                try:
                                    from people_profile.profile_view \
                                        import ProfileView

                                    resp_profile['unique_personal_hash'] = \
                                        resp_dict['unique_personal_hash']
                                    resp_profile['last_update_user'] = \
                                        resp_dict['last_update_user']
                                    resp_profile['first_name'] = first_name
                                    resp_profile['last_name'] = last_name

                                    ProfileView().insert(
                                        request, **resp_profile)

                                except Exception as e:
                                    print(e)
                            else:

                                # log_category = 'ERROR'
                                resp_dict['status'] = 'Error'
                                resp_dict['status_desc'] = \
                                    'Nova senha não atende o ' + \
                                    'critério de segurança'

                        else:

                            # log_category = 'ERROR'
                            resp_dict['status'] = 'Error'
                            resp_dict['status_desc'] = \
                                'A senha e a confirmação não são iguais.'

                    else:

                        # log_category = 'ERROR'
                        resp_dict['status'] = 'Error'
                        resp_dict['status_desc'] = 'Nova senha já usada.'

                else:

                    # log_category = 'ERROR'
                    resp_dict['status'] = 'Error'
                    resp_dict['status_desc'] = 'O status do login não ' + \
                        'precisa de validação: ' + resp_dict['login_status']

        else:

            # log_category = 'ERROR'

            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Usuário inválido'

        # login_trace.user_login_trace( log_category, \
            # resp_dict['unique_personal_hash'], \
            # resp_dict[ 'username' ], system_category, \
            # system_module, system_activity, log_description )

        return jsonify(resp_dict), status_code

    # -------------------------------------------------------------------------
    # User Login Reset
    # -------------------------------------------------------------------------
    def reset_password_login(self, request):
        # Trace Variables
        # system_category = 'PEOPLE'
        # system_module = 'USER_LOGIN'
        # system_activity = 'PASSWORD_RESET'
        # log_category = None
        # log_description = None

        resp_dict = {}
        status_code = 200

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        password_new = data.get('password_new', '')
        if not password_new:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo password_new não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        password_retype = data.get('password_retype', '')
        if not password_retype:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo password_retype não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        username = data.get('username', '')
        if not username:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo username não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_dict = self.retrieve(request)[0].get_json()[0]

        # If user Exists
        if len(resp_dict['unique_personal_hash']) > 0:

            # if new password match with retype password
            if password_new == password_retype:
                # -------------------------------------------------
                # Create Password
                # -------------------------------------------------
                txt_password = self.validade_user_password(
                    password_new)

                # if new password is OK
                if txt_password['password_ok']:
                    # log_category = 'SUCESS'

                    resp_dict['status'] = 'Success'
                    resp_dict['status_desc'] = \
                        'Login validado com sucesso'

                    # ---------------------------------------------
                    # Update Login Data
                    # ---------------------------------------------
                    try:
                        self.el.update_el(
                            index='myid_people_security_login',
                            _id=resp_dict['doc_id'],
                            data={
                                'password':
                                    txt_password[
                                        'hash_password'],
                                'attemp_qtd': 0,
                                'login_status': 'ACTIVE',
                                'login_blocked_until': None,
                                'last_update':
                                    datetime.datetime.now(),
                                'last_update_user': username
                            })
                    except Exception as e:
                        print(e)

                else:

                    # log_category = 'ERROR'
                    resp_dict['status'] = 'Error'
                    resp_dict['status_desc'] = \
                        'Nova senha não atende o ' + \
                        'critério de segurança'

            else:

                # log_category = 'ERROR'
                resp_dict['status'] = 'Error'
                resp_dict['status_desc'] = \
                    'A senha e a confirmação não são iguais.'

        else:

            # log_category = 'ERROR'

            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Usuário inválido'

        # login_trace.user_login_trace( log_category, \
            # resp_dict['unique_personal_hash'], \
            # resp_dict[ 'username' ], system_category, \
            # system_module, system_activity, log_description )

        return jsonify(resp_dict), status_code

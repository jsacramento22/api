from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class LoginModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'email_account': None,
            'username': None,
            'password': None,
            'phone_number': None,
            'doc_cpf_number': None,
            'last_login_sucessfull': None,
            'last_login_attempt': None,
            'attemp_qtd': None,
            'attemp_limit': None,
            'password_reminder_question': None,
            'password_reminder_answer': None,
            'login_status': None,
            'login_blocked_until': None,
            'password_expire_date': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

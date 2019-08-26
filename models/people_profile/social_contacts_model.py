from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class SocialContactsModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'contact_group': None,
            'first_name': None,
            'last_name': None,
            'birth_date': None,
            'email_account': None,
            'phone': None,
            'social_media': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

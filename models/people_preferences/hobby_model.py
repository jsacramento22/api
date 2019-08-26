from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class HobbyModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_hobby_hash': '',
            'hobby_type': None,
            'hobby_category': None,
            'hobby_sub_category': None,
            'hobby_brand': None,
            'hobby_tag': None,
            'hobby_description': None,
            'personal_notes': None,
            'hobby_type_logo_path': None,
            'hobby_category_logo_path': None,
            'hobby_brand_logo_path': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

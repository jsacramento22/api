from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class MyClosetModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_closet_hash': '',
            'item_category': None,
            'item_type': None,
            'brand': None,
            'model': None,
            'version': None,
            'purchase_date': None,
            'personal_notes': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

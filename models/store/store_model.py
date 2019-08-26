from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class StoreModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_store_hash': '',
            'unique_owner_hash': '',
            'shop_ranking': None,
            'title': None,
            'short_description': None,
            'description': None,
            'notes': None,
            'company_type': None,
            'company_id_number': None,
            'company_id_state_inscription': None,
            'company_id_city_inscription': None,
            'category_main': None,
            'category_type': None,
            'category_subtype': None,
            'email_account': None,
            'address': None,
            'phone': None,
            'social_media': None,
            'visual_identity': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None
        }

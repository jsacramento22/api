from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class MyPetRecordModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_pet_hash': None,
            'event_id': None,
            'event_type': None,
            'event_category': None,
            'event_date': None,
            'event_title': None,
            'event_description': None,
            'personal_notes': None,
            'shop_name': None,
            'total_cost': None,
            'record_image1_path': None,
            'record_image2_path': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

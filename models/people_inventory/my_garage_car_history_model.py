from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class MyGarageCarHistoryModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_vehicle_hash': '',
            'event_id': None,
            'event_type': None,
            'event_category': None,
            'event_date': None,
            'event_title': None,
            'event_description': None,
            'my_notes': None,
            'odometer': None,
            'shop_name': None,
            'item_amount': None,
            'unit_cost': None,
            'total_cost': None,
            'personal_notes': None,
            'history_image1_path': None,
            'history_image2_path': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

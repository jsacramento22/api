from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class MyContainerItensModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_container_hash': '',
            'item_brand': None,
            'item_model': None,
            'item_serie': None,
            'item_description': None,
            'manufacturer_information': None,
            'technical_specs': None,
            'purchase_date': None,
            'purchase_shop': None,
            'purchase_value': None,
            'is_collectibled': None,
            'is_desirebled': None,
            'item_tag': None,
            'appraisel_date': None,
            'appraisel_value': None,
            'appraisel_note': None,
            'personal_notes': None,
            'item_image1_path': None,
            'item_image2_path': None,
            'item_image3_path': None,
            'item_image4_path': None,
            'item_image5_path': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

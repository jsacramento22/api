from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class GourmetModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_gourmet_hash': '',
            'gourmet_type': None,
            'gourmet_category': None,
            'gourmet_sub_category': None,
            'gourmet_brand': None,
            'gourmet_model': None,
            'gourmet_serie': None,
            'gourmet_tag': None,
            'gourmet_description': None,
            'personal_notes': None,
            'gourmet_type_logo_path': None,
            'gourmet_category_logo_path': None,
            'gourmet_brand_logo_path': None,
            'gourmet_product_image_path': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

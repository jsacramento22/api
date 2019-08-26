from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class ProductsModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_product_hash': "",
            'product_type': None,
            'product_category': None,
            'product_brand': None,
            'product_model': None,
            'product_serie': None,
            'product_tag': None,
            'product_description': None,
            'personal_notes': None,
            'product_type_logo_path': None,
            'product_category_logo_path': None,
            'product_brand_logo_path': None,
            'product_model_image_path': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

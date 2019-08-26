from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class ProductModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_product_hash': '',
            'category_main': None,
            'category_type': None,
            'category_subtype': None,
            'manufacturer_description': None,
            'manufacturer_features': None,
            'manufacturer_brand': None,
            'manufacturer_model': None,
            'manufacturer_version': None,
            'delivery_type': None,
            'title': None,
            'description': None,
            'notes': None,
            'status': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

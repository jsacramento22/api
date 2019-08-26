from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class SalesEngineSetupModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_marketplace_hash': '',
            'unique_inventory_hash': '',
            'unique_store_hash': '',
            'unique_owner_hash': '',
            'unique_product_hash': '',
            'sale_engine_category': None,
            'is_private_sale': None,
            'setup_end_date': None,
            'sale_status': None,
            'merchandising_message': None,
            'is_price_negotiable': None,
            'price_list': None,
            'price_current': None,
            'instant_offer': None,
            'price_reserved': None,
            'payment_type': None,
            'shipping_type': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

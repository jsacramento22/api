from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class SalesNegotiationHistoryModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_marketplace_hash': '',
            'unique_inventory_hash': '',
            'unique_store_hash': '',
            'unique_owner_hash': '',
            'unique_product_hash': '',
            'unique_negotiation_hash': '',
            'sale_engine_category': None,
            'negotiation_date': None,
            'negotiation_amount': None,
            'buyer_unique_hash': None,
            'is_negotiation_accepted': None,
            'negotiation_notes': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

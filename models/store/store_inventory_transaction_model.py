from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class StoreInventoryTransactionModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_inventory_hash': '',
            'unique_store_hash': '',
            'unique_product_hash': '',
            'product_sku_id': None,
            'transaction_type': None,
            'transaction_date': None,
            'transaction_hash': None,
            'buyer_hash': None,
            'seller_hash': None,
            'transaction_unit_price': None,
            'transaction_qty': None,
            'transaction_qty_before': None,
            'transaction_qty_after': None,
            'transaction_total_amount': None,
            'transaction_notes': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class SalesTransactionsModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_marketplace_hash': '',
            'unique_inventory_hash': '',
            'unique_store_hash': '',
            'unique_owner_hash': '',
            'unique_product_hash': '',
            'unique_transaction_hash': '',
            'buyer_unique_hash': None,
            'sale_engine_category': None,
            'transaction_date': None,
            'product_price_list': None,
            'product_sell_list': None,
            'product_qtd': None,
            'transaction_amount': None,
            'campaign_unique_hash': None,
            'salesperson_unique_hash': None,
            'referred_by_login_hash': None,
            'comission_rate': None,
            'comission_amount': None,
            'comission_fee_payment_hash': None,
            'plataform_rate': None,
            'plataform_amount': None,
            'plataform_fee_payment_hash': None,
            'shipping_type': None,
            'shipping_details': None,
            'shipping_costs': None,
            'shipping_status': None,
            'is_delivered': None,
            'transaction_notes': None,
            'payment_type': None,
            'payment_history': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

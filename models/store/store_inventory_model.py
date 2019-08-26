from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class StoreInventoryModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_inventory_hash': '',
            'unique_store_hash': '',
            'unique_product_hash': '',
            'product_sku_id': None,
            'product_sell_points': None,
            'product_reward_points': None,
            'is_new_banner_logo': None,
            'new_banner_begin_date': None,
            'new_banner_end_date': None,
            'stock_min_alert': None,
            'stock_max': None,
            'stock_max_cart': None,
            'stock_current': None,
            'stock_avg_item_cost': None,
            'stock_min_item_cost': None,
            'stock_max_item_cost': None,
            'zero_stock_sell': None,
            'product_search_rate': None,
            'product_search_tags': None,
            'sponsored_item': None,
            'digital_url': None,
            'campaign': None,
            'visibility': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

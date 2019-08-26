from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class ProductInventoryModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'product_sku_id': '',
            'unique_store_hash': '',
            'unique_product_hash': '',
            'product_sell_points': None,
            'product_reward_points': None,
            'enable_cupons': None,
            'is_new_banner_logo': None,
            'new_banner_begin_date': None,
            'new_banner_end_date': None,
            'enale_virtual_stock': None,
            'inherit_stock_shop': None,
            'inheritee_shop': None,
            'stock_type': None,
            'enabled_managed_stock': None,
            'notification_min_stock': None,
            'notification_out_stock': None,
            'min_stock_threshold': None,
            'max_stock_threshold': None,
            'max_cart_threshold': None,
            'stock_current': None,
            'enable_zero_stock_sell': None,
            'notification_email': None,
            'stock_avg_item_cost': None,
            'stock_min_item_cost': None,
            'stock_max_item_cost': None,
            'stock_current_item_cost': None,
            'shipping_type': None,
            'shipping_time': None,
            'fulfilled_by': None,
            'handling_time': None,
            'product_search_rate': None,
            'product_search_tags': None,
            'enable_catalog_visibility': None,
            'catalog_visibility_begin': None,
            'catalog_visibility_end': None,
            'is_sponsored_item': None,
            'is_featured': None,
            'enable_vocher': None,
            'enable_instant_offer': None,
            'percent_instant_offer': None,
            'currency_type': None,
            'list_price': None,
            'campaign': None,
            'affiliate_ranking_search': None,
            'affiliate_ranking_sell': None,
            'affiliate_ranking_comission': None,
            'affiliatee': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None
        }

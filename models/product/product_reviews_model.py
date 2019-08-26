from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class ProductReviewsModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_store_hash': '',
            'unique_product_hash': '',
            'product_sku_id': None,
            'avg_score_size': None,
            'avg_score_quality': None,
            'avg_score_price': None,
            'avg_score_delivery': None,
            'avg_score_package': None,
            'avg_score_description': None,
            'avg_score_recomendation': None,
            'user_reviews': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None
        }

from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class ScoreCardModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'engagement_plataform': None,
            'engagement_marketing': None,
            'spent_product': None,
            'spent_service': None,
            'geo_location': None,
            'fraud': None,
            'money_laundry': None,
            'churn': None,
            'referenced_by_total': None,
            'refer_to_total': None,
            'afiliate_earnings_amount': None,
            'afiliate_products_total': None,
            'ticket_spend_avg': None,
            'ticket_spend_max': None,
            'balance_avg': None,
            'balance_max': None,
            'last_recharge_date': None,
            'recharge_days_avg': None,
            'last_recharge_amount': None,
            'recharge_amount_avg': None,
            'days_until_last_login': None,
            'days_until_last_buy': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

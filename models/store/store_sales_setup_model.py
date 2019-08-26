from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class StoreSalesSetupModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'store_sales_setup_hash': '',
            'store_hash': '',
            'enable_cashback_program': None,
            'gbu': None,
            'territory': None,
            'fiscal_year': None,
            'sales_cycle': None,
            'sales_performance_level': None,
            'sales_performance_level_threshold': None,
            'sales_level_kpi': None,
            'team_level_kpi': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

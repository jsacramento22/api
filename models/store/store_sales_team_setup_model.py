from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class StoreSalesTeamSetupModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_sales_team_hash': '',
            'unique_store_hash': '',
            'team_ranking': None,
            'team_title': None,
            'shop_team_identification': None,
            'team_description': None,
            'notes': None,
            'gbu_hash': None,
            'territory_hash': None,
            'current_level_hash': None,
            'previous_level_hash': None,
            'next_level_entries': None,
            'is_top_level': None,
            'team_leader_hash': None,
            'team_leader_name': None,
            'team_members': None,
            'team_members_kpi': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

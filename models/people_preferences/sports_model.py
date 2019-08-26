from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class SportsModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_sport_hash': '',
            'sport_type': None,
            'sport_category': None,
            'sport_team': None,
            'sport_player': None,
            'sport_tag': None,
            'sport_description': None,
            'personal_notes': None,
            'sport_type_logo_path': None,
            'sport_category_logo_path': None,
            'sport_team_logo_path': None,
            'sport_player_image_path': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

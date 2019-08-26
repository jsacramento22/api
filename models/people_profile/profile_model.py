from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class ProfileModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'first_name': None,
            'last_name': None,
            'birth_date': None,
            'birth_location_country': None,
            'birth_location_state': None,
            'birth_location_city': None,
            'ethnicity': None,
            'gender': None,
            'sexual_orientation': None,
            'marital_status': None,
            'facebook': None,
            'instagram': None,
            'linkedin': None,
            'twitter': None,
            'language': None,
            'scorecard_topics': None,
            'profile_image_path': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

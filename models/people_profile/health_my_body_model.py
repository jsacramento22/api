from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class HealthMyBodyModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'height': None,
            'neck': None,
            'shoulder': None,
            'bicep': None,
            'sleeve': None,
            'chest': None,
            'underbust': None,
            'bra': None,
            'waist': None,
            'high_hip': None,
            'low_hip': None,
            'thigh': None,
            'inseam': None,
            'foot': None,
            'outfit_type': None,
            'outfit_size': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

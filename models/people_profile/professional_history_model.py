from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class ProfessionalHistoryModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'work_period': None,
            'start_date': None,
            'end_date': None,
            'is_current': None,
            'company_name': None,
            'based_location': None,
            'job_title': None,
            'job_headline': None,
            'job_description': None,
            'personal_notes': None,
            'accomplishment_date': None,
            'accomplishment_type': None,
            'accomplishment_description': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

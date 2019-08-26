from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class StoreSalesTeamApplyModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_store_hash': '',
            'unique_salesman_hash': '',
            'apply_date': None,
            'applicant_title': None,
            'applicant_description': None,
            'apply_status': None,
            'apply_answer': None,
            'store_disclaimer': None,
            'store_disclaimer_agreement': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class HealthPrescriptionModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'issued_date': None,
            'doctor_name': None,
            'doctor_id': None,
            'medicine_id': None,
            'medicine_name': None,
            'manufacturer_name': None,
            'medicine_purpose': None,
            'medicine_instructions': None,
            'drug_name': None,
            'is_generic': None,
            'active_substance': None,
            'shape': None,
            'route': None,
            'dose': None,
            'unit': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

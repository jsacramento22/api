from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class MyPetModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_pet_hash': '',
            'specie_type': None,
            'breed': None,
            'pet_name': None,
            'image_path': None,
            'birth_date': None,
            'colour': None,
            'gender': None,
            'microchip_number': None,
            'personal_notes': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

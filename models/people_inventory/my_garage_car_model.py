from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class MyGarageCarModel():

    def get_index_fields(self):
        return {
            'doc_id': None,
            'unique_personal_hash': '',
            'unique_vehicle_hash': '',
            'vehicle_title': None,
            'vehicle_vin_number': None,
            'vehicle_doc_number': None,
            'vehicle_registration_plate': None,
            'vehicle_make': None,
            'vehicle_model': None,
            'vehicle_trim': None,
            'year_make': None,
            'year_model': None,
            'odometer': None,
            'style_body_type': None,
            'style_seats': None,
            'style_doors': None,
            'style_exterior_color': None,
            'style_interior_color': None,
            'engine_type': None,
            'engine_cc': None,
            'engine_cylinders': None,
            'engine_fuel': None,
            'engine_transmission': None,
            'engine_drive_type': None,
            'option_is_armored': None,
            'all_features': None,
            'vehicle_image1_path': None,
            'vehicle_image2_path': None,
            'vehicle_image3_path': None,
            'vehicle_image4_path': None,
            'vehicle_image5_path': None,
            'purchase_date': None,
            'purchase_shop': None,
            'purchase_value': None,
            'is_financed': None,
            'finance_company': None,
            'down_payment': None,
            'month_total': None,
            'monthly_amount': None,
            'payment_period': None,
            'start_payment_date': None,
            'record_status': None,
            'creation_date': None,
            'last_update': None,
            'last_update_user': None,
        }

import os

from flask import Flask, jsonify, request

from flask_cors import CORS

from lookups.people import closet_cloth_categories_view
from lookups.people import closet_cloth_types_view
from lookups.people import contact_address_types_view
from lookups.people import document_types_view
from lookups.people import education_degree_types_view
from lookups.people import family_relationships_view
from lookups.people import garage_vehicle_brands_view
from lookups.people import garage_vehicle_models_view
from lookups.people import garage_vehicle_types_view
from lookups.people import gourmet_brands_view
from lookups.people import gourmet_categories_view
from lookups.people import gourmet_models_view
from lookups.people import gourmet_sub_categories_view
from lookups.people import gourmet_types_view
from lookups.people import health_issue_categories_view
from lookups.people import health_issue_types_view
from lookups.people import health_outfit_types_view
from lookups.people import health_prescription_drugs_view
from lookups.people import hobby_brands_view
from lookups.people import hobby_categories_view
from lookups.people import hobby_sub_categories_view
from lookups.people import hobby_types_view
from lookups.people import pet_breeds_view
from lookups.people import pet_record_types_view
from lookups.people import pet_species_view
from lookups.people import product_brands_view
from lookups.people import product_categories_view
from lookups.people import product_sub_categories_view
from lookups.people import product_types_view
from lookups.people import professional_skill_types_view
from lookups.people import sport_athlete_view
from lookups.people import sport_categories_view
from lookups.people import sport_team_view
from lookups.people import sport_types_view

from people_inventory import my_closet_view
from people_inventory import my_container_itens_view
from people_inventory import my_container_view
from people_inventory import my_garage_car_history_view
from people_inventory import my_garage_car_view
from people_inventory import my_pet_record_view
from people_inventory import my_pet_view

from people_preferences import gourmet_view
from people_preferences import hobby_view
from people_preferences import portal_view
from people_preferences import products_view
from people_preferences import shop_view
from people_preferences import sports_view

from people_profile import contact_me_view
from people_profile import documents_view
from people_profile import education_view
from people_profile import health_know_issues_view
from people_profile import health_my_body_view
from people_profile import health_prescription_view
from people_profile import my_family_view
from people_profile import my_lists_view
from people_profile import professional_history_view
from people_profile import professional_skills_view
from people_profile import profile_view
from people_profile import scorecard_view
from people_profile import social_contacts_view

from people_security import login_view

from product import product_inventory_view
from product import product_reviews_view
from product import product_view

from runenv import load_env

from sales import engine_setup_view
from sales import negotiation_history_view
from sales import sales_transactions_view

from store import store_sales_setup_view
from store import store_sales_team_apply_view
from store import store_sales_team_setup_view
from store import store_view

from system import error_codes_view

app = Flask(__name__)
CORS(app)
load_env()


@app.route(
    '/')
def index():
    # return 'Hello World!', 200
    your_value = os.environ.get('ENV')
    print(your_value)
    resp_dict = {'first_name': your_value, 'last_name': 'Mauro'}
    response = jsonify(resp_dict)
    return response


# ----------------------------------------------------------------------
# lkup_closet_cloth_categories
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-closet-cloth-categories',
    methods=['POST'])
def get_closet_cloth_categories():
    return closet_cloth_categories_view.ClosetClothCategoriesView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/lookup/people/get-closet-cloth-categories-all',
    methods=['GET'])
def get_closet_cloth_categories_all():
    return closet_cloth_categories_view.ClosetClothCategoriesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-closet-cloth-categories-id',
    methods=['POST'])
def get_closet_cloth_categories_id():
    return closet_cloth_categories_view.ClosetClothCategoriesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-closet-cloth-categories',
    methods=['POST'])
def update_closet_cloth_categories():
    return closet_cloth_categories_view.ClosetClothCategoriesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-closet-cloth-categories',
    methods=['POST'])
def insert_closet_cloth_categories():
    return closet_cloth_categories_view.ClosetClothCategoriesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-closet-cloth-categories',
    methods=['POST'])
def deactivate_closet_cloth_categories():
    return closet_cloth_categories_view.ClosetClothCategoriesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-closet-cloth-categories',
    methods=['POST'])
def activate_closet_cloth_categories():
    return closet_cloth_categories_view.ClosetClothCategoriesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-closet-cloth-categories',
    methods=['POST'])
def delete_closet_cloth_categories():
    return closet_cloth_categories_view.ClosetClothCategoriesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_closet_cloth_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-closet-cloth-types-all',
    methods=['GET'])
def get_closet_cloth_types_all():
    return closet_cloth_types_view.ClosetClothTypeView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-closet-cloth-types-id',
    methods=['POST'])
def get_closet_cloth_types_id():
    return closet_cloth_types_view.ClosetClothTypeView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-closet-cloth-types',
    methods=['POST'])
def update_closet_cloth_types():
    return closet_cloth_types_view.ClosetClothTypeView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-closet-cloth-types',
    methods=['POST'])
def insert_closet_cloth_types():
    return closet_cloth_types_view.ClosetClothTypeView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-closet-cloth-types',
    methods=['POST'])
def deactivate_closet_cloth_types():
    return closet_cloth_types_view.ClosetClothTypeView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-closet-cloth-types',
    methods=['POST'])
def activate_closet_cloth_types():
    return closet_cloth_types_view.ClosetClothTypeView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-closet-cloth-types',
    methods=['POST'])
def delete_closet_cloth_types():
    return closet_cloth_types_view.ClosetClothTypeView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_contact_address_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-contact-address-types-all',
    methods=['GET'])
def get_contact_address_types_all():
    return contact_address_types_view.ContactAddressTypesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-contact-address-types-id',
    methods=['POST'])
def get_contact_address_types_id():
    return contact_address_types_view.ContactAddressTypesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-contact-address-types',
    methods=['POST'])
def update_contact_address_types():
    return contact_address_types_view.ContactAddressTypesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-contact-address-types',
    methods=['POST'])
def insert_contact_address_types():
    return contact_address_types_view.ContactAddressTypesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-contact-address-types',
    methods=['POST'])
def deactivate_contact_address_types():
    return contact_address_types_view.ContactAddressTypesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-contact-address-types',
    methods=['POST'])
def activate_contact_address_types():
    return contact_address_types_view.ContactAddressTypesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-contact-address-types',
    methods=['POST'])
def delete_contact_address_types():
    return contact_address_types_view.ContactAddressTypesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_document_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-document-types-all',
    methods=['GET'])
def get_document_types_all():
    return document_types_view.DocumentTypesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-document-types-id',
    methods=['POST'])
def get_document_types_id():
    return document_types_view.DocumentTypesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-document-types',
    methods=['POST'])
def update_document_types():
    return document_types_view.DocumentTypesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-document-types',
    methods=['POST'])
def insert_document_types():
    return document_types_view.DocumentTypesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-document-types',
    methods=['POST'])
def deactivate_document_types():
    return document_types_view.DocumentTypesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-document-types',
    methods=['POST'])
def activate_document_types():
    return document_types_view.DocumentTypesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-document-types',
    methods=['POST'])
def delete_document_types():
    return document_types_view.DocumentTypesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_education_degree_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-education-degree-types-all',
    methods=['GET'])
def get_education_degree_types_all():
    return education_degree_types_view.EducationDegreeTypesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-education-degree-types-id',
    methods=['POST'])
def get_education_degree_types_id():
    return education_degree_types_view.EducationDegreeTypesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-education-degree-types',
    methods=['POST'])
def update_education_degree_types():
    return education_degree_types_view.EducationDegreeTypesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-education-degree-types',
    methods=['POST'])
def insert_education_degree_types():
    return education_degree_types_view.EducationDegreeTypesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-education-degree-types',
    methods=['POST'])
def deactivate_education_degree_types():
    return education_degree_types_view.EducationDegreeTypesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-education-degree-types',
    methods=['POST'])
def activate_education_degree_types():
    return education_degree_types_view.EducationDegreeTypesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-education-degree-types',
    methods=['POST'])
def delete_education_degree_types():
    return education_degree_types_view.EducationDegreeTypesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_family_relationships
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-family-relationships-all',
    methods=['GET'])
def get_family_relationships_all():
    return family_relationships_view.FamilyRelationshipsView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-family-relationships-id',
    methods=['POST'])
def get_family_relationships_id():
    return family_relationships_view.FamilyRelationshipsView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-family-relationships',
    methods=['POST'])
def update_family_relationships():
    return family_relationships_view.FamilyRelationshipsView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-family-relationships',
    methods=['POST'])
def insert_family_relationships():
    return family_relationships_view.FamilyRelationshipsView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-family-relationships',
    methods=['POST'])
def deactivate_family_relationships():
    return family_relationships_view.FamilyRelationshipsView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-family-relationships',
    methods=['POST'])
def activate_family_relationships():
    return family_relationships_view.FamilyRelationshipsView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-family-relationships',
    methods=['POST'])
def delete_family_relationships():
    return family_relationships_view.FamilyRelationshipsView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_garage_vehicle_brands
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-garage-vehicle-brands-all',
    methods=['GET'])
def get_garage_vehicle_brands_all():
    return garage_vehicle_brands_view.GarageVehicleBrandsView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-garage-vehicle-brands-id',
    methods=['POST'])
def get_garage_vehicle_brands_id():
    return garage_vehicle_brands_view.GarageVehicleBrandsView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-garage-vehicle-brands',
    methods=['POST'])
def update_garage_vehicle_brands():
    return garage_vehicle_brands_view.GarageVehicleBrandsView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-garage-vehicle-brands',
    methods=['POST'])
def insert_garage_vehicle_brands():
    return garage_vehicle_brands_view.GarageVehicleBrandsView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-garage-vehicle-brands',
    methods=['POST'])
def deactivate_garage_vehicle_brands():
    return garage_vehicle_brands_view.GarageVehicleBrandsView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-garage-vehicle-brands',
    methods=['POST'])
def activate_garage_vehicle_brands():
    return garage_vehicle_brands_view.GarageVehicleBrandsView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-garage-vehicle-brands',
    methods=['POST'])
def delete_garage_vehicle_brands():
    return garage_vehicle_brands_view.GarageVehicleBrandsView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_garage_vehicle_models
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-garage-vehicle-models',
    methods=['POST'])
def get_garage_vehicle_models():
    return garage_vehicle_models_view.GarageVehicleModelsView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/lookup/people/get-garage-vehicle-models-all',
    methods=['GET'])
def get_garage_vehicle_models_all():
    return garage_vehicle_models_view.GarageVehicleModelsView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-garage-vehicle-models-id',
    methods=['POST'])
def get_garage_vehicle_models_id():
    return garage_vehicle_models_view.GarageVehicleModelsView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-garage-vehicle-models',
    methods=['POST'])
def update_garage_vehicle_models():
    return garage_vehicle_models_view.GarageVehicleModelsView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-garage-vehicle-models',
    methods=['POST'])
def insert_garage_vehicle_models():
    return garage_vehicle_models_view.GarageVehicleModelsView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-garage-vehicle-models',
    methods=['POST'])
def deactivate_garage_vehicle_models():
    return garage_vehicle_models_view.GarageVehicleModelsView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-garage-vehicle-models',
    methods=['POST'])
def activate_garage_vehicle_models():
    return garage_vehicle_models_view.GarageVehicleModelsView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-garage-vehicle-models',
    methods=['POST'])
def delete_garage_vehicle_models():
    return garage_vehicle_models_view.GarageVehicleModelsView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_garage_vehicle_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-garage-vehicle-types-all',
    methods=['GET'])
def get_garage_vehicle_types_all():
    return garage_vehicle_types_view.GarageVehicleTypesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-garage-vehicle-types-id',
    methods=['POST'])
def get_garage_vehicle_types_id():
    return garage_vehicle_types_view.GarageVehicleTypesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-garage-vehicle-types',
    methods=['POST'])
def update_garage_vehicle_types():
    return garage_vehicle_types_view.GarageVehicleTypesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-garage-vehicle-types',
    methods=['POST'])
def insert_garage_vehicle_types():
    return garage_vehicle_types_view.GarageVehicleTypesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-garage-vehicle-types',
    methods=['POST'])
def deactivate_garage_vehicle_types():
    return garage_vehicle_types_view.GarageVehicleTypesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-garage-vehicle-types',
    methods=['POST'])
def activate_garage_vehicle_types():
    return garage_vehicle_types_view.GarageVehicleTypesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-garage-vehicle-types',
    methods=['POST'])
def delete_garage_vehicle_types():
    return garage_vehicle_types_view.GarageVehicleTypesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_gourmet_brands
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-gourmet-brands',
    methods=['POST'])
def get_gourmet_brands():
    return gourmet_brands_view.GourmetBrandsView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/lookup/people/get-gourmet-brands-all',
    methods=['GET'])
def get_gourmet_brands_all():
    return gourmet_brands_view.GourmetBrandsView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-gourmet-brands-id',
    methods=['POST'])
def get_gourmet_brands_id():
    return gourmet_brands_view.GourmetBrandsView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-gourmet-brands',
    methods=['POST'])
def update_gourmet_brands():
    return gourmet_brands_view.GourmetBrandsView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-gourmet-brands',
    methods=['POST'])
def insert_gourmet_brands():
    return gourmet_brands_view.GourmetBrandsView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-gourmet-brands',
    methods=['POST'])
def deactivate_gourmet_brands():
    return gourmet_brands_view.GourmetBrandsView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-gourmet-brands',
    methods=['POST'])
def activate_gourmet_brands():
    return gourmet_brands_view.GourmetBrandsView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-gourmet-brands',
    methods=['POST'])
def delete_gourmet_brands():
    return gourmet_brands_view.GourmetBrandsView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_gourmet_categories
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-gourmet-categories',
    methods=['POST'])
def get_gourmet_categories():
    return gourmet_categories_view.GourmetCategoriesView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/lookup/people/get-gourmet-categories-all',
    methods=['GET'])
def get_gourmet_categories_all():
    return gourmet_categories_view.GourmetCategoriesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-gourmet-categories-id',
    methods=['POST'])
def get_gourmet_categories_id():
    return gourmet_categories_view.GourmetCategoriesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-gourmet-categories',
    methods=['POST'])
def update_gourmet_categories():
    return gourmet_categories_view.GourmetCategoriesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-gourmet-categories',
    methods=['POST'])
def insert_gourmet_categories():
    return gourmet_categories_view.GourmetCategoriesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-gourmet-categories',
    methods=['POST'])
def deactivate_gourmet_categories():
    return gourmet_categories_view.GourmetCategoriesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-gourmet-categories',
    methods=['POST'])
def activate_gourmet_categories():
    return gourmet_categories_view.GourmetCategoriesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-gourmet-categories',
    methods=['POST'])
def delete_gourmet_categories():
    return gourmet_categories_view.GourmetCategoriesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_gourmet_models
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-gourmet-models',
    methods=['POST'])
def get_gourmet_models():
    return gourmet_models_view.GourmetModelsView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/lookup/people/get-gourmet-models-all',
    methods=['GET'])
def get_gourmet_models_all():
    return gourmet_models_view.GourmetModelsView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-gourmet-models-id',
    methods=['POST'])
def get_gourmet_models_id():
    return gourmet_models_view.GourmetModelsView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-gourmet-models',
    methods=['POST'])
def update_gourmet_models():
    return gourmet_models_view.GourmetModelsView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-gourmet-models',
    methods=['POST'])
def insert_gourmet_models():
    return gourmet_models_view.GourmetModelsView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-gourmet-models',
    methods=['POST'])
def deactivate_gourmet_models():
    return gourmet_models_view.GourmetModelsView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-gourmet-models',
    methods=['POST'])
def activate_gourmet_models():
    return gourmet_models_view.GourmetModelsView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-gourmet-models',
    methods=['POST'])
def delete_gourmet_models():
    return gourmet_models_view.GourmetModelsView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_gourmet_sub_categories
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-gourmet-sub-categories',
    methods=['POST'])
def get_gourmet_sub_categories():
    return gourmet_sub_categories_view.GourmetSubCategoriesView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/lookup/people/get-gourmet-sub-categories-all',
    methods=['GET'])
def get_gourmet_sub_categories_all():
    return gourmet_sub_categories_view.GourmetSubCategoriesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-gourmet-sub-categories-id',
    methods=['POST'])
def get_gourmet_sub_categories_id():
    return gourmet_sub_categories_view.GourmetSubCategoriesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-gourmet-sub-categories',
    methods=['POST'])
def update_gourmet_sub_categories():
    return gourmet_sub_categories_view.GourmetSubCategoriesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-gourmet-sub-categories',
    methods=['POST'])
def insert_gourmet_sub_categories():
    return gourmet_sub_categories_view.GourmetSubCategoriesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-gourmet-sub-categories',
    methods=['POST'])
def deactivate_gourmet_sub_categories():
    return gourmet_sub_categories_view.GourmetSubCategoriesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-gourmet-sub-categories',
    methods=['POST'])
def activate_gourmet_sub_categories():
    return gourmet_sub_categories_view.GourmetSubCategoriesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-gourmet-sub-categories',
    methods=['POST'])
def delete_gourmet_sub_categories():
    return gourmet_sub_categories_view.GourmetSubCategoriesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_gourmet_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookup/people/get-gourmet-types-all',
    methods=['GET'])
def get_gourmet_types_all():
    return gourmet_types_view.GourmetTypesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookup/people/get-gourmet-types-id',
    methods=['POST'])
def get_gourmet_types_id():
    return gourmet_types_view.GourmetTypesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookup/people/update-gourmet-types',
    methods=['POST'])
def update_gourmet_types():
    return gourmet_types_view.GourmetTypesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookup/people/insert-gourmet-types',
    methods=['POST'])
def insert_gourmet_types():
    return gourmet_types_view.GourmetTypesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookup/people/deactivate-gourmet-types',
    methods=['POST'])
def deactivate_gourmet_types():
    return gourmet_types_view.GourmetTypesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookup/people/activate-gourmet-types',
    methods=['POST'])
def activate_gourmet_types():
    return gourmet_types_view.GourmetTypesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookup/people/delete-gourmet-types',
    methods=['POST'])
def delete_gourmet_types():
    return gourmet_types_view.GourmetTypesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_health_issue_categories
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-health-issues-categories',
    methods=['POST'])
def get_health_issue_categories():
    return health_issue_categories_view.HealthIssueCategoriesView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-health-issues-categories-all',
    methods=['GET'])
def get_health_issue_categories_all():
    return health_issue_categories_view.HealthIssueCategoriesView()\
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-health-issues-categories-id',
    methods=['POST'])
def get_health_issue_categories_id():
    return health_issue_categories_view.HealthIssueCategoriesView()\
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-health-issues-categories',
    methods=['POST'])
def update_health_issue_categories():
    return health_issue_categories_view.HealthIssueCategoriesView()\
        .update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-health-issues-categories',
    methods=['POST'])
def insert_health_issue_categories():
    return health_issue_categories_view.HealthIssueCategoriesView()\
        .insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-health-issues-categories',
    methods=['POST'])
def deactivate_health_issue_categories():
    return health_issue_categories_view.HealthIssueCategoriesView()\
        .deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-health-issues-categories',
    methods=['POST'])
def activate_health_issue_categories():
    return health_issue_categories_view.HealthIssueCategoriesView()\
        .activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-health-issues-categories',
    methods=['POST'])
def delete_health_issue_categories():
    return health_issue_categories_view.HealthIssueCategoriesView()\
        .delete(request)


# ----------------------------------------------------------------------
# lkup_health_issue_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-health-issue-types-all',
    methods=['GET'])
def get_health_issue_types_all():
    return health_issue_types_view.HealthIssueTypesView()\
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-health-issue-types-id',
    methods=['POST'])
def get_health_issue_types_id():
    return health_issue_types_view.HealthIssueTypesView()\
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-health-issue-types',
    methods=['POST'])
def update_health_issue_types():
    return health_issue_types_view.HealthIssueTypesView()\
        .update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-health-issue-types',
    methods=['POST'])
def insert_health_issue_types():
    return health_issue_types_view.HealthIssueTypesView()\
        .insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-health-issue-types',
    methods=['POST'])
def deactivate_health_issue_types():
    return health_issue_types_view.HealthIssueTypesView()\
        .deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-health-issue-types',
    methods=['POST'])
def activate_health_issue_types():
    return health_issue_types_view.HealthIssueTypesView()\
        .activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-health-issue-types',
    methods=['POST'])
def delete_health_issue_types():
    return health_issue_types_view.HealthIssueTypesView()\
        .delete(request)


# ----------------------------------------------------------------------
# lkup_health_outfit_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-health-outfit-types-all',
    methods=['GET'])
def get_health_outfit_types_all():
    return health_outfit_types_view.HealthOutfitTypesView()\
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-health-outfit-types-id',
    methods=['POST'])
def get_health_outfit_types_id():
    return health_outfit_types_view.HealthOutfitTypesView()\
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-health-outfit-types',
    methods=['POST'])
def update_health_outfit_types():
    return health_outfit_types_view.HealthOutfitTypesView()\
        .update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-health-outfit-types',
    methods=['POST'])
def insert_health_outfit_types():
    return health_outfit_types_view.HealthOutfitTypesView()\
        .insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-health-outfit-types',
    methods=['POST'])
def deactivate_health_outfit_types():
    return health_outfit_types_view.HealthOutfitTypesView()\
        .deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-health-outfit-types',
    methods=['POST'])
def activate_health_outfit_types():
    return health_outfit_types_view.HealthOutfitTypesView()\
        .activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-health-outfit-types',
    methods=['POST'])
def delete_health_outfit_types():
    return health_outfit_types_view.HealthOutfitTypesView()\
        .delete(request)


# ----------------------------------------------------------------------
# lkup_health_prescription_drugs
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-health-prescription-drugs-all',
    methods=['GET'])
def get_health_prescription_drugs_all():
    return health_prescription_drugs_view.HealthPrescriptionDrugsView()\
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-health-prescription-drugs-id',
    methods=['POST'])
def get_health_prescription_drugs_id():
    return health_prescription_drugs_view.HealthPrescriptionDrugsView()\
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-health-prescription-drugs',
    methods=['POST'])
def update_health_prescription_drugs():
    return health_prescription_drugs_view.HealthPrescriptionDrugsView()\
        .update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-health-prescription-drugs',
    methods=['POST'])
def insert_health_prescription_drugs():
    return health_prescription_drugs_view.HealthPrescriptionDrugsView()\
        .insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-health-prescription-drugs',
    methods=['POST'])
def deactivate_health_prescription_drugs():
    return health_prescription_drugs_view.HealthPrescriptionDrugsView()\
        .deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-health-prescription-drugs',
    methods=['POST'])
def activate_health_prescription_drugs():
    return health_prescription_drugs_view.HealthPrescriptionDrugsView()\
        .activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-health-prescription-drugs',
    methods=['POST'])
def delete_health_prescription_drugs():
    return health_prescription_drugs_view.HealthPrescriptionDrugsView()\
        .delete(request)


# ----------------------------------------------------------------------
# lkup_hobby_brands
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-hobby-brands',
    methods=['POST'])
def get_hobby_brands():
    return hobby_brands_view.HobbyBrandsView().retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-hobby-brands-all',
    methods=['GET'])
def get_hobby_brands_all():
    return hobby_brands_view.HobbyBrandsView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-hobby-brands-id',
    methods=['POST'])
def get_hobby_brands_id():
    return hobby_brands_view.HobbyBrandsView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-hobby-brands',
    methods=['POST'])
def update_hobby_brands():
    return hobby_brands_view.HobbyBrandsView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-hobby-brands',
    methods=['POST'])
def insert_hobby_brands():
    return hobby_brands_view.HobbyBrandsView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-hobby-brands',
    methods=['POST'])
def deactivate_hobby_brands():
    return hobby_brands_view.HobbyBrandsView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-hobby-brands',
    methods=['POST'])
def activate_hobby_brands():
    return hobby_brands_view.HobbyBrandsView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-hobby-brands',
    methods=['POST'])
def delete_hobby_brands():
    return hobby_brands_view.HobbyBrandsView().delete(request)


# ----------------------------------------------------------------------
# lkup_hobby_categories
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-hobby-categories',
    methods=['POST'])
def get_hobby_categories():
    return hobby_categories_view.HobbyCategoriesView().retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-hobby-categories-all',
    methods=['GET'])
def get_hobby_categories_all():
    return hobby_categories_view.HobbyCategoriesView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-hobby-categories-id',
    methods=['POST'])
def get_hobby_categories_id():
    return hobby_categories_view.HobbyCategoriesView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-hobby-categories',
    methods=['POST'])
def update_hobby_categories():
    return hobby_categories_view.HobbyCategoriesView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-hobby-categories',
    methods=['POST'])
def insert_hobby_categories():
    return hobby_categories_view.HobbyCategoriesView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-hobby-categories',
    methods=['POST'])
def deactivate_hobby_categories():
    return hobby_categories_view.HobbyCategoriesView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-hobby-categories',
    methods=['POST'])
def activate_hobby_categories():
    return hobby_categories_view.HobbyCategoriesView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-hobby-categories',
    methods=['POST'])
def delete_hobby_categories():
    return hobby_categories_view.HobbyCategoriesView().delete(request)


# ----------------------------------------------------------------------
# lkup_hobby_sub_categories
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-hobby-sub-categories',
    methods=['POST'])
def get_hobby_sub_categories():
    return hobby_sub_categories_view.HobbySubCategoriesView().retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-hobby-sub-categories-all',
    methods=['GET'])
def get_hobby_sub_categories_all():
    return hobby_sub_categories_view.HobbySubCategoriesView()\
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-hobby-sub-categories-id',
    methods=['POST'])
def get_hobby_sub_categories_id():
    return hobby_sub_categories_view.HobbySubCategoriesView()\
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-hobby-sub-categories',
    methods=['POST'])
def update_hobby_sub_categories():
    return hobby_sub_categories_view.HobbySubCategoriesView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-hobby-sub-categories',
    methods=['POST'])
def insert_hobby_sub_categories():
    return hobby_sub_categories_view.HobbySubCategoriesView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-hobby-sub-categories',
    methods=['POST'])
def deactivate_hobby_sub_categories():
    return hobby_sub_categories_view.HobbySubCategoriesView()\
        .deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-hobby-sub-categories',
    methods=['POST'])
def activate_hobby_sub_categories():
    return hobby_sub_categories_view.HobbySubCategoriesView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-hobby-sub-categories',
    methods=['POST'])
def delete_hobby_sub_categories():
    return hobby_sub_categories_view.HobbySubCategoriesView().delete(request)


# ----------------------------------------------------------------------
# lkup_hobby_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-hobby-types-all',
    methods=['GET'])
def get_hobby_types_all():
    return hobby_types_view.HobbyTypesView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-hobby-types-id',
    methods=['POST'])
def get_hobby_types_id():
    return hobby_types_view.HobbyTypesView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-hobby-types',
    methods=['POST'])
def update_hobby_types():
    return hobby_types_view.HobbyTypesView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-hobby-types',
    methods=['POST'])
def insert_hobby_types():
    return hobby_types_view.HobbyTypesView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-hobby-types',
    methods=['POST'])
def deactivate_hobby_types():
    return hobby_types_view.HobbyTypesView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-hobby-types',
    methods=['POST'])
def activate_hobby_types():
    return hobby_types_view.HobbyTypesView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-hobby-types',
    methods=['POST'])
def delete_hobby_types():
    return hobby_types_view.HobbyTypesView().delete(request)


# ----------------------------------------------------------------------
# lkup_pet_breeds
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-pet-breeds-all',
    methods=['GET'])
def get_pet_breeds_all():
    return pet_breeds_view.PetBreedsView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-pet-breeds-id',
    methods=['POST'])
def get_pet_breeds_id():
    return pet_breeds_view.PetBreedsView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-pet-breeds',
    methods=['POST'])
def update_pet_breeds():
    return pet_breeds_view.PetBreedsView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-pet-breeds',
    methods=['POST'])
def insert_pet_breeds():
    return pet_breeds_view.PetBreedsView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-pet-breeds',
    methods=['POST'])
def deactivate_pet_breeds():
    return pet_breeds_view.PetBreedsView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-pet-breeds',
    methods=['POST'])
def activate_pet_breeds():
    return pet_breeds_view.PetBreedsView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-pet-breeds',
    methods=['POST'])
def delete_pet_breeds():
    return pet_breeds_view.PetBreedsView().delete(request)


# ----------------------------------------------------------------------
# lkup_pet_record_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-pet-record-types-all',
    methods=['GET'])
def get_pet_record_types_all():
    return pet_record_types_view.PetRecordTypesView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-pet-record-types-id',
    methods=['POST'])
def get_pet_record_types_id():
    return pet_record_types_view.PetRecordTypesView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-pet-record-types',
    methods=['POST'])
def update_pet_record_types():
    return pet_record_types_view.PetRecordTypesView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-pet-record-types',
    methods=['POST'])
def insert_pet_record_types():
    return pet_record_types_view.PetRecordTypesView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-pet-record-types',
    methods=['POST'])
def deactivate_pet_record_types():
    return pet_record_types_view.PetRecordTypesView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-pet-record-types',
    methods=['POST'])
def activate_pet_record_types():
    return pet_record_types_view.PetRecordTypesView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-pet-record-types',
    methods=['POST'])
def delete_pet_record_types():
    return pet_record_types_view.PetRecordTypesView().delete(request)


# ----------------------------------------------------------------------
# lkup_pet_species
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-pet-species',
    methods=['POST'])
def get_pet_species():
    return pet_species_view.PetSpeciesView().retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-pet-species-all',
    methods=['GET'])
def get_pet_species_all():
    return pet_species_view.PetSpeciesView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-pet-species-id',
    methods=['POST'])
def get_pet_species_id():
    return pet_species_view.PetSpeciesView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-pet-species',
    methods=['POST'])
def update_pet_species():
    return pet_species_view.PetSpeciesView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-pet-species',
    methods=['POST'])
def insert_pet_species():
    return pet_species_view.PetSpeciesView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-pet-species',
    methods=['POST'])
def deactivate_pet_species():
    return pet_species_view.PetSpeciesView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-pet-species',
    methods=['POST'])
def activate_pet_species():
    return pet_species_view.PetSpeciesView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-pet-species',
    methods=['POST'])
def delete_pet_species():
    return pet_species_view.PetSpeciesView().delete(request)


# ----------------------------------------------------------------------
# lkup_product_brands
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-product-brands-all',
    methods=['GET'])
def get_product_brands_all():
    return product_brands_view.ProductBrandsView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-product-brands-id',
    methods=['POST'])
def get_product_brands_id():
    return product_brands_view.ProductBrandsView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-product-brands',
    methods=['POST'])
def update_product_brands():
    return product_brands_view.ProductBrandsView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-product-brands',
    methods=['POST'])
def insert_product_brands():
    return product_brands_view.ProductBrandsView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-product-brands',
    methods=['POST'])
def deactivate_product_brands():
    return product_brands_view.ProductBrandsView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-product-brands',
    methods=['POST'])
def activate_product_brands():
    return product_brands_view.ProductBrandsView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-product-brands',
    methods=['POST'])
def delete_product_brands():
    return product_brands_view.ProductBrandsView().delete(request)


# ----------------------------------------------------------------------
# lkup_product_categories
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-product-categories',
    methods=['POST'])
def get_product_categories():
    return product_categories_view.ProductCategoriesView().retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-product-categories-all',
    methods=['GET'])
def get_product_categories_all():
    return product_categories_view.ProductCategoriesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-product-categories-id',
    methods=['POST'])
def get_product_categories_id():
    return product_categories_view.ProductCategoriesView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-product-categories',
    methods=['POST'])
def update_product_categories():
    return product_categories_view.ProductCategoriesView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-product-categories',
    methods=['POST'])
def insert_product_categories():
    return product_categories_view.ProductCategoriesView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-product-categories',
    methods=['POST'])
def deactivate_product_categories():
    return product_categories_view.ProductCategoriesView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-product-categories',
    methods=['POST'])
def activate_product_categories():
    return product_categories_view.ProductCategoriesView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-product-categories',
    methods=['POST'])
def delete_product_categories():
    return product_categories_view.ProductCategoriesView().delete(request)


# ----------------------------------------------------------------------
# lkup_product_sub_categories
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-product-sub-categories',
    methods=['POST'])
def get_product_sub_categories():
    return product_sub_categories_view.ProductSubCategoriesView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-product-sub-categories-all',
    methods=['GET'])
def get_product_sub_categories_all():
    return product_sub_categories_view.ProductSubCategoriesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-product-sub-categories-id',
    methods=['POST'])
def get_product_sub_categories_id():
    return product_sub_categories_view.ProductSubCategoriesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-product-sub-categories',
    methods=['POST'])
def update_product_sub_categories():
    return product_sub_categories_view.ProductSubCategoriesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-product-sub-categories',
    methods=['POST'])
def insert_product_sub_categories():
    return product_sub_categories_view.ProductSubCategoriesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-product-sub-categories',
    methods=['POST'])
def deactivate_product_sub_categories():
    return product_sub_categories_view.ProductSubCategoriesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-product-sub-categories',
    methods=['POST'])
def activate_product_sub_categories():
    return product_sub_categories_view.ProductSubCategoriesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-product-sub-categories',
    methods=['POST'])
def delete_product_sub_categories():
    return product_sub_categories_view.ProductSubCategoriesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_product_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-product-types-all',
    methods=['GET'])
def get_product_types_all():
    return product_types_view.ProductTypesView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-product-types-id',
    methods=['POST'])
def get_product_types_id():
    return product_types_view.ProductTypesView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-product-types',
    methods=['POST'])
def update_product_types():
    return product_types_view.ProductTypesView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-product-types',
    methods=['POST'])
def insert_product_types():
    return product_types_view.ProductTypesView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-product-types',
    methods=['POST'])
def deactivate_product_types():
    return product_types_view.ProductTypesView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-product-types',
    methods=['POST'])
def activate_product_types():
    return product_types_view.ProductTypesView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-product-types',
    methods=['POST'])
def delete_product_types():
    return product_types_view.ProductTypesView().delete(request)


# ----------------------------------------------------------------------
# lkup_professional_skill_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-professional-skill-types-all',
    methods=['GET'])
def get_professional_skill_types_all():
    return professional_skill_types_view.ProfessionalSkillTypesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-professional-skill-types-id',
    methods=['POST'])
def get_professional_skill_types_id():
    return professional_skill_types_view.ProfessionalSkillTypesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-professional-skill-types',
    methods=['POST'])
def update_professional_skill_types():
    return professional_skill_types_view.ProfessionalSkillTypesView() \
        .update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-professional-skill-types',
    methods=['POST'])
def insert_professional_skill_types():
    return professional_skill_types_view.ProfessionalSkillTypesView() \
        .insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-professional-skill-types',
    methods=['POST'])
def deactivate_professional_skill_types():
    return professional_skill_types_view.ProfessionalSkillTypesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-professional-skill-types',
    methods=['POST'])
def activate_professional_skill_types():
    return professional_skill_types_view.ProfessionalSkillTypesView() \
        .activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-professional-skill-types',
    methods=['POST'])
def delete_professional_skill_types():
    return professional_skill_types_view.ProfessionalSkillTypesView() \
        .delete(request)


# ----------------------------------------------------------------------
# lkup_sport_athlete
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-sport-athlete',
    methods=['POST'])
def get_sport_athlete():
    return sport_athlete_view.SportAthleteView().retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-sport-athlete-all',
    methods=['GET'])
def get_sport_athlete_all():
    return sport_athlete_view.SportAthleteView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-sport-athlete-id',
    methods=['POST'])
def get_sport_athlete_id():
    return sport_athlete_view.SportAthleteView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-sport-athlete',
    methods=['POST'])
def update_sport_athlete():
    return sport_athlete_view.SportAthleteView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-sport-athlete',
    methods=['POST'])
def insert_sport_athlete():
    return sport_athlete_view.SportAthleteView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-sport-athlete',
    methods=['POST'])
def deactivate_sport_athlete():
    return sport_athlete_view.SportAthleteView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-sport-athlete',
    methods=['POST'])
def activate_sport_athlete():
    return sport_athlete_view.SportAthleteView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-sport-athlete',
    methods=['POST'])
def delete_sport_athlete():
    return sport_athlete_view.SportAthleteView().delete(request)


# ----------------------------------------------------------------------
# lkup_sport_categories
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-sport-categories',
    methods=['POST'])
def get_sport_categories():
    return sport_categories_view.SportCategoriesView().retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-sport-categories-all',
    methods=['GET'])
def get_sport_categories_all():
    return sport_categories_view.SportCategoriesView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-sport-categories-id',
    methods=['POST'])
def get_sport_categories_id():
    return sport_categories_view.SportCategoriesView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-sport-categories',
    methods=['POST'])
def update_sport_categories():
    return sport_categories_view.SportCategoriesView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-sport-categories',
    methods=['POST'])
def insert_sport_categories():
    return sport_categories_view.SportCategoriesView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-sport-categories',
    methods=['POST'])
def deactivate_sport_categories():
    return sport_categories_view.SportCategoriesView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-sport-categories',
    methods=['POST'])
def activate_sport_categories():
    return sport_categories_view.SportCategoriesView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-sport-categories',
    methods=['POST'])
def delete_sport_categories():
    return sport_categories_view.SportCategoriesView().delete(request)


# ----------------------------------------------------------------------
# lkup_sport_team
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-sport-team',
    methods=['POST'])
def get_sport_team():
    return sport_team_view.SportTeamView().retrieve(request)


@app.route(
    '/api/v1.0/lookups/people/get-sport-team-all',
    methods=['GET'])
def get_sport_team_all():
    return sport_team_view.SportTeamView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-sport-team-id',
    methods=['POST'])
def get_sport_team_id():
    return sport_team_view.SportTeamView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-sport-team',
    methods=['POST'])
def update_sport_team():
    return sport_team_view.SportTeamView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-sport-team',
    methods=['POST'])
def insert_sport_team():
    return sport_team_view.SportTeamView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-sport-team',
    methods=['POST'])
def deactivate_sport_team():
    return sport_team_view.SportTeamView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-sport-team',
    methods=['POST'])
def activate_sport_team():
    return sport_team_view.SportTeamView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-sport-team',
    methods=['POST'])
def delete_sport_team():
    return sport_team_view.SportTeamView().delete(request)


# ----------------------------------------------------------------------
# lkup_sport_types
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/lookups/people/get-sport-types-all',
    methods=['GET'])
def get_sport_types_all():
    return sport_types_view.SportTypesView().retrieve_all(request)


@app.route(
    '/api/v1.0/lookups/people/get-sport-types-id',
    methods=['POST'])
def get_sport_types_id():
    return sport_types_view.SportTypesView().retrieve_id(request)


@app.route(
    '/api/v1.0/lookups/people/update-sport-types',
    methods=['POST'])
def update_sport_types():
    return sport_types_view.SportTypesView().update(request)


@app.route(
    '/api/v1.0/lookups/people/insert-sport-types',
    methods=['POST'])
def insert_sport_types():
    return sport_types_view.SportTypesView().insert(request)


@app.route(
    '/api/v1.0/lookups/people/deactivate-sport-types',
    methods=['POST'])
def deactivate_sport_types():
    return sport_types_view.SportTypesView().deactivate(request)


@app.route(
    '/api/v1.0/lookups/people/activate-sport-types',
    methods=['POST'])
def activate_sport_types():
    return sport_types_view.SportTypesView().activate(request)


@app.route(
    '/api/v1.0/lookups/people/delete-sport-types',
    methods=['POST'])
def delete_sport_types():
    return sport_types_view.SportTypesView().delete(request)


# ----------------------------------------------------------------------
# myid_people_inventory_my_closet
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/inventory/get-my-closet-hash',
    methods=['POST'])
def get_my_closet_hash():
    return my_closet_view.MyClosetView().retrieve(request)


@app.route(
    '/api/v1.0/people/inventory/get-my-closet-id',
    methods=['POST'])
def get_my_closet_id():
    return my_closet_view.MyClosetView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/inventory/update-my-closet',
    methods=['POST'])
def update_my_closet():
    return my_closet_view.MyClosetView().update(request)


@app.route(
    '/api/v1.0/people/inventory/insert-my-closet',
    methods=['POST'])
def insert_my_closet():
    return my_closet_view.MyClosetView().insert(request)


@app.route(
    '/api/v1.0/people/inventory/deactivate-my-closet',
    methods=['POST'])
def deactivate_my_closet():
    return my_closet_view.MyClosetView().deactivate(request)


@app.route(
    '/api/v1.0/people/inventory/activate-my-closet',
    methods=['POST'])
def activate_my_closet():
    return my_closet_view.MyClosetView().activate(request)


@app.route(
    '/api/v1.0/people/inventory/delete-my-closet',
    methods=['POST'])
def delete_my_closet():
    return my_closet_view.MyClosetView().delete(request)


# ----------------------------------------------------------------------
# myid_people_inventory_my_container_itens
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/inventory/get-my-container-itens-hash',
    methods=['POST'])
def get_my_container_hash_itens():
    return my_container_itens_view.MyContainerItensView().retrieve(request)


@app.route(
    '/api/v1.0/people/inventory/get-my-container-itens-id',
    methods=['POST'])
def get_my_container_id_itens():
    return my_container_itens_view.MyContainerItensView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/inventory/update-my-container-itens',
    methods=['POST'])
def update_my_container_itens():
    return my_container_itens_view.MyContainerItensView().update(request)


@app.route(
    '/api/v1.0/people/inventory/insert-my-container-itens',
    methods=['POST'])
def insert_my_container_itens():
    return my_container_itens_view.MyContainerItensView().insert(request)


@app.route(
    '/api/v1.0/people/inventory/deactivate-my-container-itens',
    methods=['POST'])
def deactivate_my_container_itens():
    return my_container_itens_view.MyContainerItensView().deactivate(request)


@app.route(
    '/api/v1.0/people/inventory/activate-my-container-itens',
    methods=['POST'])
def activate_my_container_itens():
    return my_container_itens_view.MyContainerItensView().activate(request)


@app.route(
    '/api/v1.0/people/inventory/delete-my-container-itens',
    methods=['POST'])
def delete_my_container_itens():
    return my_container_itens_view.MyContainerItensView().delete(request)


# ----------------------------------------------------------------------
# myid_people_inventory_my_container
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/inventory/get-my-container-hash',
    methods=['POST'])
def get_my_container_hash():
    return my_container_view.MyContainerView().retrieve(request)


@app.route(
    '/api/v1.0/people/inventory/get-my-container-id',
    methods=['POST'])
def get_my_container_id():
    return my_container_view.MyContainerView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/inventory/update-my-container',
    methods=['POST'])
def update_my_container():
    return my_container_view.MyContainerView().update(request)


@app.route(
    '/api/v1.0/people/inventory/insert-my-container',
    methods=['POST'])
def insert_my_container():
    return my_container_view.MyContainerView().insert(request)


@app.route(
    '/api/v1.0/people/inventory/deactivate-my-container',
    methods=['POST'])
def deactivate_my_container():
    return my_container_view.MyContainerView().deactivate(request)


@app.route(
    '/api/v1.0/people/inventory/activate-my-container',
    methods=['POST'])
def activate_my_container():
    return my_container_view.MyContainerView().activate(request)


@app.route(
    '/api/v1.0/people/inventory/delete-my-container',
    methods=['POST'])
def delete_my_container():
    return my_container_view.MyContainerView().delete(request)


# ----------------------------------------------------------------------
# myid_people_inventory_my_garage_car_history
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/inventory/get-my-garage-car-history-hash',
    methods=['POST'])
def get_my_garage_car_history_hash():
    return my_garage_car_history_view.MyGarageCarHistoryView().retrieve(
        request)


@app.route(
    '/api/v1.0/people/inventory/get-my-garage-car-history-id',
    methods=['POST'])
def get_my_garage_car_history_id():
    return my_garage_car_history_view.MyGarageCarHistoryView().retrieve_id(
        request)


@app.route(
    '/api/v1.0/people/inventory/update-my-garage-car-history',
    methods=['POST'])
def update_my_garage_car_history():
    return my_garage_car_history_view.MyGarageCarHistoryView().update(request)


@app.route(
    '/api/v1.0/people/inventory/insert-my-garage-car-history',
    methods=['POST'])
def insert_my_garage_car_history():
    return my_garage_car_history_view.MyGarageCarHistoryView().insert(request)


@app.route(
    '/api/v1.0/people/inventory/deactivate-my-garage-car-history',
    methods=['POST'])
def deactivate_my_garage_car_history():
    return my_garage_car_history_view.MyGarageCarHistoryView().deactivate(
        request)


@app.route(
    '/api/v1.0/people/inventory/activate-my-garage-car-history',
    methods=['POST'])
def activate_my_garage_car_history():
    return my_garage_car_history_view.MyGarageCarHistoryView().activate(
        request)


@app.route(
    '/api/v1.0/people/inventory/delete-my-garage-car-history',
    methods=['POST'])
def delete_my_garage_car_history():
    return my_garage_car_history_view.MyGarageCarHistoryView().delete(request)


# ----------------------------------------------------------------------
# myid_people_inventory_my_garage_car
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/inventory/get-my-garage-car-hash',
    methods=['POST'])
def get_my_garage_car_hash():
    return my_garage_car_view.MyGarageCarView().retrieve(request)


@app.route(
    '/api/v1.0/people/inventory/get-my-garage-car-id',
    methods=['POST'])
def get_my_garage_car_id():
    return my_garage_car_view.MyGarageCarView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/inventory/update-my-garage-car',
    methods=['POST'])
def update_my_garage_car():
    return my_garage_car_view.MyGarageCarView().update(request)


@app.route(
    '/api/v1.0/people/inventory/insert-my-garage-car',
    methods=['POST'])
def insert_my_garage_car():
    return my_garage_car_view.MyGarageCarView().insert(request)


@app.route(
    '/api/v1.0/people/inventory/deactivate-my-garage-car',
    methods=['POST'])
def deactivate_my_garage_car():
    return my_garage_car_view.MyGarageCarView().deactivate(request)


@app.route(
    '/api/v1.0/people/inventory/activate-my-garage-car',
    methods=['POST'])
def activate_my_garage_car():
    return my_garage_car_view.MyGarageCarView().activate(request)


@app.route(
    '/api/v1.0/people/inventory/delete-my-garage-car',
    methods=['POST'])
def delete_my_garage_car():
    return my_garage_car_view.MyGarageCarView().delete(request)


# ----------------------------------------------------------------------
# myid_people_inventory_my_pet
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/inventory/get-my-pet-hash',
    methods=['POST'])
def get_my_pet_hash():
    return my_pet_view.MyPetView().retrieve(request)


@app.route(
    '/api/v1.0/people/inventory/get-my-pet-id',
    methods=['POST'])
def get_my_pet_id():
    return my_pet_view.MyPetView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/inventory/update-my-pet',
    methods=['POST'])
def update_my_pet():
    return my_pet_view.MyPetView().update(request)


@app.route(
    '/api/v1.0/people/inventory/insert-my-pet',
    methods=['POST'])
def insert_my_pet():
    return my_pet_view.MyPetView().insert(request)


@app.route(
    '/api/v1.0/people/inventory/deactivate-my-pet',
    methods=['POST'])
def deactivate_my_pet():
    return my_pet_view.MyPetView().deactivate(request)


@app.route(
    '/api/v1.0/people/inventory/activate-my-pet',
    methods=['POST'])
def activate_my_pet():
    return my_pet_view.MyPetView().activate(request)


@app.route(
    '/api/v1.0/people/inventory/delete-my-pet',
    methods=['POST'])
def delete_my_pet():
    return my_pet_view.MyPetView().delete(request)


# ----------------------------------------------------------------------
# myid_people_inventory_my_pet_record
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/inventory/get-my-pet-record-hash',
    methods=['POST'])
def get_my_pet_record_hash():
    return my_pet_record_view.MyPetRecordView().retrieve(request)


@app.route(
    '/api/v1.0/people/inventory/get-my-pet-record-id',
    methods=['POST'])
def get_my_pet_record_id():
    return my_pet_record_view.MyPetRecordView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/inventory/update-my-pet-record',
    methods=['POST'])
def update_my_pet_record():
    return my_pet_record_view.MyPetRecordView().update(request)


@app.route(
    '/api/v1.0/people/inventory/insert-my-pet-record',
    methods=['POST'])
def insert_my_pet_record():
    return my_pet_record_view.MyPetRecordView().insert(request)


@app.route(
    '/api/v1.0/people/inventory/deactivate-my-pet-record',
    methods=['POST'])
def deactivate_my_pet_record():
    return my_pet_record_view.MyPetRecordView().deactivate(request)


@app.route(
    '/api/v1.0/people/inventory/activate-my-pet-record',
    methods=['POST'])
def activate_my_pet_record():
    return my_pet_record_view.MyPetRecordView().activate(request)


@app.route(
    '/api/v1.0/people/inventory/delete-my-pet-record',
    methods=['POST'])
def delete_my_pet_record():
    return my_pet_record_view.MyPetRecordView().delete(request)


# ----------------------------------------------------------------------
# myid_people_preferences_gourmet
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/preferences/get-gourmet-hash',
    methods=['POST'])
def get_gourmet_hash():
    return gourmet_view.GourmetView().retrieve(request)


@app.route(
    '/api/v1.0/people/preferences/get-gourmet-id',
    methods=['POST'])
def get_gourmet_id():
    return gourmet_view.GourmetView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/preferences/update-gourmet',
    methods=['POST'])
def update_gourmet():
    return gourmet_view.GourmetView().update(request)


@app.route(
    '/api/v1.0/people/preferences/insert-gourmet',
    methods=['POST'])
def insert_gourmet():
    return gourmet_view.GourmetView().insert(request)


@app.route(
    '/api/v1.0/people/preferences/deactivate-gourmet',
    methods=['POST'])
def deactivate_gourmet():
    return gourmet_view.GourmetView().deactivate(request)


@app.route(
    '/api/v1.0/people/preferences/activate-gourmet',
    methods=['POST'])
def activate_gourmet():
    return gourmet_view.GourmetView().activate(request)


@app.route(
    '/api/v1.0/people/preferences/delete-gourmet',
    methods=['POST'])
def delete_gourmet():
    return gourmet_view.GourmetView().delete(request)


# ----------------------------------------------------------------------
# myid_people_preferences_hobby
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/preferences/get-hobby-hash',
    methods=['POST'])
def get_hobby_hash():
    return hobby_view.HobbyView().retrieve(request)


@app.route(
    '/api/v1.0/people/preferences/get-hobby-id',
    methods=['POST'])
def get_hobby_id():
    return hobby_view.HobbyView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/preferences/update-hobby',
    methods=['POST'])
def update_hobby():
    return hobby_view.HobbyView().update(request)


@app.route(
    '/api/v1.0/people/preferences/insert-hobby',
    methods=['POST'])
def insert_hobby():
    return hobby_view.HobbyView().insert(request)


@app.route(
    '/api/v1.0/people/preferences/deactivate-hobby',
    methods=['POST'])
def deactivate_hobby():
    return hobby_view.HobbyView().deactivate(request)


@app.route(
    '/api/v1.0/people/preferences/activate-hobby',
    methods=['POST'])
def activate_hobby():
    return hobby_view.HobbyView().activate(request)


@app.route(
    '/api/v1.0/people/preferences/delete-hobby',
    methods=['POST'])
def delete_hobby():
    return hobby_view.HobbyView().delete(request)


# ----------------------------------------------------------------------
# myid_people_preferences_portal
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/preferences/get-portal-hash',
    methods=['POST'])
def get_portal_hash():
    return portal_view.PortalView().retrieve(request)


@app.route(
    '/api/v1.0/people/preferences/get-portal-id',
    methods=['POST'])
def get_portal_id():
    return portal_view.PortalView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/preferences/update-portal',
    methods=['POST'])
def update_portal():
    return portal_view.PortalView().update(request)


@app.route(
    '/api/v1.0/people/preferences/insert-portal',
    methods=['POST'])
def insert_portal():
    return portal_view.PortalView().insert(request)


@app.route(
    '/api/v1.0/people/preferences/deactivate-portal',
    methods=['POST'])
def deactivate_portal():
    return portal_view.PortalView().deactivate(request)


@app.route(
    '/api/v1.0/people/preferences/activate-portal',
    methods=['POST'])
def activate_portal():
    return portal_view.PortalView().activate(request)


@app.route(
    '/api/v1.0/people/preferences/delete-portal',
    methods=['POST'])
def delete_portal():
    return portal_view.PortalView().delete(request)


# ----------------------------------------------------------------------
# myid_people_preferences_products
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/preferences/get-products-hash',
    methods=['POST'])
def get_products_hash():
    return products_view.ProductsView().retrieve(request)


@app.route(
    '/api/v1.0/people/preferences/get-products-id',
    methods=['POST'])
def get_products_id():
    return products_view.ProductsView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/preferences/update-products',
    methods=['POST'])
def update_products():
    return products_view.ProductsView().update(request)


@app.route(
    '/api/v1.0/people/preferences/insert-products',
    methods=['POST'])
def insert_products():
    return products_view.ProductsView().insert(request)


@app.route(
    '/api/v1.0/people/preferences/deactivate-products',
    methods=['POST'])
def deactivate_products():
    return products_view.ProductsView().deactivate(request)


@app.route(
    '/api/v1.0/people/preferences/activate-products',
    methods=['POST'])
def activate_products():
    return products_view.ProductsView().activate(request)


@app.route(
    '/api/v1.0/people/preferences/delete-products',
    methods=['POST'])
def delete_products():
    return products_view.ProductsView().delete(request)


# ----------------------------------------------------------------------
# myid_people_preferences_shop
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/preferences/get-shop-hash',
    methods=['POST'])
def get_shop_hash():
    return shop_view.ShopView().retrieve(request)


@app.route(
    '/api/v1.0/people/preferences/get-shop-id',
    methods=['POST'])
def get_shop_id():
    return shop_view.ShopView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/preferences/update-shop',
    methods=['POST'])
def update_shop():
    return shop_view.ShopView().update(request)


@app.route(
    '/api/v1.0/people/preferences/insert-shop',
    methods=['POST'])
def insert_shop():
    return shop_view.ShopView().insert(request)


@app.route(
    '/api/v1.0/people/preferences/deactivate-shop',
    methods=['POST'])
def deactivate_shop():
    return shop_view.ShopView().deactivate(request)


@app.route(
    '/api/v1.0/people/preferences/activate-shop',
    methods=['POST'])
def activate_shop():
    return shop_view.ShopView().activate(request)


@app.route(
    '/api/v1.0/people/preferences/delete-shop',
    methods=['POST'])
def delete_shop():
    return shop_view.ShopView().delete(request)


# ----------------------------------------------------------------------
# myid_people_preferences_sports
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/preferences/get-sports-hash',
    methods=['POST'])
def get_sports_hash():
    return sports_view.SportsView().retrieve(request)


@app.route(
    '/api/v1.0/people/preferences/get-sports-id',
    methods=['POST'])
def get_sports_id():
    return sports_view.SportsView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/preferences/update-sports',
    methods=['POST'])
def update_sports():
    return sports_view.SportsView().update(request)


@app.route(
    '/api/v1.0/people/preferences/insert-sports',
    methods=['POST'])
def insert_sports():
    return sports_view.SportsView().insert(request)


@app.route(
    '/api/v1.0/people/preferences/deactivate-sports',
    methods=['POST'])
def deactivate_sports():
    return sports_view.SportsView().deactivate(request)


@app.route(
    '/api/v1.0/people/preferences/activate-sports',
    methods=['POST'])
def activate_sports():
    return sports_view.SportsView().activate(request)


@app.route(
    '/api/v1.0/people/preferences/delete-sports',
    methods=['POST'])
def delete_sports():
    return sports_view.SportsView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_contact_me
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-contact-me-hash',
    methods=['POST'])
def get_contact_me_hash():
    return contact_me_view.ContactMeView().retrieve(request)


@app.route(
    '/api/v1.0/people/profile/get-contact-me-id',
    methods=['POST'])
def get_contact_me_id():
    return contact_me_view.ContactMeView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/profile/update-contact-me',
    methods=['POST'])
def update_contact_me():
    return contact_me_view.ContactMeView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-contact-me',
    methods=['POST'])
def insert_contact_me():
    return contact_me_view.ContactMeView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-contact-me',
    methods=['POST'])
def deactivate_contact_me():
    return contact_me_view.ContactMeView().deactivate(request)


@app.route(
    '/api/v1.0/people/profile/activate-contact-me',
    methods=['POST'])
def activate_contact_me():
    return contact_me_view.ContactMeView().activate(request)


@app.route(
    '/api/v1.0/people/profile/delete-contact-me',
    methods=['POST'])
def delete_contact_me():
    return contact_me_view.ContactMeView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_documents
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-documents-hash',
    methods=['POST'])
def get_documents_hash():
    return documents_view.DocumentsView().retrieve(request)


@app.route(
    '/api/v1.0/people/profile/get-documents-id',
    methods=['POST'])
def get_documents_id():
    return documents_view.DocumentsView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/profile/update-documents',
    methods=['POST'])
def update_documents():
    return documents_view.DocumentsView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-documents',
    methods=['POST'])
def insert_documents():
    return documents_view.DocumentsView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-documents',
    methods=['POST'])
def deactivate_documents():
    return documents_view.DocumentsView().deactivate(request)


@app.route(
    '/api/v1.0/people/profile/activate-documents',
    methods=['POST'])
def activate_documents():
    return documents_view.DocumentsView().activate(request)


@app.route(
    '/api/v1.0/people/profile/delete-documents',
    methods=['POST'])
def delete_documents():
    return documents_view.DocumentsView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_education
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-education-hash',
    methods=['POST'])
def get_education_hash():
    return education_view.EducationView().retrieve(request)


@app.route(
    '/api/v1.0/people/profile/get-education-id',
    methods=['POST'])
def get_education_id():
    return education_view.EducationView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/profile/update-education',
    methods=['POST'])
def update_education():
    return education_view.EducationView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-education',
    methods=['POST'])
def insert_education():
    return education_view.EducationView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-education',
    methods=['POST'])
def deactivate_education():
    return education_view.EducationView().deactivate(request)


@app.route(
    '/api/v1.0/people/profile/activate-education',
    methods=['POST'])
def activate_education():
    return education_view.EducationView().activate(request)


@app.route(
    '/api/v1.0/people/profile/delete-education',
    methods=['POST'])
def delete_education():
    return education_view.EducationView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_health_know_issues
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-health-know-issues-hash',
    methods=['POST'])
def get_health_know_issues_hash():
    return health_know_issues_view.HealthKnowIssuesView().retrieve(request)


@app.route(
    '/api/v1.0/people/profile/get-health-know-issues-id',
    methods=['POST'])
def get_health_know_issues_id():
    return health_know_issues_view.HealthKnowIssuesView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/profile/update-health-know-issues',
    methods=['POST'])
def update_health_know_issues():
    return health_know_issues_view.HealthKnowIssuesView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-health-know-issues',
    methods=['POST'])
def insert_health_know_issues():
    return health_know_issues_view.HealthKnowIssuesView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-health-know-issues',
    methods=['POST'])
def deactivate_health_know_issues():
    return health_know_issues_view.HealthKnowIssuesView().deactivate(request)


@app.route(
    '/api/v1.0/people/profile/activate-health-know-issues',
    methods=['POST'])
def activate_health_know_issues():
    return health_know_issues_view.HealthKnowIssuesView().activate(request)


@app.route(
    '/api/v1.0/people/profile/delete-health-know-issues',
    methods=['POST'])
def delete_health_know_issues():
    return health_know_issues_view.HealthKnowIssuesView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_health_my_body
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-health-my-body-hash',
    methods=['POST'])
def get_health_my_body_hash():
    return health_my_body_view.HealthMyBodyView().retrieve(request)


@app.route(
    '/api/v1.0/people/profile/get-health-my-body-id',
    methods=['POST'])
def get_health_my_body_id():
    return health_my_body_view.HealthMyBodyView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/profile/update-health-my-body',
    methods=['POST'])
def update_health_my_body():
    return health_my_body_view.HealthMyBodyView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-health-my-body',
    methods=['POST'])
def insert_health_my_body():
    return health_my_body_view.HealthMyBodyView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-health-my-body',
    methods=['POST'])
def deactivate_health_my_body():
    return health_my_body_view.HealthMyBodyView().deactivate(request)


@app.route(
    '/api/v1.0/people/profile/activate-health-my-body',
    methods=['POST'])
def activate_health_my_body():
    return health_my_body_view.HealthMyBodyView().activate(request)


@app.route(
    '/api/v1.0/people/profile/delete-health-my-body',
    methods=['POST'])
def delete_health_my_body():
    return health_my_body_view.HealthMyBodyView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_health_prescription
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-health-prescription-hash',
    methods=['POST'])
def get_health_prescription_hash():
    return health_prescription_view.HealthPrescriptionView().retrieve(request)


@app.route(
    '/api/v1.0/people/profile/get-health-prescription-id',
    methods=['POST'])
def get_health_prescription_id():
    return health_prescription_view.HealthPrescriptionView().retrieve_id(
        request)


@app.route(
    '/api/v1.0/people/profile/update-health-prescription',
    methods=['POST'])
def update_health_prescription():
    return health_prescription_view.HealthPrescriptionView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-health-prescription',
    methods=['POST'])
def insert_health_prescription():
    return health_prescription_view.HealthPrescriptionView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-health-prescription',
    methods=['POST'])
def deactivate_health_prescription():
    return health_prescription_view.HealthPrescriptionView().deactivate(
        request)


@app.route(
    '/api/v1.0/people/profile/activate-health-prescription',
    methods=['POST'])
def activate_health_prescription():
    return health_prescription_view.HealthPrescriptionView().activate(request)


@app.route(
    '/api/v1.0/people/profile/delete-health-prescription',
    methods=['POST'])
def delete_health_prescription():
    return health_prescription_view.HealthPrescriptionView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_my_family
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-my-family-hash',
    methods=['POST'])
def get_my_family_hash():
    return my_family_view.MyFamilyView().retrieve(request)


@app.route(
    '/api/v1.0/people/profile/get-my-family-id',
    methods=['POST'])
def get_my_family_id():
    return my_family_view.MyFamilyView().retrieve_id(
        request)


@app.route(
    '/api/v1.0/people/profile/update-my-family',
    methods=['POST'])
def update_my_family():
    return my_family_view.MyFamilyView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-my-family',
    methods=['POST'])
def insert_my_family():
    return my_family_view.MyFamilyView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-my-family',
    methods=['POST'])
def deactivate_my_family():
    return my_family_view.MyFamilyView().deactivate(
        request)


@app.route(
    '/api/v1.0/people/profile/activate-my-family',
    methods=['POST'])
def activate_my_family():
    return my_family_view.MyFamilyView().activate(request)


@app.route(
    '/api/v1.0/people/profile/delete-my-family',
    methods=['POST'])
def delete_my_family():
    return my_family_view.MyFamilyView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_professional_history
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-professional-history-hash',
    methods=['POST'])
def get_professional_history_hash():
    return professional_history_view.ProfessionalHistoryView().retrieve(
        request)


@app.route(
    '/api/v1.0/people/profile/get-professional-history-id',
    methods=['POST'])
def get_professional_history_id():
    return professional_history_view.ProfessionalHistoryView().retrieve_id(
        request)


@app.route(
    '/api/v1.0/people/profile/update-professional-history',
    methods=['POST'])
def update_professional_history():
    return professional_history_view.ProfessionalHistoryView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-professional-history',
    methods=['POST'])
def insert_professional_history():
    return professional_history_view.ProfessionalHistoryView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-professional-history',
    methods=['POST'])
def deactivate_professional_history():
    return professional_history_view.ProfessionalHistoryView().deactivate(
        request)


@app.route(
    '/api/v1.0/people/profile/activate-professional-history',
    methods=['POST'])
def activate_professional_history():
    return professional_history_view.ProfessionalHistoryView().activate(
        request)


@app.route(
    '/api/v1.0/people/profile/delete-professional-history',
    methods=['POST'])
def delete_professional_history():
    return professional_history_view.ProfessionalHistoryView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_professional_skills
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-professional-skills-hash',
    methods=['POST'])
def get_professional_skills_hash():
    return professional_skills_view.ProfessionalSkillsView().retrieve(
        request)


@app.route(
    '/api/v1.0/people/profile/get-professional-skills-id',
    methods=['POST'])
def get_professional_skills_id():
    return professional_skills_view.ProfessionalSkillsView().retrieve_id(
        request)


@app.route(
    '/api/v1.0/people/profile/update-professional-skills',
    methods=['POST'])
def update_professional_skills():
    return professional_skills_view.ProfessionalSkillsView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-professional-skills',
    methods=['POST'])
def insert_professional_skills():
    return professional_skills_view.ProfessionalSkillsView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-professional-skills',
    methods=['POST'])
def deactivate_professional_skills():
    return professional_skills_view.ProfessionalSkillsView().deactivate(
        request)


@app.route(
    '/api/v1.0/people/profile/activate-professional-skills',
    methods=['POST'])
def activate_professional_skills():
    return professional_skills_view.ProfessionalSkillsView().activate(
        request)


@app.route(
    '/api/v1.0/people/profile/delete-professional-skills',
    methods=['POST'])
def delete_professional_skills():
    return professional_skills_view.ProfessionalSkillsView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-profile-hash',
    methods=['POST'])
def get_profile_hash():
    return profile_view.ProfileView().retrieve(request)


@app.route(
    '/api/v1.0/people/profile/get-profile-id',
    methods=['POST'])
def get_profile_id():
    return profile_view.ProfileView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/profile/update-profile',
    methods=['POST'])
def update_profile():
    return profile_view.ProfileView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-profile',
    methods=['POST'])
def insert_profile():
    return profile_view.ProfileView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-profile',
    methods=['POST'])
def deactivate_profile():
    return profile_view.ProfileView().deactivate(request)


@app.route(
    '/api/v1.0/people/profile/activate-profile',
    methods=['POST'])
def activate_profile():
    return profile_view.ProfileView().activate(request)


@app.route(
    '/api/v1.0/people/profile/delete-profile',
    methods=['POST'])
def delete_profile():
    return profile_view.ProfileView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_scorecard
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-scorecard-hash',
    methods=['POST'])
def get_scorecard_hash():
    return scorecard_view.ScoreCardView().retrieve(request)


@app.route(
    '/api/v1.0/people/profile/get-scorecard-id',
    methods=['POST'])
def get_scorecard_id():
    return scorecard_view.ScoreCardView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/profile/update-scorecard',
    methods=['POST'])
def update_scorecard():
    return scorecard_view.ScoreCardView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-scorecard',
    methods=['POST'])
def insert_scorecard():
    return scorecard_view.ScoreCardView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-scorecard',
    methods=['POST'])
def deactivate_scorecard():
    return scorecard_view.ScoreCardView().deactivate(request)


@app.route(
    '/api/v1.0/people/profile/activate-scorecard',
    methods=['POST'])
def activate_scorecard():
    return scorecard_view.ScoreCardView().activate(request)


@app.route(
    '/api/v1.0/people/profile/delete-scorecard',
    methods=['POST'])
def delete_scorecard():
    return scorecard_view.ScoreCardView().delete(request)


# ----------------------------------------------------------------------
# myid_people_profile_social_contacts
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-social-contacts-hash',
    methods=['POST'])
def get_social_contacts_hash():
    return social_contacts_view.SocialContactsView().retrieve(
        request)


@app.route(
    '/api/v1.0/people/profile/get-social-contacts-id',
    methods=['POST'])
def get_social_contacts_id():
    return social_contacts_view.SocialContactsView().retrieve_id(
        request)


@app.route(
    '/api/v1.0/people/profile/update-social-contacts',
    methods=['POST'])
def update_social_contacts():
    return social_contacts_view.SocialContactsView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-social-contacts',
    methods=['POST'])
def insert_social_contacts():
    return social_contacts_view.SocialContactsView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-social-contacts',
    methods=['POST'])
def deactivate_social_contacts():
    return social_contacts_view.SocialContactsView().deactivate(
        request)


@app.route(
    '/api/v1.0/people/profile/activate-social-contacts',
    methods=['POST'])
def activate_social_contacts():
    return social_contacts_view.SocialContactsView().activate(
        request)


@app.route(
    '/api/v1.0/people/profile/delete-social-contacts',
    methods=['POST'])
def delete_social_contacts():
    return social_contacts_view.SocialContactsView().delete(request)


# ----------------------------------------------------------------------
# myid_people_my_lists
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/profile/get-my-lists-hash',
    methods=['POST'])
def get_index_fields_hash():
    return my_lists_view.MyListsView().retrieve(
        request)


@app.route(
    '/api/v1.0/people/profile/get-my-lists-id',
    methods=['POST'])
def get_index_fields_id():
    return my_lists_view.MyListsView().retrieve_id(
        request)


@app.route(
    '/api/v1.0/people/profile/update-my-lists',
    methods=['POST'])
def update_get_index_fields():
    return my_lists_view.MyListsView().update(request)


@app.route(
    '/api/v1.0/people/profile/insert-my-lists',
    methods=['POST'])
def insert_get_index_fields():
    return my_lists_view.MyListsView().insert(request)


@app.route(
    '/api/v1.0/people/profile/deactivate-my-lists',
    methods=['POST'])
def deactivate_get_index_fields():
    return my_lists_view.MyListsView().deactivate(
        request)


@app.route(
    '/api/v1.0/people/profile/activate-my-lists',
    methods=['POST'])
def activate_get_index_fields():
    return my_lists_view.MyListsView().activate(
        request)


@app.route(
    '/api/v1.0/people/profile/delete-my-lists',
    methods=['POST'])
def delete_get_index_fields():
    return my_lists_view.MyListsView().delete(request)


# ----------------------------------------------------------------------
# myid_people_security_activity_history
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# myid_people_security_login
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/people/security/get-login-username',
    methods=['POST'])
def get_login_hash():
    return login_view.LoginView().retrieve(request)


@app.route(
    '/api/v1.0/people/security/get-login-id',
    methods=['POST'])
def get_login_id():
    return login_view.LoginView().retrieve_id(request)


@app.route(
    '/api/v1.0/people/security/update-login',
    methods=['POST'])
def update_login():
    return login_view.LoginView().update(request)


@app.route(
    '/api/v1.0/people/security/insert-login',
    methods=['POST'])
def insert_login():
    return login_view.LoginView().insert(request)


@app.route(
    '/api/v1.0/people/security/deactivate-login',
    methods=['POST'])
def deactivate_login():
    return login_view.LoginView().deactivate(request)


@app.route(
    '/api/v1.0/people/security/activate-login',
    methods=['POST'])
def activate_login():
    return login_view.LoginView().activate(request)


@app.route(
    '/api/v1.0/people/security/delete-login',
    methods=['POST'])
def delete_login():
    return login_view.LoginView().delete(request)


@app.route(
    '/api/v1.0/people/security/validate-login',
    methods=['POST'])
def validate_login():
    return login_view.LoginView().validate_login(request)


@app.route(
    '/api/v1.0/people/security/validate-first-login',
    methods=['POST'])
def validade_first_login():
    return login_view.LoginView().validade_first_login(request)


@app.route(
    '/api/v1.0/people/security/reset-password-login',
    methods=['POST'])
def reset_password_login():
    return login_view.LoginView().reset_password_login(request)


# ----------------------------------------------------------------------
# shop_product_inventory
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/product/get-inventory',
    methods=['POST'])
def get_product_inventory():
    return product_inventory_view.ProductInventoryView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/product/get-inventory-id',
    methods=['POST'])
def get_product_inventory_id():
    return product_inventory_view.ProductInventoryView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/product/update-inventory',
    methods=['POST'])
def update_product_inventory():
    return product_inventory_view.ProductInventoryView() \
        .update(request)


@app.route(
    '/api/v1.0/product/insert-inventory',
    methods=['POST'])
def insert_product_inventory():
    return product_inventory_view.ProductInventoryView() \
        .insert(request)


@app.route(
    '/api/v1.0/product/deactivate-inventory',
    methods=['POST'])
def deactivate_product_inventory():
    return product_inventory_view.ProductInventoryView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/product/activate-inventory',
    methods=['POST'])
def activate_product_inventory():
    return product_inventory_view.ProductInventoryView() \
        .activate(request)


@app.route(
    '/api/v1.0/product/delete-inventory',
    methods=['POST'])
def delete_product_inventory():
    return product_inventory_view.ProductInventoryView() \
        .delete(request)


# ----------------------------------------------------------------------
# shop_product_reviews
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/product/get-reviews',
    methods=['POST'])
def get_reviews():
    return product_reviews_view.ProductReviewsView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/product/get-reviews-id',
    methods=['POST'])
def get_reviews_id():
    return product_reviews_view.ProductReviewsView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/product/update-reviews',
    methods=['POST'])
def update_reviews():
    return product_reviews_view.ProductReviewsView() \
        .update(request)


@app.route(
    '/api/v1.0/product/insert-reviews',
    methods=['POST'])
def insert_reviews():
    return product_reviews_view.ProductReviewsView() \
        .insert(request)


@app.route(
    '/api/v1.0/product/deactivate-reviews',
    methods=['POST'])
def deactivate_reviews():
    return product_reviews_view.ProductReviewsView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/product/activate-reviews',
    methods=['POST'])
def activate_reviews():
    return product_reviews_view.ProductReviewsView() \
        .activate(request)


@app.route(
    '/api/v1.0/product/delete-reviews',
    methods=['POST'])
def delete_reviews():
    return product_reviews_view.ProductReviewsView() \
        .delete(request)


# ----------------------------------------------------------------------
# shop_product
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/product/get-product',
    methods=['POST'])
def get_product():
    return product_view.ProductView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/product/get-product-id',
    methods=['POST'])
def get_product_id():
    return product_view.ProductView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/product/update-product',
    methods=['POST'])
def update_product():
    return product_view.ProductView() \
        .update(request)


@app.route(
    '/api/v1.0/product/insert-product',
    methods=['POST'])
def insert_product():
    return product_view.ProductView() \
        .insert(request)


@app.route(
    '/api/v1.0/product/deactivate-product',
    methods=['POST'])
def deactivate_product():
    return product_view.ProductView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/product/activate-product',
    methods=['POST'])
def activate_product():
    return product_view.ProductView() \
        .activate(request)


@app.route(
    '/api/v1.0/product/delete-product',
    methods=['POST'])
def delete_product():
    return product_view.ProductView() \
        .delete(request)


# ----------------------------------------------------------------------
# mkpl_sales_engine_setup
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/sales/get-engine-setup',
    methods=['POST'])
def get_engine_setup():
    return engine_setup_view.SalesEngineSetupView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/sales/get-engine-setup-id',
    methods=['POST'])
def get_engine_setup_id():
    return engine_setup_view.SalesEngineSetupView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/sales/update-engine-setup',
    methods=['POST'])
def update_engine_setup():
    return engine_setup_view.SalesEngineSetupView() \
        .update(request)


@app.route(
    '/api/v1.0/sales/insert-engine-setup',
    methods=['POST'])
def insert_engine_setup():
    return engine_setup_view.SalesEngineSetupView() \
        .insert(request)


# ----------------------------------------------------------------------
# mkpl_sales_negotiation_history
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/sales/get-sales-negotiation-history',
    methods=['POST'])
def get_sales_negotiation_history():
    return negotiation_history_view.SalesNegotiationHistoryView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/sales/get-sales-negotiation-history-id',
    methods=['POST'])
def get_sales_negotiation_history_id():
    return negotiation_history_view.SalesNegotiationHistoryView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/sales/update-sales-negotiation-history',
    methods=['POST'])
def update_sales_negotiation_history():
    return negotiation_history_view.SalesNegotiationHistoryView() \
        .update(request)


@app.route(
    '/api/v1.0/sales/insert-sales-negotiation-history',
    methods=['POST'])
def insert_sales_negotiation_history():
    return negotiation_history_view.SalesNegotiationHistoryView() \
        .insert(request)


# ----------------------------------------------------------------------
# mkpl_sales_transactions
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/sales/get-sales-transactions',
    methods=['POST'])
def get_sales_transactions():
    return sales_transactions_view.SalesTransactionsView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/sales/get-sales-transactions-id',
    methods=['POST'])
def get_sales_transactions_id():
    return sales_transactions_view.SalesTransactionsView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/sales/update-sales-transactions',
    methods=['POST'])
def update_sales_transactions():
    return sales_transactions_view.SalesTransactionsView() \
        .update(request)


@app.route(
    '/api/v1.0/sales/insert-sales-transactions',
    methods=['POST'])
def insert_sales_transactions():
    return sales_transactions_view.SalesTransactionsView() \
        .insert(request)


# ----------------------------------------------------------------------
# shop_store_sales_setup
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/store/get-store-sales-setup',
    methods=['POST'])
def get_store_sales_setup():
    return store_sales_setup_view.StoreSalesSetupView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/store/get-store-sales-setup-id',
    methods=['POST'])
def get_store_sales_setup_id():
    return store_sales_setup_view.StoreSalesSetupView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/store/update-store-sales-setup',
    methods=['POST'])
def update_store_sales_setup():
    return store_sales_setup_view.StoreSalesSetupView() \
        .update(request)


@app.route(
    '/api/v1.0/store/insert-store-sales-setup',
    methods=['POST'])
def insert_store_sales_setup():
    return store_sales_setup_view.StoreSalesSetupView() \
        .insert(request)


@app.route(
    '/api/v1.0/store/deactivate-store-sales-setup',
    methods=['POST'])
def deactivate_store_sales_setup():
    return store_sales_setup_view.StoreSalesSetupView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/store/activate-store-sales-setup',
    methods=['POST'])
def activate_store_sales_setup():
    return store_sales_setup_view.StoreSalesSetupView() \
        .activate(request)


@app.route(
    '/api/v1.0/store/delete-store-sales-setup',
    methods=['POST'])
def delete_store_sales_setup():
    return store_sales_setup_view.StoreSalesSetupView() \
        .delete(request)


# ----------------------------------------------------------------------
# shop_store_sales_team_apply
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/store/get-store-sales-team-apply',
    methods=['POST'])
def get_store_sales_team_apply():
    return store_sales_team_apply_view.StoreSalesTeamApplyView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/store/get-store-sales-team-apply-id',
    methods=['POST'])
def get_store_sales_team_apply_id():
    return store_sales_team_apply_view.StoreSalesTeamApplyView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/store/update-store-sales-team-apply',
    methods=['POST'])
def update_store_sales_team_apply():
    return store_sales_team_apply_view.StoreSalesTeamApplyView() \
        .update(request)


@app.route(
    '/api/v1.0/store/insert-store-sales-team-apply',
    methods=['POST'])
def insert_store_sales_team_apply():
    return store_sales_team_apply_view.StoreSalesTeamApplyView() \
        .insert(request)


@app.route(
    '/api/v1.0/store/deactivate-store-sales-team-apply',
    methods=['POST'])
def deactivate_store_sales_team_apply():
    return store_sales_team_apply_view.StoreSalesTeamApplyView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/store/activate-store-sales-team-apply',
    methods=['POST'])
def activate_store_sales_team_apply():
    return store_sales_team_apply_view.StoreSalesTeamApplyView() \
        .activate(request)


@app.route(
    '/api/v1.0/store/delete-store-sales-team-apply',
    methods=['POST'])
def delete_store_sales_team_apply():
    return store_sales_team_apply_view.StoreSalesTeamApplyView() \
        .delete(request)


# ----------------------------------------------------------------------
# shop_store_sales_team_setup
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/store/get-store-sales-team-setup',
    methods=['POST'])
def get_store_sales_team_setup():
    return store_sales_team_setup_view.StoreSalesTeamSetupView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/store/get-store-sales-team-setup-id',
    methods=['POST'])
def get_store_sales_team_setup_id():
    return store_sales_team_setup_view.StoreSalesTeamSetupView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/store/update-store-sales-team-setup',
    methods=['POST'])
def update_store_sales_team_setup():
    return store_sales_team_setup_view.StoreSalesTeamSetupView() \
        .update(request)


@app.route(
    '/api/v1.0/store/insert-store-sales-team-setup',
    methods=['POST'])
def insert_store_sales_team_setup():
    return store_sales_team_setup_view.StoreSalesTeamSetupView() \
        .insert(request)


@app.route(
    '/api/v1.0/store/deactivate-store-sales-team-setup',
    methods=['POST'])
def deactivate_store_sales_team_setup():
    return store_sales_team_setup_view.StoreSalesTeamSetupView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/store/activate-store-sales-team-setup',
    methods=['POST'])
def activate_store_sales_team_setup():
    return store_sales_team_setup_view.StoreSalesTeamSetupView() \
        .activate(request)


@app.route(
    '/api/v1.0/store/delete-store-sales-team-setup',
    methods=['POST'])
def delete_store_sales_team_setup():
    return store_sales_team_setup_view.StoreSalesTeamSetupView() \
        .delete(request)


# ----------------------------------------------------------------------
# shop_store
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/store/get-store',
    methods=['POST'])
def get_store():
    return store_view.StoreView() \
        .retrieve(request)


@app.route(
    '/api/v1.0/store/get-store-id',
    methods=['POST'])
def get_store_id():
    return store_view.StoreView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/store/update-store',
    methods=['POST'])
def update_store():
    return store_view.StoreView() \
        .update(request)


@app.route(
    '/api/v1.0/store/insert-store',
    methods=['POST'])
def insert_store():
    return store_view.StoreView() \
        .insert(request)


@app.route(
    '/api/v1.0/store/deactivate-store',
    methods=['POST'])
def deactivate_store():
    return store_view.StoreView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/store/activate-store',
    methods=['POST'])
def activate_store():
    return store_view.StoreView() \
        .activate(request)


@app.route(
    '/api/v1.0/store/delete-store',
    methods=['POST'])
def delete_store():
    return store_view.StoreView() \
        .delete(request)


# ----------------------------------------------------------------------
# sysm_plataform_error_codes
# ----------------------------------------------------------------------
@app.route(
    '/api/v1.0/system/get-error-codes-all',
    methods=['POST'])
def get_error_codes():
    return error_codes_view.ErrorCodesView() \
        .retrieve_all(request)


@app.route(
    '/api/v1.0/system/get-error-codes-id',
    methods=['POST'])
def get_error_codes_id():
    return error_codes_view.ErrorCodesView() \
        .retrieve_id(request)


@app.route(
    '/api/v1.0/system/update-error-codes',
    methods=['POST'])
def update_error_codes():
    return error_codes_view.ErrorCodesView() \
        .update(request)


@app.route(
    '/api/v1.0/system/insert-error-codes',
    methods=['POST'])
def insert_error_codes():
    return error_codes_view.ErrorCodesView() \
        .insert(request)


@app.route(
    '/api/v1.0/system/deactivate-error-codes',
    methods=['POST'])
def deactivate_error_codes():
    return error_codes_view.ErrorCodesView() \
        .deactivate(request)


@app.route(
    '/api/v1.0/system/activate-error-codes',
    methods=['POST'])
def activate_error_codes():
    return error_codes_view.ErrorCodesView() \
        .activate(request)


@app.route(
    '/api/v1.0/system/delete-error-codes',
    methods=['POST'])
def delete_error_codes():
    return error_codes_view.ErrorCodesView() \
        .delete(request)


# include this for local dev
if __name__ == '__main__':
    app.run(debug=True)

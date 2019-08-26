import datetime

from flask import Flask

import server_conector

from system.error_codes_view import ErrorCodesView
from system.system_activity_view import SystemActivityView
from system.system_category_view import SystemCategoryView
from system.system_module_view import SystemModuleView

from slackbot.slackbot_view import SlackbotView

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class LoggerView(ErrorCodesView,
                 SystemActivityView,
                 SystemCategoryView,
                 SystemModuleView):

    def __init__(self, data, **kwargs):
        self.el = server_conector.ServerConector()
        self.log_dict = {}

        # self.log_dict['login_hash'] = data.get('login_hash', None)
        # self.log_dict['username'] = data.get('username', None)

        self.log_info = data.pop('log_info', None)
        if self.log_info:
            ip_address = self.log_info.get('ip_address', None)
            if ip_address:
                self.log_dict['ip_address'] = ip_address

            web_browser = self.log_info.get('web_browser', None)
            if web_browser:
                self.log_dict['web_browser'] = web_browser

            url_description = self.log_info.get('url_description', None)
            if url_description:
                self.log_dict['url_description'] = url_description

            device_description = self.log_info.get('device_description', None)
            if device_description:
                self.log_dict['device_description'] = device_description

        self.log_dict['json_text'] = data

    def insert_user_activity(self, system_category,
                             system_module,
                             system_activity,
                             log_description):

        self.log_dict['timestamp'] = datetime.datetime.now()
        self.log_dict['category'] = 'User Activity'
        self.log_dict['system_category'] = system_category
        self.log_dict['system_module'] = system_module
        self.log_dict['system_activity'] = system_activity
        self.log_dict['log_description'] = log_description

        self.el.insert_el(
            index='sysm_plataform_activity_history', data=self.log_dict)

    def insert_system_error(self, system_category,
                            system_module,
                            system_activity,
                            error_code,
                            log_description,
                            notify=False):

        self.log_dict['timestamp'] = datetime.datetime.now()
        self.log_dict['category'] = 'System Error'
        self.log_dict['system_category'] = system_category
        self.log_dict['system_module'] = system_module
        self.log_dict['system_activity'] = system_activity
        self.log_dict['error_code'] = error_code

        error_obj = self.retrieve_code(error_code)
        self.log_dict['error_message'] = error_obj['error_message']

        self.log_dict['log_description'] = log_description

        if notify:
            message = (
                f':x: {self.log_dict["category"]} :x: \n'
                f'Categoria do sistema: {system_category} \n'
                f'Módulo do sistema: {system_module} \n'
                f'Atividade do sistema: {system_activity} \n'
                f'Código do erro: {error_code} \n'
                f'Mensagem do erro: {self.log_dict["error_message"]} \n'
                f'Descrição do log: {log_description} \n'
            )
            SlackbotView().send_message(message=message)

        self.el.insert_el(
            index='sysm_plataform_activity_history', data=self.log_dict)

    def insert_error_message(self, system_category,
                             system_module,
                             system_activity,
                             error_code,
                             log_description,
                             notify=False):

        self.log_dict['timestamp'] = datetime.datetime.now()
        self.log_dict['category'] = 'Error Message'
        self.log_dict['system_category'] = system_category
        self.log_dict['system_module'] = system_module
        self.log_dict['system_activity'] = system_activity
        self.log_dict['error_code'] = error_code

        error_obj = self.retrieve_code(error_code)
        self.log_dict['error_message'] = error_obj['error_message']

        self.log_dict['log_description'] = log_description

        if notify:
            message = (
                f':warning: {self.log_dict["category"]} :warning: \n'
                f'Categoria do sistema: {system_category} \n'
                f'Módulo do sistema: {system_module} \n'
                f'Atividade do sistema: {system_activity} \n'
                f'Código do erro: {error_code} \n'
                f'Mensagem do erro: {self.log_dict["error_message"]} \n'
                f'Descrição do log: {log_description} \n'
            )
            SlackbotView().send_message(message=message)

        self.el.insert_el(
            index='sysm_plataform_activity_history', data=self.log_dict)

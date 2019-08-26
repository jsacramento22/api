from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'

app = Flask(__name__)


class SystemModuleView():
    def get_module_user(self):
        return 'Usuário'

    def get_module_product(self):
        return 'Produto'

    def get_module_store(self):
        return 'Loja'

    def get_module_marketplace(self):
        return 'Marketplace'

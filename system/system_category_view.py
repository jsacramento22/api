from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'

app = Flask(__name__)


class SystemCategoryView():
    def get_category_technical(self):
        return 'Erro Técnico(Infra/Banco/WebServer)'

    def get_category_operational(self):
        return 'Erro Operacional'

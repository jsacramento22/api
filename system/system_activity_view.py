from flask import Flask

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'

app = Flask(__name__)


class SystemActivityView():
    def get_actinity_create(self):
        return 'Create'

    def get_actinity_read(self):
        return 'Read'

    def get_actinity_update(self):
        return 'Update'

    def get_actinity_delete(self):
        return 'Delete'

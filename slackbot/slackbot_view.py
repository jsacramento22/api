import os

from flask import Flask, jsonify

import slack

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class SlackbotView:

    def __init__(self):
        self.slack_token = os.environ.get('SLACK_TOKEN')
        self.slack_client = slack.WebClient(self.slack_token)

    def send_message(self, message,
                     channel=os.environ.get('SLACK_DEFAULT_CHANNEL')):

        self.slack_client.chat_postMessage(
            channel=channel,
            text=message
        )

        return jsonify('Feito!')

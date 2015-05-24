__author__ = 'Hibiki'

import json

PUB_KEY = "0000"
AUTH_TOKEN = "12345"

def auth(pub_key):
    if pub_key == PUB_KEY:
        ret = {
            'res': 'ok',
            'auth_token': AUTH_TOKEN
        }
    else:
        ret = {
            'res': 'err',
            'reason': 'Sorry, Passphrase is NOT valid.'
        }
    return json.dumps(ret)


def check(token):
    return token == AUTH_TOKEN


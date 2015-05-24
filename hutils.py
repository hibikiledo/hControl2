__author__ = 'Hibiki'

import json

def errormsg(msg):
    return json.dumps({'ret': 'err', 'reason': msg})
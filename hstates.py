__author__ = 'Hibiki'

import json

'''
    This module keep the states of objects in house.
    It provides 4 main functions :

        add(obj, group) - add new object in specified group
        remove(obj, group) - remove obj
        get(obj) - get current value of obj
        set(obj, value) - set new value to obj
'''

# Constants
OUTDOOR = 'OUTDOOR'
INDOOR = 'INDOOR'

# This module provides the following groups
GROUPS = ['OUTDOOR', 'INDOOR']
VALUES = ['off', 'on']


# Dictionary contains the mapping of obj with value
__map__ = {'OUTDOOR': [], 'INDOOR': []}



def add(obj, group):
    # add obj into __map__
    try:
        __map__[group].append({'object': obj, 'value': 'off'})
        return True
    except KeyError:
        print "Trying to add group:", group, "which is not supported."
        print "The following groups are supported:\n\t", ", ".join(GROUPS)
        return False


def remove(obj, group):
    # get objs from group
    try:
        objs = __map__[group]
    except KeyError:
        print "Trying to access group:", group, "which is not supported."
        print "The following groups are supported:\n\t", ", ".join(GROUPS)
        return False

    # remove specified object
    for o in objs:
        if o['object'] == obj:
            objs.remove({'object': obj, 'value': o['value']})
            return True

    # return -1 for failure
    return False


def get(obj, group):
    # get objs from group
    try:
        objs = __map__[group]
    except KeyError:
        errmsg = " ".join(
            [
                "Trying to access group: `{}` which is not supported.".format(group),
                "The following groups are supported: {}".format(", ".join(GROUPS))
            ]
        )
        return json.dumps({'res': 'err', 'reason': errmsg})

    # get value of the specified object
    for o in objs:
        if o['object'] == obj:
            return json.dumps({'res': 'ok', 'value': o['value']})

    # not found in objs
    errmsg = (
        "Trying to set value of object: `{}` which is not existed in group {}.".format(obj, group)
    )
    return json.dumps({'res': 'err', 'reason': errmsg})


def set(obj, group, value):
    # get objs from group
    try:
        objs = __map__[group]
    except KeyError:
        errmsg = " ".join(
            [
                "Trying to access group: `{}` which is not supported.".format(group),
                "The following groups are supported: {}".format(", ".join(GROUPS))
            ]
        )
        return json.dumps({'res': 'err', 'reason': errmsg})

    # check value
    if value not in VALUES:
        errmsg = " ".join(
            [
                "Trying to set value: `{}` which is not supported.".format(value),
                "The following values are supported: {}".format(", ".join(VALUES))
            ]
        )
        return json.dumps({'res': 'err', 'reason': errmsg})

    # set value of the specified object
    for o in objs:
        if o['object'] == obj:
            o['value'] = value
            return json.dumps({'res': 'ok'})

    # return useful error message for failure
    errmsg = (
        "Trying to set value of object: `{}` which is not existed in group {}.".format(obj, group)
    )
    return json.dumps({'res': 'err', 'reason': errmsg})


def report():
    return json.dumps({'res': 'ok', 'data': __map__})


if __name__ == '__main__':
    # setup home state
    add('spotlight_1', OUTDOOR)
    print(get('spotlight_1', 'OUTDOOR'))
    set('spotlight_1', OUTDOOR, 'onn')
    print(get('spotlight_1', OUTDOOR))
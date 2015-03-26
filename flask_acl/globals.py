import functools

import werkzeug as wz
from flask import current_app


load_user = None


def user_loader(func):
    global load_user
    load_user = func
    return func


#: Proxy to the current Flask app's :class:`.ACLManager`.
current_acl_manager = wz.local.LocalProxy(lambda: current_app.acl_manager)
current_user = wz.local.LocalProxy(lambda: load_user())

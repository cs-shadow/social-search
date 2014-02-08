from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.security import authenticated_userid

from models import DBSession,Post,PostTag,PostLike,PostDislike
from ..users.models import User
from ..util import getTimeEpoch

from sqlalchemy import and_

@view_config(route_name='postAdd',renderer='json')
def postAdd(request):
    return {}

@view_config(route_name='postGet',renderer='json')
def postGet(request):
    return {}

@view_config(route_name='postLike',renderer='json')
def postLike(request):
    return {}

@view_config(route_name='postDislike',renderer='json')
def postDislike(request):
    return {}

@view_config(route_name='postDelete',renderer='json')
def postDelete(request):
    return {}


from pyramid.response import Response
from pyramid.view import view_config,forbidden_view_config
from pyramid.security import remember,authenticated_userid, forget, Authenticated
from pyramid.httpexceptions import HTTPFound

from models import DBSession

from sqlalchemy import and_
import hashlib

@view_config(route_name='home',renderer='json', permission='__no_permission_required__')
def homeView(request):
    return {'hi' : 'user'}

@forbidden_view_config()
def forbidden(request):
    return Response('Not Allowed')

@view_config(context='pyramid.exceptions.NotFound', renderer='json', permission='__no_permission_required__')
def notFound_view(request):
    notFound404 = '404 Not Found'
    return {'error' : notFound404}
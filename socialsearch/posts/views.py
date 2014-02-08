from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.security import authenticated_userid

from models import DBSession,Post,PostTag,PostLike,PostDislike
from ..users.models import User
from ..util import getTimeEpoch,row2dict

from sqlalchemy import and_

@view_config(route_name='postAdd',renderer='json',request_method='POST')
def postAdd(request):
    
    currentUser = int(authenticated_userid(request))
    
    rankWeight = None #TODO
    
    topic_id = request.POST['topic']
    content_title = request.POST['content_title']
    content_URL = request.POST['content_URL']
    content_type = "URL" #TODO
    
    postToSave = Post(currentUser,rankWeight,content_title,content_URL,content_type,topic_id)
    DBSession.add(postToSave)
    DBSession.flush()
    
    return {'post' : row2dict(postToSave)}

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

@view_config(route_name='postFeed',renderer='json')
def postFeed(request):
    return {}


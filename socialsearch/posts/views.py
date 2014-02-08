from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.security import authenticated_userid

from models import DBSession,Post,PostTag,PostLike,PostDislike,Content
from ..users.models import User
from ..util import getTimeEpoch,row2dict

from sqlalchemy import and_

@view_config(route_name='postAdd',renderer='json',request_method='POST')
def postAdd(request):
    
    currentUser = int(authenticated_userid(request))
    rankWeight = None #TODO
    topic_id = request.POST['topic']
    
    newPost = Post(currentUser,rankWeight,topic_id)
    DBSession.add(newPost)
    DBSession.flush()
    
    contentTitles = []
    contentURLs = []
    for key, value in request.POST.iteritems():
        if key == "title" and value != "":
            contentTitles.append(value)
        elif key == "URL" and value != "":
            contentURLs.append(value)
    
    contents = []
    for title,URL in zip(contentTitles,contentURLs):
        contentType = "LINK"  # TODO
        
        newContent = Content(title,URL,contentType,newPost.id)
        DBSession.add(newContent)
        DBSession.flush()
        
        contents.append(row2dict(newContent))
    
    post = {}
    post['post'] = row2dict(newPost)
    post['contents'] = contents
    
    return {'post' : post}

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


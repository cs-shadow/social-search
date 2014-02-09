from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.security import authenticated_userid

from models import DBSession,Topic,Badge
from ..users.models import User,UserFollowedTopic
from ..util import getTimeEpoch,row2dict

from sqlalchemy import and_


@view_config(route_name='topicAdd',
             renderer='json',
             request_method='POST')
def topicAdd(request):
    return{}
    
    
@view_config(route_name='topicGet',
             renderer='json',
             request_method='GET')
def topicGet(request):
    
    topicId = int(request.matchdict['topic_id'])
    
    return{}
    

@view_config(route_name='topicFollow',
             renderer='json',
             request_method='POST')
def topicFollow(request):
    
    currentUser = int(authenticated_userid(request))
    topicId = int(request.matchdict['topic_id'])
    
    followed = DBSession.query(UserFollowedTopic).\
    filter(and_(UserFollowedTopic.topic_id == topicId,UserFollowedTopic.user_id == currentUser)).\
    first()
    
    if followed != None:
        return {'status' : 'Already Following'}
    
    newTopicFollow = UserFollowedTopic(topicId,currentUser)
    DBSession.add(newTopicFollow)
    DBSession.flush()
    
    return {'status' : 'Follwed'}
    
@view_config(route_name='topicUnfollow',
             renderer='json',
             request_method='POST')
def topicUnfollow(request):
    
    currentUser = int(authenticated_userid(request))
    topicId = int(request.matchdict['topic_id'])
    
    followed = DBSession.query(UserFollowedTopic).\
    filter(and_(UserFollowedTopic.topic_id == topicId,UserFollowedTopic.user_id == currentUser)).\
    first()
    
    if followed == None:
        return {'status' : 'Not Following'}
    
    DBSession.delete(followed)
    DBSession.flush()
    DBSession.commit()
    
    return {'status' : 'Unfollowed'}
    
@view_config(route_name='topicDelete',
             renderer='json',
             request_method='GET')
def topicDelete(request):
    
    topicId = int(request.matchdict['topic_id'])
    
    return{}
        
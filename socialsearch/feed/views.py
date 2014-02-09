from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.security import authenticated_userid

from ..posts.models import Post,PostTag,PostLike,PostDislike,Content
from ..users.models import User,UserFollowedTopic
from ..tags.models import Topic
from ..models import DBSession
from ..util import getTimeEpoch,row2dict

from sqlalchemy import and_

@view_config(route_name='newsFeed',
             renderer='json',
             request_method='GET',
             )
def newsFeed(request):
    
    currentUser = int(authenticated_userid(request))
    offset = int(request.matchdict['offset'])
    postLimit = 20 # TODO
    
    userFollowedTopics = DBSession.query(UserFollowedTopic.topic_id)
    userTopics = []
    for topic in userFollowedTopics.all():
        userTopics.append(topic.topic_id)
        
    
    latestPosts = DBSession.query(Post).\
    filter(Post.topic_id.in_(userTopics)).\
    order_by(Post.time.desc()).\
    limit(postLimit).\
    offset(offset)
    
    
    posts = []
    for post in latestPosts.all():
        posts.append(row2dict(post))
    
    return {'posts' : posts}
    
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.security import authenticated_userid

from models import DBSession,Post,PostTag,PostLike,PostDislike,Content
from ..users.models import User
from ..tags.models import Topic
from ..util import getTimeEpoch,row2dict

from sqlalchemy import and_


@view_config(route_name='postAdd',
             renderer='json',
             request_method='POST')
def postAdd(request):
    
    currentUser = int(authenticated_userid(request))
    rankWeight = None #TODO
    pasteTitle = request.POST['paste_title']
    topic_id = request.POST['topic']
    
    newPost = Post(currentUser,rankWeight,topic_id,pasteTitle)
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


@view_config(route_name='postGet',
             renderer='json',
             request_method='GET',
             permission='__no_permission_required__')
def postGet(request):
    
    postId = int(request.matchdict['post_id'])
    
    dbPost = DBSession.query(Post).filter(Post.id == postId).first()
    if dbPost == None:
        return {'status' : '0'}
    
    contents = []
    postContents = DBSession.query(Content).filter(Content.post_id == postId)
    for content in postContents.all():
        contents.append(row2dict(content))
    
    post = {}
    post['post'] = row2dict(dbPost)
    post['contents'] = contents
    
    return {'status' : '1' , 'post' : post}


@view_config(route_name='postLike',
             renderer='json',
             request_method='GET')
def postLike(request):
    
    currentUser = int(authenticated_userid(request))
    postId = int(request.matchdict['post_id'])
    
    liked = DBSession.query(PostLike).\
    filter(and_(PostLike.post_id == postId,PostLike.user_id == currentUser)).\
    first()
    
    if liked != None:
        return {'status' : 'Already UpVoted'}
    
    newPostLike = PostLike(postId,currentUser)
    DBSession.add(newPostLike)
    DBSession.flush()
    
    return {'status' : 'UpVoted'}


@view_config(route_name='postDislike',
             renderer='json',
             request_method='GET')
def postDislike(request):
    
    currentUser = int(authenticated_userid(request))
    postId = int(request.matchdict['post_id'])
    
    disliked = DBSession.query(PostDislike).\
    filter(and_(PostDislike.post_id == postId,PostDislike.user_id == currentUser)).\
    first()
    
    if disliked != None:
        return {'status' : 'Already DownVoted'}
    
    newPostDislike = PostDislike(postId,currentUser)
    DBSession.add(newPostDislike)
    DBSession.flush()
    
    return {'status' : 'DownVoted'}


@view_config(route_name='postTagAdd',
             renderer='json',
             request_method='POST')
def postTagAdd(request):
    
    currentUser = int(authenticated_userid(request))
    postId = int(request.matchdict['post_id'])
    
    tagName = request.POST['tag_name']
        
    dbPostTag = DBSession.query(PostTag).\
    filter(and_(PostTag.post_id == postId,PostTag.tag_name == tagName)).\
    first()

    if dbPostTag != None:
        return {'status' : 'Tag Already Present'}

    newPostTag = PostTag(postId,tagName)
    DBSession.add(newPostTag)
    DBSession.flush()
	
    return {'status' : 'Tag Added'}

@view_config(route_name='postDelete',renderer='json')
def postDelete(request):
    return {}



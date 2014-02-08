from pyramid.response import Response
from pyramid.view import view_config, forbidden_view_config
from pyramid.security import remember,authenticated_userid, forget, Authenticated

from pyramid.httpexceptions import HTTPFound

import urllib2,json

from .models import DBSession
from .models import User
from ..util import row2dict

__dummyImage = "static/img/img-default-med.jpg"

def __getFacebookProfilePic(user_id,access_token):
    
    urlProfilePic = "https://graph.facebook.com/"
    urlProfilePic += user_id
    urlProfilePic += "/picture?type=large&redirect=false&access_token="
    urlProfilePic += access_token
        
    urlRequest = urllib2.Request(urlProfilePic)
    
    userData = urllib2.urlopen(urlRequest)
    userData = json.load(userData)
    
    urlPic = userData['data']['url']
    isSilhouette = str(userData['data']['is_silhouette'])
    
    if isSilhouette == 'true':
        return __dummyImage
    return urlPic


@view_config(
    context='velruse.AuthenticationComplete',
    renderer='blank.mako',
    permission='__no_permission_required__'
)
def login_complete_view(request):
    
    context = request.context
    result = {
        'provider_type': context.provider_type,
        'provider_name': context.provider_name,
        'profile': context.profile,
        'credentials': context.credentials,
    }
    
    email = result['profile']['verifiedEmail']
    
    dbFoundUser = DBSession.query(User.id).filter(User.email == email).first()
    
    if dbFoundUser == None:
        
        user_id = result['profile']['accounts'][0]['userid']
        domain = result['profile']['accounts'][0]['domain']
        access_token = result['credentials']['oauthAccessToken']
    
        provider_name = result['provider_name']
        
        about = None
        password = None
        profile_pic = None
    
        if provider_name == 'google':
            refresh_token = result['credentials']['oauthRefreshToken']
        
            urlRequest = urllib2.Request("https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token="+access_token)
        
            userData = urllib2.urlopen(urlRequest)
            userData = json.load(userData)
            
            try:
                profile_pic = userData['picture']
            except:
                profile_pic = __dummyImage
                
        
            given_name = userData['given_name']
            formatted = userData['name']
            family_name = userData['family_name']
            
        elif provider_name == 'facebook':
        
            given_name = result['profile']['name']['givenName']
            formatted = result['profile']['name']['formatted']
            family_name = result['profile']['name']['familyName']
        
            profile_pic = __getFacebookProfilePic(user_id,access_token)
        
            refresh_token = None
            
        dbFoundUser = User(given_name,formatted,family_name,
                     email,user_id,domain,access_token,refresh_token,
                     about,
                     password,profile_pic)
        
        request.session['user'] = row2dict(dbFoundUser)
        
        DBSession.add(dbFoundUser)
        DBSession.flush()

    headers = remember(request,dbFoundUser.id) 
    return HTTPFound(location = request.route_url('home'), headers = headers)

@view_config(route_name='logout')
def logout(request):
    
    currentUser = int(authenticated_userid(request))
    headers = forget(request)
    
    request.session.invalidate()
    return HTTPFound(location = request.route_url('home'), headers = headers)




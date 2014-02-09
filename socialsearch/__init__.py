from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Authenticated

from pyramid.session import UnencryptedCookieSessionFactoryConfig
import os
import logging

from .models import (
    DBSession,
    Base,
    )

here = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger(__name__)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    settings['mako.directories'] = os.path.join(here,'templates')

    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(settings=settings,root_factory='.models.RootFactory', session_factory=session_factory)
    
    """Velruse settings
    """
    config.include('velruse.providers.facebook')
    config.add_facebook_login_from_settings(prefix='velruse.facebook.')
    config.include('velruse.providers.google_oauth2')
    config.add_google_oauth2_login_from_settings(prefix='velruse.google.')
    

    authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.set_default_permission(Authenticated)

    config.add_static_view('static', 'static')
    config.add_static_view('attachment',os.path.join(here, 'static/attachments'))
    config.add_static_view('css',os.path.join(here, 'static/css'))
    config.add_static_view('js',os.path.join(here, 'static/js'))
    config.include('pyramid_chameleon')


    """ Routes Here """
    config.add_route('home', '/')
    config.add_route('profile', '/profile')
    config.add_route('about', '/about')
    config.add_route('contact', '/contact')
    config.add_route('terms', '/terms')
    config.add_route('team', '/team')
    
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    
    config.add_route('postAdd', '/post_add')
    config.add_route('postTagAdd', '/post_tag_add/{post_id}')
    config.add_route('postTagDelete', '/post_tag_delete/{post_id}/{tag_id}')
    config.add_route('postGet', '/post_get/{post_id}')
    config.add_route('postLike', '/post_like/{post_id}')
    config.add_route('postDislike', '/post_dislike/{post_id}')
    config.add_route('postDelete', '/post_delete/{post_id}')
    
    
    config.add_route('topicAdd', '/topic_add')
    config.add_route('topicGet', '/topic_get/{topic_id}')
    config.add_route('topicFollow', '/topic_follow/{topic_id}')
    config.add_route('topicUnfollow', '/topic_unfollow/{topic_id}')
    config.add_route('topicDelete', '/topic_delete/{topic_id}')
    
    config.add_route('topicFeed', '/topic_feed')
    config.add_route('newsFeed', '/news_feed/{offset}')
    
    config.add_route('search', '/search')
    
    
    config.scan()
    return config.make_wsgi_app()

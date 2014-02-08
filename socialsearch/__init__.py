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
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    
    
#     config.add_route('', '/post_add')
#     config.add_route('', '/post_like/{post_id}')
#     config.add_route('', '/post_dislike/{post_id}')
#     config.add_route('', '/post_delete/{post_id}')
#     
#     
#     config.add_route('', '/tag_add')
#     config.add_route('', '/tag_follow/{tag_id}')
#     config.add_route('', '/tag_unfollow/{tag_id}')
#     config.add_route('', '/tag_delete/{}')
    
    
    config.scan()
    return config.make_wsgi_app()

from pyramid.session import SignedCookieSessionFactory


def includeme(config):
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    config.set_session_factory(my_session_factory)

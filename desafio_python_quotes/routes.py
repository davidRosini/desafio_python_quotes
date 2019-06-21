def register_routes(config):
    config.add_route('home', '/')

    config.add_route('quotes', '/quotes')
    config.add_route('quote', '/quotes/{quote_number}')
    config.add_route('quote_random', '/quotes/random/')

    config.add_route('visits_session', '/visits')
    config.add_route('history_session', '/history')


def includeme(config):
    register_routes(config)

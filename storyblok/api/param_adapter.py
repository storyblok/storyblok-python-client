def body(token, options={}):
    params = options['query'] if 'query' in options else {}
    params['token'] = token

    return params

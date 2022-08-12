def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return [bytes(i+'\n') for i in environ['QUERY_STRING'].split('&')]
	

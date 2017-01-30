from django.http import HttpResponse

def index(request):
    html = "<h1>Hello, Ruskyhost!</h1><p>I'm Django application.</p>"
    return HttpResponse(html)
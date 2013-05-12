from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('example_app/index.html',
                              {'message': 'Hello world!'},
                              context_instance=RequestContext(request))

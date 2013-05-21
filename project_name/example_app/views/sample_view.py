from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from example_app.views.decorator import login_checker
from example_app import forms
from example_app.models.post_message import PostMessage


@login_checker
def index(request):
    post_message_form = forms.PostMessageForm()
    messageset = PostMessage.objects.all().order_by('-post_date')

    return render_to_response('example_app/index.html',
                              {'post_message_form': post_message_form,
                               'messageset': messageset},
                              context_instance=RequestContext(request))


@login_checker
def post(request):
    if request.method == 'POST':
        form = forms.PostMessageForm(request.POST, request.FILES)

        if form.is_valid():
            name = request.POST.get('name')
            message = request.POST.get('message')
            upload_file = request.FILES.get('upload_file', None)

            if not name:
                name = 'anonymous'

            if upload_file:
                content = upload_file.read()
            else:
                content = ''

            new_post = PostMessage(name=name, message=message, upload_file=content)
            new_post.save()

        return HttpResponseRedirect('/')

    else:
        raise Http404

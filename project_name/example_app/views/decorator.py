from django.template import RequestContext
from django.shortcuts import render_to_response
from example_app import forms


def login_checker(view_func):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated():
            login_form = forms.LoginForm()
            return render_to_response('example_app/login.html',
                                      {'login_form': login_form,
                                       'next': request.get_full_path(),
                                       'account_status': 'nologin'},
                                      context_instance=RequestContext(request))

        else:
            return view_func(request, *args, **kwargs)

    wrap.__doc__ = view_func.__doc__
    wrap.__name__ = view_func.__name__

    return wrap

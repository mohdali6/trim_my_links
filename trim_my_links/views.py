# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

import json

# Create your views here.

@ensure_csrf_cookie
def index(request):
	request.session.set_test_cookie()
	return render(request, 'trim_my_links/index.html')


def trim_link(request):
	if request.method == 'POST':
		print json.loads(request.body.decode('utf-8'))
		# ToDo
		return JsonResponse({'message': 'POST SERVED'})
	else:
		return JsonResponse({'message': "Oops! That didn't work!"})

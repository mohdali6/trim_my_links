# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db import IntegrityError
from .models import Link
import random
import string
import json
from django.core.serializers import serialize

# Create your views here.

@ensure_csrf_cookie
def index(request):
    request.session.set_test_cookie()
    return render(request, 'trim_my_links/index.html')


def trim_link(request, link_id=0):
    DOMAIN_NAME = 'https://example.com/'
    JSON_KEY_BIG_LINK = 'big_link'

    if request.method == 'GET':
        try:
            link = Link.objects.get(id=link_id)

            data = {
                "data": {
                    "id": link_id,
                    "trimmed_link": link.trimmed_link,
                    "original_link": link.original_link,
                    "timestamp": link.timestamp
                }
            }
            return JsonResponse(data)
        except Link.DoesNotExist:
            data = {
                "error": {
                    "code": 404,
                    "message": "Not found"
                }
            }
            return JsonResponse(data, status=404)

    elif request.method == 'POST':
        big_link = json.loads(request.body.decode('utf-8'))[JSON_KEY_BIG_LINK].strip()

        try :
            fetched_link = Link.objects.get(original_link=big_link)
            data = {
                "error": {
                    "code": 409,
                    "message": "Link already exists"
                }
            }
            return JsonResponse(data, status=409)
        except Link.DoesNotExist:
            pass

        while True:
            unique_str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
            new_trimmed_link = DOMAIN_NAME + unique_str

            try:
                fetched_trimmed_link = Link.objects.get(trimmed_link=new_trimmed_link)
            except Link.DoesNotExist:
                break

        link_obj = Link(
                trimmed_link = new_trimmed_link,
                original_link = big_link
            )
        link_obj.save()
        # ToDo


        return redirect('result/')

    else:
        return JsonResponse({'message': "Oops! That didn't work!"})

def redirect_to_result(request):
    return HttpResponse('ToDo')
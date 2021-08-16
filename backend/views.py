import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import News


def index(request):
    return render(request, "index.html", locals())


def json_view(request):
    resp = []
    for n in News.objects.all():
        resp.append(
            {
                "id": n.id,
                "school": n.school,
                "dep": n.dep,
                "category": n.category,
                "title": n.title,
                "url": n.url,
                "published": n.published,
                "created_at": str(n.created_at),
            }
        )
    return HttpResponse(json.dumps(resp), content_type="application/json")

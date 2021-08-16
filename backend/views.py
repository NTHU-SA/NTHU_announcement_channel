import json

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import News


def index(request):
    return render(request, "index.html", locals())


@csrf_exempt
def search(request):
    if request.method == "POST":
        print(request)
        keyword = json.loads(request.body)["keyword"]
        result = [
            {"title": i.title, "url": i.url}
            for i in News.objects.filter(
                Q(title__contains=keyword) | Q(category__contains=keyword)
            )
        ]
        return JsonResponse({"result": result})
    return JsonResponse({})


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

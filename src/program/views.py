from django.http import HttpResponse
import os
from django.conf import settings

#  NOTE: You can import from existing packages
#  but no new package can be added.


def status(request):
    return HttpResponse(status=200)


def main(request):
    return HttpResponse(
        "Tell me who to say hello? e.g. /sayHello/?name=alice", status=200
    )


def say_hello(request):
    if not request.GET.get("name", None):
        return HttpResponse(
            "Tell me who to say hello? e.g. /sayHello/?name=alice", status=200
        )
    return HttpResponse(f'<h1>Hello, {request.GET["name"]}</h1>', status=200)

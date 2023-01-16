from django_q.tasks import async_task
from django.http import JsonResponse

def index(request):
    async_task("myapp.tasks.foo", 3, hook="myapp.tasks.hook_after_foo")
    return JsonResponse({"msg":"Hello World."})
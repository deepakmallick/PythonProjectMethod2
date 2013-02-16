from django.http import HttpResponse

def hello(request):
    return HttpResponse("This is my 1st Web Page Created By Using Django")

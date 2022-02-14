from django.shortcuts import render


# Create your views here.

def message_views(request):
    return render(request, "message_form.html")

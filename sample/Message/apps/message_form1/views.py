from django.shortcuts import render
from apps.message_form1.models import Message


# Create your views here.

def message_views(request):
    if request.method == "POST":
        if request.POST.get("name"):
            message_data = Message()
            # message_data.name = request.POST.get("name")
            # message_data.email = request.POST.get("email")
            # message_data.address = request.POST.get("address")
            # message_data.message = request.POST.get("message")
            message_data.set_attrs(request.POST)
            message_data.save()
    return render(request, "message_form.html")


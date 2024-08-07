from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import NameForm
from django.urls import reverse

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["your_name"]
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
    else:
        form = NameForm()
    return render(request, "contacts/name.html", {"form": form})

def thanks(request, name):
    return HttpResponse(f"Obrigado {name}!")
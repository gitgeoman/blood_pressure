from django.shortcuts import render
from .services import FakeMeasurementsService
# Create your views here.

def list(request):
    ms = FakeMeasurementsService.list()

    return render(
        request, 
        "measurements/list.html",
        {"measurements": ms}
    )
def details(request, id): pass
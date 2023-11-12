from datetime import datetime
from django.shortcuts import render
from .services import JsonMeasurementService as service
# Create your views here.

def list(request):

    if request.method == "GET":
        print(request.GET)
   

    if request.method == "POST":
        print(request.POST)
        service.create(
            date=datetime.fromisoformat(request.POST.get("mes_date")),
            systolic=request.POST.get("mes_systolic"),
            diastolic=request.POST.get("mes_diastolic")
        )


    ms = service.list()

    return render(
        request, 
        "measurements/list.html",
        {"measurements": ms}
    )



def details(request, id): pass
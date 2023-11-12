from django.shortcuts import render
from .services import InMemoeryMeasurementService as service
# Create your views here.

def list(request):
    ms = service.list()

    if request.method == "GET":
        print(request.GET)
   

    if request.method == "POST":
        print(request.POST)
        service.create(
            date=request.POST.get("mes_date"),
            systolic=request.POST.get("mes_systolic"),
            diastolic=request.POST.get("mes_diastolic")
        )

    return render(
        request, 
        "measurements/list.html",
        {"measurements": ms}
    )



def details(request, id): pass
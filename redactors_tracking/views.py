from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from redactors_tracking.models import Redactor, Newspaper, Topic


@login_required
def index(request):
    """View function for the home page of the site."""

    num_drivers = Redactor.objects.count()
    num_cars = Newspaper.objects.count()
    num_manufacturers = Topic.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "redactors_tracking/index.html", context=context)

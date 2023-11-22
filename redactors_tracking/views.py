from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from redactors_tracking.models import Redactor, Newspaper, Topic


@login_required
def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topic = Topic.objects.count()

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topic": num_topic,
    }

    return render(request, "redactors_tracking/index.html", context=context)

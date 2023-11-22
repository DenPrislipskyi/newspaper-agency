from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    # paginate_by = 4


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("redactors_tracking:topic-list")
    template_name = "redactors_tracking/topic_form.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("redactors_tracking:topic-list")
    template_name = "redactors_tracking/topic_form.html"


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "redactors_tracking/topic_delete.html"
    success_url = reverse_lazy("redactors_tracking:topic-list")

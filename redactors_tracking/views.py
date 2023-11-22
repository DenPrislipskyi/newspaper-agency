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
    paginate_by = 4


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


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 4
    queryset = Newspaper.objects.all().select_related("topic")


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("redactors_tracking:newspaper-list")
    template_name = "redactors_tracking/newspaper_form.html"


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("redactors_tracking:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    template_name = "redactors_tracking/newspaper_delete.html"
    success_url = reverse_lazy("redactors_tracking:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 4


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    # form_class = RedactorUpdateForm
    success_url = reverse_lazy("redactors_tracking:redactor-list")
    fields = ("username", "first_name", "last_name", "redactor_id")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor

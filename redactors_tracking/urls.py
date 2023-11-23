from django.urls import path

from redactors_tracking.views import (index,
                                      TopicListView,
                                      TopicCreateView,
                                      TopicUpdateView,
                                      TopicDeleteView,
                                      NewspaperListView,
                                      NewspaperDetailView,
                                      NewspaperUpdateView,
                                      NewspaperCreateView,
                                      NewspaperDeleteView,
                                      RedactorListView,
                                      RedactorUpdateView,
                                      RedactorDetailView,
                                      RedactorCreateView,
                                      RedactorDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path("Topics/", TopicListView.as_view(), name="topic-list"),
    path("Topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("Topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("Topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete"),
    path("Newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("Newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("Newspapers/<int:pk>/detail", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("Newspapers/<int:pk>/update", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("Newspapers/<int:pk>/delete", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    path("Redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("Redactors/<int:pk>/update/", RedactorUpdateView.as_view(), name="redactor-update"),
    path("Redactors/<int:pk>/detail", RedactorDetailView.as_view(), name="redactor-detail"),
    path("Redactors/create", RedactorCreateView.as_view(), name="redactor-create"),
    path("Redactors/<int:pk>/delete", RedactorDeleteView.as_view(), name="redactor-delete"),

]

app_name = "redactors_tracking"

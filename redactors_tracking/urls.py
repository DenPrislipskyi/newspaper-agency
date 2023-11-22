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
                                      NewspaperDeleteView,)

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
]

app_name = "redactors_tracking"

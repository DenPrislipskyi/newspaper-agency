from django.urls import path

from redactors_tracking.views import (index,
                                      TopicListView,
                                      TopicCreateView,
                                      TopicUpdateView,
                                      TopicDeleteView,)

urlpatterns = [
    path("", index, name="index"),
    path("Topics/", TopicListView.as_view(), name="topic-list"),
    path("Topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("Topic/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("Topic/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete"),
]

app_name = "redactors_tracking"

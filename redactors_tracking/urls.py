from django.urls import path

from redactors_tracking.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "redactors_tracking"

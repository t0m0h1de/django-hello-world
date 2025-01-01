from django.urls import path

from . import views

urlpatterns = [
    path("/ready", views.readiness, name="readiness"),
    path("/live", views.liveness, name="liveness")
]
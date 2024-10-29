from django.urls import path

from crud.api import api


urlpatterns = [
    path('crudapi/', api.urls),
]

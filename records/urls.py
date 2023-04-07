from django.urls import path
from . import views 


urlpatterns = [
    path("records/<uuid:record_id>/", views.record_detail, name='record-detail')
]

from django.urls import path
from .views import *


urlpatterns = [

    path('receipt', receipt, name='receipts'),
    path('error_report', errorreport, name='error-report'),



]

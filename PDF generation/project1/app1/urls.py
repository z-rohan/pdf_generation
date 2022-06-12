from django.urls import path
from .views import *

urlpatterns=[
    path('al/',AddLaptopView,name="addlaptop_url"),
    path('sl/',ShowLaptopView,name="showlaptop_url"),
    path('pr/<int:id>/',ReportView,name="pdf_url"),
    path('ap/',AllReportView,name='allpdf_url')
]
"""Pbl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home'),
    path('hatchback/',views.hatchback,name='Hatchback'),
    path('sportsCars/',views.sportsCars,name='Sports'),
    path('sedanCars/',views.sedanCars,name='Sedan'),
    path('suvCars/',views.suvCars,name='SUV'),
    path('sedanCars/sedan/Mer',views.sedanMer,name='MerSe'),
    path('sedanCars/sedan/Maser',views.sedanMaser,name='MaserSe'),
    path('sedanCars/sedan/Aston',views.sedanAston,name='AstonSe'),
    path('sedanCars/sedan/Rolls',views.sedanRolls,name='RollSe'),
    path('sedanCars/sedan/Lexus',views.sedanLexus,name='LexSe'),
    path('suvCars/suv/Lambo',views.suvLambo,name='Lambosuv'),
    path('suvCars/suv/MaserSuv',views.suvMaser,name='Masersuv'),
    path('suvCars/suv/BMWsuv',views.suvBMW,name='BMWsuv'),
    path('suvCars/suv/MerSuv',views.suvMer,name='MerSuv'),
    path('suvCars/suv/Bentleysuv',views.Bentleysuv,name='BenSuv'),
    path('sportsCars/audi',views.Audisports,name='AudiSport'),
    path('sportsCars/ford',views.Fordsports,name='FordSport'),
    path('sportsCars/dodge',views.Dodgesports,name='DodgeSport'),
    path('sportsCars/Mlar',views.MlarSports,name='MlarSport'),
    path('sportsCars/Buga',views.BugaSports,name='BugaSport'),
    path('hatchback/Hatch/Audi',views.AudiHatch,name='AudiHatch'),
    path('hatchback/Hatch/BMW',views.BMWhatch,name='BMWhatch'),
    path('hatchback/Hatch/Skoda',views.SkodaHatch,name='SkodaHatch'),
    path('hatchback/Hatch/Cooper',views.CooperHatch,name='CopperHatch'),
    path('hatchback/Hatch/Country',views.CountryHatch,name='CountryHatch')
    
    
    
    
    

    
    
]

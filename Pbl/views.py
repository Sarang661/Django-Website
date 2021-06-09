from django.http import HttpResponse
from django.shortcuts import render,redirect


 

def home(request):
    return render(request,"home.html")
def hatchback(request):
    return render(request,"hatchback.html")
def x(request):
    return render(request,"try.html")
def sportsCars(request):
    return render(request, "sportsCars.html")
def sedanCars(request):
    return render(request,"sedan.html")
def suvCars(request):
    return render(request, "suv.html")
def sedanMer(request):
    return render(request, "Mercedes.html")
def sedanMaser(request):
    return render(request, "Maserati.html")
def sedanAston(request):
    return render(request, "Aston.html")
def sedanRolls(request):
    return render(request, "Rolls.html")
def sedanLexus(request):
    return render(request, "Lexus.html")
def suvLambo(request):
    return render(request, "Lambo.html")
def suvMaser(request):
    return render(request,"MaseratiSuv.html")
def suvBMW(request):
    return render(request,"BMW.html")
def suvMer(request):
    return render(request,"MercedesSuv.html")
def Bentleysuv(request):
    return render(request,"Bentley.html")
def Audisports(request):
    return render(request,"audi.html")
def Fordsports(request):
    return render(request, "ford.html")
def Dodgesports(request):
    return render(request, "dodge.html")
def MlarSports(request):
    return render(request, "Mlar.html")
def BugaSports(request):
    return render(request, "Buggati.html")
def AudiHatch(request):
    return render(request,"AudiHatch.html")
def BMWhatch(request):
    return render(request, "HatchBMW.html")
def SkodaHatch(request):
    return render(request, "Skoda.html")
def CooperHatch(request):
    return render(request, "Cooper.html")
def CountryHatch(request):
    return render(request, "Country.html")



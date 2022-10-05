from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html", {"name": "Agam"})


# Function to add two numbers and send result to results page
def add(request):

    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])

    sum = val1 + val2

    return render(request, "result.html", {"result": sum})

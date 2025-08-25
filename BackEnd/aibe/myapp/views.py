from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

def chatbot(request):
    print( request.method)  # debug line
    if request.method == "POST":
        user_query = request.POST.get("query")
        print( user_query)


    return render(request, "myapp/index.html")

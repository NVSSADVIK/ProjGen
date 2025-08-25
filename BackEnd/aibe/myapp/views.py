from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from genai import ProjGen

from pathlib import Path

# BASE_DIR usually points to your Django project folder (ProjGen/BackEnd/aibe)
BASE_DIR = Path(__file__).resolve().parent.parent  # adjust if needed

# PROJECT_FOLDER = ProjGen folder (root of your repo)
PROJECT_FOLDER = BASE_DIR.parent.parent  # climbs up two levels from BASE_DIR

cb = ProjGen()
cb.load_api_key(PROJECT_FOLDER / ".api_key.txt")
cb.start_chatbot()

def chatbot(request):
    print(request.method)  # debug line
    if request.method == "POST":
        user_query = request.POST.get("query")
        print(user_query)
        response = cb.send_message(user_query)
        cb.print_fmt_response(response)


    return render(request, "myapp/index.html")

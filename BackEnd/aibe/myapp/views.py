from django.shortcuts import render
from django.http import JsonResponse
from genai import ProjGen
from pathlib import Path

# Setup chatbot globally so all requests can use it
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_FOLDER = BASE_DIR.parent.parent

cb = ProjGen()
cb.load_api_key(PROJECT_FOLDER / ".api_key.txt")
cb.start_chatbot()

def chatbot(request):
    if request.method == "POST":
        user_query = request.POST.get("query")
        print("User:", user_query)

        # Generate bot reply
        response = cb.send_message(user_query)
        cb.print_fmt_response(response)

        # Return JSON for frontend
        return JsonResponse({"response": response})

    # Only render template on GET
    return render(request, "myapp/index.html")

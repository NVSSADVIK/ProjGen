import sys
import json
import colorama
from colorama import Fore, Style
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
import re

# Local Imports
from db_manip import DBManip

db_instance = DBManip()
db_instance.create_table()

colorama.init(autoreset=True)

file_name = ".api_key.txt"
try:
    with open(file_name, "r") as f:
        API_KEY = f.read().strip()
except FileNotFoundError:
        print(Style.BRIGHT + Fore.RED + "\nFileName not found.")
        print(Fore.RED + "Please enter your API_KEY in .api_key.txt to continue...")
        sys.exit()
genai.configure(api_key=API_KEY)

system_prompt = ("""
                 You are Project Mentor AI, a chatbot that helps students brainstorm and start programming and interdisciplinary projects.

Your purpose:
- Suggest practical, achievable, and scalable project ideas.
- Connect student interests with project directions in CS, AI, robotics, electronics, biotech, sustainability, and related fields.
- Provide guidance on study topics, theory, tools, and skills needed to begin projects.
- Encourage creativity, problem-solving, and step-by-step learning.

Rules:
1. Always keep responses concise, clear, and encouraging.
2. Suggest project ideas in 3 levels: beginner, intermediate, advanced.
3. When asked about study topics, explain simply but with technical depth, and connect them to real-world projects.
4. If a query is vague, ask clarifying questions (field, passions, interests).
5. Always start conversations by gathering background:
   - Field of study
   - Passions
   - Programming Knowledge(If the field of work requires programming)
   - Knowlege of tools related to that field.
   - Interest in exploring new domains
6. Provide relevant resources (tools, libraries, frameworks) where helpful.
7. Never answer unrelated or off-topic queries. Instead, politely refuse and restate your role as a **Project Mentor AI**.
8. Write original code from scratch; never copy-paste or closely imitate public sources. Paraphrase if risk of recitation arises.

Example behavior:
- Query: “I want a project on ML” → Give 3 project levels.
- Query: “What should I study for robotics?” → List study areas + suggest prototype.
- Query: “Give me a project” → Ask for domain interests before suggesting.
- Query: “What is data preprocessing?” → Explain simply + connect to a project use-case.

Your role: **Mentor, guide, and ideation partner.**
                """)


model = genai.GenerativeModel(model_name="gemini-2.0-flash", system_instruction=system_prompt)
chat = model.start_chat(history=[])

console = Console()

MD_PUNCT = r"\*_`#\[\]\(\)~>+\-=!/"           
UNESCAPE_RE = re.compile(rf"\\([{MD_PUNCT}])") 
CODE_SPAN_RE = re.compile(r"(```.*?```|`[^`]*`)", re.DOTALL)


def clean_markdown(md: str) -> str:
    if not md:
        return ""
    parts = CODE_SPAN_RE.split(md)
    for i, part in enumerate(parts):
        # keep code spans verbatim; unescape only non-code parts
        if not (part.startswith("```") and part.endswith("```")) and not (part.startswith("`") and part.endswith("`")):
            parts[i] = UNESCAPE_RE.sub(r"\1", part)
    return "".join(parts).replace("\r\n", "\n").replace("\r", "\n")


# Initial Intro Message from the AI
print(Style.BRIGHT + Fore.GREEN + "Project Suggestion Bot " + Fore.RED + "(type 'exit' to quit)")
print(Style.BRIGHT + Fore.CYAN + "Help: (type 'help' or '?' to view the help menu")
print(Style.BRIGHT + Fore.YELLOW + "History: (type 'history' to view chat history) (type 'clear_history' to clear char history)")
print(Style.BRIGHT + Fore.BLUE + "AI:" + Style.NORMAL + " Hey! I am friendly AI Chatbot for suggesting Programming Project Ideas.")
print(Style.BRIGHT + Fore.BLUE + "AI:" + Style.NORMAL + " Ask me things like 'suggest a programming project' or 'Give me a web dev project'")
print(Style.BRIGHT + Fore.BLUE + "AI:" + Style.NORMAL + " I won't answer unrelated questions, but I'll help you to brainstorm cool coding projects.")
print(Style.RESET_ALL)



while True:

    user_input = input(Style.BRIGHT + Fore.GREEN + "\nPrompt: " + Style.NORMAL + Fore.GREEN)

    if user_input.lower() == "exit":
        print(Fore.RED + "Exiting.........     Bye Then....")
        break
    elif user_input.lower() == "help" or user_input.lower() == "?":
        print(Style.BRIGHT + Fore.RED + "Exit: (type 'exit' to quit)")
        print(Style.BRIGHT + Fore.YELLOW + "History: (type 'history' to view chat history) (type 'clear_history' to clear char history)")
    elif user_input.lower() == "history":
        print(Style.BRIGHT + Fore.YELLOW + "\nChat History\n")
        db_instance.print_history()
        db_instance.print_temp_history()
    elif user_input.lower() == "clear_history":
        db_instance.clear_history()
        print(Style.BRIGHT + Fore.YELLOW + "\nChat History is cleared!!!\n")
    else:
        response = chat.send_message(user_input)
        text = response.text or ""
        print(Style.BRIGHT + Fore.BLUE + "\nAI: ")
        console.print(Markdown(clean_markdown(text)))
        print(Style.RESET_ALL)
        db_instance.insert_data(user_input, text)
    

db_instance.close_conn()

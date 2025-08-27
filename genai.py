# Imports
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

class ProjGen:
    def __init__(self):
        self.API_KEY = None

        self.db = DBManip()
        self.db.create_table()

        colorama.init(autoreset=True)

        self.model = None
        self.chat = None

        self.console = Console()
        self.MD_PUNCT = r"\*_`#\[\]\(\)~>+\-=!/"           
        self.UNESCAPE_RE = re.compile(rf"\\([{self.MD_PUNCT}])") 
        self.CODE_SPAN_RE = re.compile(r"(```.*?```|`[^`]*`)", re.DOTALL)


    def load_api_key(self, file_name):
        try:
            with open(file_name, "r") as f:
                self.API_KEY = f.read().strip()
        except FileNotFoundError:
                print(Style.BRIGHT + Fore.RED + "\nFileName not found.")
                print(Fore.RED + "Please enter your API_KEY in .api_key.txt to continue...")
                print(Style.RESET_ALL)
                sys.exit()

    def start_chatbot(self):
        genai.configure(api_key=self.API_KEY)
        
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
        
        
        self.model = genai.GenerativeModel(model_name="gemini-2.0-flash", system_instruction=system_prompt)
        self.chat = self.model.start_chat(history=[])
    
    def clean_markdown(self, md: str) -> str:
        if not md:
            return ""
        parts = self.CODE_SPAN_RE.split(md)
        for i, part in enumerate(parts):
            # keep code spans verbatim; unescape only non-code parts
            if not (part.startswith("```") and part.endswith("```")) and not (part.startswith("`") and part.endswith("`")):
                parts[i] = self.UNESCAPE_RE.sub(r"\1", part)
        return "".join(parts).replace("\r\n", "\n").replace("\r", "\n")
    
    

    def display_intro(self):
        # Initial Intro Message from the AI
        print(Style.BRIGHT + Fore.GREEN + "ProjGen - AI Project Ideation Assistant " + Fore.RED + "(type 'exit' to quit)")
        print(Style.BRIGHT + Fore.CYAN + "Help: (type 'help' or '?' to view the help menu)")
        print(Style.BRIGHT + Fore.YELLOW + "History: (type 'history' to view chat history) (type 'clear_history' to clear chat history)")
        print(Style.BRIGHT + Fore.BLUE + "AI:" + Style.NORMAL + " Hello! I'm ProjGen, powered by Gemini Flash 2.0.")
        print(Style.BRIGHT + Fore.BLUE + "AI:" + Style.NORMAL + " I help students discover exciting programming projects tailored to their interests.")
        print(Style.BRIGHT + Fore.BLUE + "AI:" + Style.NORMAL + " Ask me for project ideas in any domain - Web Dev, Mobile Apps, AI/ML, Games & more!")
        print(Style.BRIGHT + Fore.BLUE + "AI:" + Style.NORMAL + " I focus on programming projects, so let's brainstorm something amazing!")
        print(Style.RESET_ALL)
        
    def send_message(self, user_input):
        response = self.chat.send_message(user_input)
        self.db.insert_message(user_input, response.text or "")
        return response.text or ""
    def print_fmt_response(self, response):

        self.console.print(Markdown(self.clean_markdown(response)))
    
    def main_loop(self):
        while True:
            user_input = input(Style.BRIGHT + Fore.GREEN + "\nPrompt: " + Style.NORMAL + Fore.GREEN)
        
            if user_input.lower() == "exit":
                print(Fore.RED + "Exiting.........     Bye Then....")
                break
            elif user_input.lower() == "help" or user_input.lower() == "?":
                print(Style.BRIGHT + Fore.RED + "Exit: (type 'exit' to quit)")
                print(Style.BRIGHT + Fore.YELLOW + "History: (type 'history' to view chat history) (type 'clear_history' to clear chat history)")
            elif user_input.lower() == "history":
                print(Style.BRIGHT + Fore.YELLOW + "\nChat History\n")
                self.db.print_history()
            elif user_input.lower() == "clear_history":
                self.db.clear_history()
                print(Style.BRIGHT + Fore.YELLOW + "\nChat History is cleared!!!\n")
            else:
                response = self.send_message(user_input)
                print(Style.BRIGHT + Fore.BLUE + "\nAI: ")
                self.console.print(Markdown(self.clean_markdown(response)))
                print(Style.RESET_ALL)
                self.db.insert_message(user_input, response)
        self.db.close_conn()

def main():
    chatbot = ProjGen()
    chatbot.load_api_key("./.api_key.txt")
    chatbot.start_chatbot()
    chatbot.display_intro()
    chatbot.main_loop()

if __name__ == "__main__":
    main()

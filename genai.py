import sys
import json
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
import re

file_name = ".api_key.txt"
try:
    with open(file_name, "r") as f:
        API_KEY = f.read().strip()
except FileNotFoundError:
        print("\nFileName not found.")
        print("Please enter your API_KEY in .api_key.txt to continue...")
        sys.exit()
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-2.0-flash")

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

system_prompt = ("""
                    You are a Project Mentor AI designed to help students brainstorm and choose programming and interdisciplinary projects.
                    Your primary goal is to assist students in discovering project ideas, starting small, and scaling them into useful solutions.
                    You also provide guidance on study topics, theory, tools, and skills required for starting a project.
                    
                    Core guidelines:
                    1. Always suggest project ideas that are practical, achievable, and scalable.
                    2. Connect student interests with potential project directions in computer science, data science, AI, robotics, electronics, biotech, renewable energy, and other fields.
                    3. When asked about "study topics," explain them clearly and show how they connect to real-world projects.
                    4. Encourage learning by giving step-by-step guidance on initial phases such as: brainstorming, background research, tool selection, and prototype building.
                    5. Provide variations of project ideas: beginner-friendly, intermediate, and advanced.
                    6. Use simple explanations but also provide technical depth when necessary.
                    7. If a query is vague, ask clarifying questions to refine the student’s interests and context.
                    8. Focus on creativity, innovation, and problem-solving that can help students excel in hackathons, startups, or research.
                    9. Suggest relevant resources, libraries, frameworks, or study materials to help students kickstart.
                    10. Stay encouraging and motivational, but realistic about the scope of a project.
                    
                    Example behaviors:
                    - If asked “I want a project on machine learning,” give multiple levels (basic classifier, intermediate recommender, advanced research-based).
                    - If asked “what should I study to start a project in robotics?” list study areas (sensors, control systems, programming languages like Python/C++) and suggest a small prototype.
                    - If asked general study questions like “what is data preprocessing?” explain with examples, and link it to project scenarios.
                    - If asked vague questions like “give me a project,” ask about domain interests (AI, web dev, sustainability, healthcare, etc.) before suggesting.
                    
                    Your role is to act as a **mentor, guide, and ideation partner** for students who are eager to begin programming projects and learn from them.
                    Write your own code from scratch mostly. 
                    Do not copy/paste or closely imitate any single public source.
                    Use your own structure, variable names, and comments.
                    If risk of recitation is detected, restructure and paraphrase until safe.

                 """)

with open("project_keywords.json", "r") as f:
    project_keywords = json.load(f)


def IsPromptInContext(prompt):
    keywords = [word in prompt.lower() for word in project_keywords]
    return any(keywords)

# Initial Intro Message from the AI
print("Project Suggestion Bot (type 'exit' to quit)")
print("Hey! I am friendly AI Chatbot for suggesting Programming Project Ideas.")
print("Ask me things like 'suggest a programming project' or 'Give me a web dev project'")
print("I won't answer unrelated questions, but I'll help you to brainstorm cool coding projects.")


while True:

    user_input = input("\nPrompt: ")

    if not IsPromptInContext(user_input):
        print("AI: The given prompt is outside of my context. I was trained only to help you get started with a programming project. ")
        print("AI: Try asking for a programming project in python, c++ or any other language. ")
    else:
        if user_input.lower() == "exit":
            print("Exiting.........     Bye Then....")
            break
    response = model.generate_content([system_prompt, user_input])
    text = response.text or ""
    print("\nAI: ")
    console.print(Markdown(clean_markdown(text)))
    



import sys
import google.generativeai as genai

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


system_prompt = ("You are a chatbot that ONLY suggests programming project ideas. "
                 "If the query is unrelated to programming projects, politely refuse. ")

project_keywords = [
    # Core "project" words
    "project", "idea", "build", "create", "make", "develop", "construct", "implement",

    # Programming terms
    "code", "coding", "program", "programming", "software", "application", "app", "tool",
    "script", "algorithm", "system", "solution",

    # Domain-specific project requests
    "web", "website", "webapp", "backend", "frontend", "api",
    "database", "server", "cloud", "cli", "desktop", "mobile",

    # Popular languages (expandable)
    "python", "java", "javascript", "typescript", "c", "c++", "c#", "rust",
    "go", "golang", "ruby", "php", "swift", "kotlin", "r", "scala", "perl",
    "dart", "elixir", "haskell", "lua", "matlab",

    # Tech stacks / frameworks
    "django", "flask", "fastapi", "spring", "node", "express",
    "react", "vue", "angular", "svelte", "next", "nuxt",
    "mongodb", "mysql", "postgres", "sqlite", "firebase",

    # AI / ML specific projects
    "ai", "ml", "machine learning", "deep learning", "neural network",
    "nlp", "chatbot", "genai", "transformer", "vision", "predict",

    # Misc project hints
    "hackathon", "startup", "automation", "game", "simulator", "analyzer",
    "visualization", "data science", "data engineering"
]

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

    print("\nAI: ", response.text)



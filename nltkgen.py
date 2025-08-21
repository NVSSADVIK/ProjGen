from nltk.corpus import wordnet as wn
import json

def create_wordlist(seed):
    keywords = set(seed)
    output_list = list(seed)
    for word in keywords:
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                candidate = lemma.name().replace("_", " ")
                if candidate not in output_list:
                    output_list.append(candidate)
    return output_list

seed = [
    # Core project actions
    "project", "idea", "build", "create", "make", "develop", "programming",
    "software", "app", "tool", "automation", "system", "simulation", "model",
    "design", "analysis", "experiment", "prototype", "implementation",
    "deployment", "framework", "architecture", "workflow", "pipeline",
    "integration", "optimization", "scalability", "efficiency", "usability",
    "testing", "debugging", "validation", "verification", "iteration",
    "collaboration", "documentation", "planning", "execution",

    # Academic / research-related
    "thesis", "dissertation", "publication", "conference", "journal",
    "poster", "seminar", "workshop", "presentation", "literature review",
    "case study", "field study", "survey", "hypothesis", "methodology",
    "evaluation", "findings", "results", "discussion", "conclusion",

    # Fields of study
    "computer science", "data science", "ai", "machine learning",
    "deep learning", "robotics", "cybersecurity", "blockchain",
    "biotechnology", "bioinformatics", "genetics", "nanotech",
    "neuroscience", "cognitive science", "mechanical", "civil",
    "electrical", "electronics", "chemical", "physics", "mathematics",
    "statistics", "astronomy", "astrophysics", "quantum", "chemistry",
    "biology", "ecology", "agriculture", "oceanography", "geology",
    "meteorology", "environmental", "sustainability", "renewable",
    "climate", "energy", "smart grid", "hydrogen", "solar", "wind",

    # Scenarios / contexts
    "real world", "problem solving", "scenario", "industry", "startup",
    "hackathon", "research", "innovation", "entrepreneurship",
    "business plan", "incubation", "accelerator", "pitching",
    "funding", "crowdfunding", "investment", "mentorship",
    "collaboration", "open source", "community", "competition",

    # Tech trends
    "iot", "cloud", "edge computing", "big data", "data mining",
    "data visualization", "natural language processing",
    "computer vision", "recommendation system", "digital twin",
    "smart cities", "metaverse", "wearables", "3d printing",
    "autonomous vehicles", "drones", "biometrics", "cryptography",
    "vr", "ar", "xr", "mixed reality", "quantum computing",

    # Soft skills / process
    "brainstorming", "creativity", "innovation", "critical thinking",
    "problem analysis", "strategy", "roadmap", "sprint", "agile",
    "scrum", "kanban", "milestone", "goal", "objective", "task",
    "deadline", "deliverable", "outcome", "impact", "vision"
]


project_keywords = create_wordlist(seed)

with open("project_keywords.json", "w") as f:
    json.dump(project_keywords, f)


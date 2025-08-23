# ProjGen

**ProjGen** is a **Simple Generative AI Chat Bot** designed to help students in colleges and universities kickstart projects in their field of interest.  

This project runs locally on your machine but **connects to Google’s cloud-based Gemini Flash 2.0 model** through the `google.generativeai` library. All interactions are powered by **Gemini Flash 2.0**, giving you fast, context-aware, and intelligent project ideation support.  

---

## API Key Setup  

This project requires a valid **Google API Key** to access Gemini models.  

1. Obtain your API Key from **Google AI Studio**.  
2. Create a file named `.api_key.txt` in the project’s root directory.  
3. Paste your API Key inside this file **without adding any extra text, spaces, or lines**.  

Example:  

```
AIzaSyD9-your-api-key-here
```

---

## Required Libraries  

Make sure you have the following Python libraries installed before running the project:  

- `sys`  
- `json`  
- `colorama`  
- `google.generativeai`  
- `rich`  
- `re`  
- `sqlite3`

Install them using:  

```bash
pip install colorama google-generativeai rich
```

---

## Running the Project  

After setting up dependencies and saving your API Key, run the chatbot(CLI Version).

```bash
python genai.py
```

---

## Features  

- **Project Ideation:** Generate project topics tailored to your chosen domain.  
- **Gemini Flash 2.0 Powered:** Uses Google’s cloud-based AI for high-quality responses.  
- **Local Execution with Cloud Intelligence:** Runs from your machine, connects securely to Gemini API.  
- **Enhanced Console Experience:** Clean and colorful output using `colorama` + `rich`.  
- **Chat History:** Storage of Chat History to enhance the User Experience to provide Personalized Results.

---

## Notes  

- Keep your `.api_key.txt` private. Do **not** share or push it to GitHub.  
- Internet connection is required since ProjGen depends on Google’s Gemini cloud API.  


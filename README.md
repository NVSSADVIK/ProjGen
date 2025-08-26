# ProjGen
**ProjGen** is a **Simple Generative AI Chat Bot** designed to help students in colleges and universities kickstart projects in their field of interest.  
This project runs locally on your machine but **connects to Google's cloud-based Gemini Flash 2.0 model** through the `google.generativeai` library. All interactions are powered by **Gemini Flash 2.0**, giving you fast, context-aware, and intelligent project ideation support.  

ProjGen offers both **CLI (Command Line Interface)** and **Web Interface** options to suit different user preferences.

---

## Project Structure

The following shows the key files and folders that are modifiable by the user:

```
ProjGen/
├── BackEnd/
│   └── aibe/
│       ├── aibe/
│       │   └── settings.py          # Django project settings
│       ├── manage.py                # Django management script
│       └── myapp/
│           ├── static/
│           │   └── myapp/
│           │       ├── script.js    # Frontend JavaScript
│           │       └── style.css    # Frontend styling
│           ├── templates/
│           │   └── myapp/
│           │       └── index.html   # Main web interface template
│           ├── urls.py              # URL routing for the web app
│           └── views.py             # Connects genai.py functions with Backend and Frontend
├── genai.py                         # Main CLI chatbot and core AI functions
├── .history.db                      # SQLite database for chat history
├── .api_key.txt                     # Your Google API Key (create this file)
└── db_manip.py                      # Database manipulation functions
```

**Note:** The `views.py` file serves as the bridge that connects the core AI functions in `genai.py` with both the Django backend and frontend interface.

---

## API Key Setup  
This project requires a valid **Google API Key** to access Gemini models.  
1. Obtain your API Key from **Google AI Studio**.  
2. Create a file named `.api_key.txt` in the project's root directory.  
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
- `django`

Install them using:  
```bash
pip install colorama google-generativeai rich django
```

---

## Running the Project  

### CLI Version (Command Line Interface)
After setting up dependencies and saving your API Key, run the chatbot in CLI mode:
```bash
python genai.py
```

### Web Interface (Django)
To run the web-based interface:
1. Navigate to the Django project directory:
   ```bash
   cd BackEnd/aibe
   ```
2. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
3. Open your web browser and go to `http://127.0.0.1:8000/`

---

## Features  
- **Dual Interface Options:** Choose between CLI and web-based interfaces.
- **Project Ideation:** Generate project topics tailored to your chosen domain.  
- **Gemini Flash 2.0 Powered:** Uses Google's cloud-based AI for high-quality responses.  
- **Local Execution with Cloud Intelligence:** Runs from your machine, connects securely to Gemini API.  
- **Enhanced Console Experience:** Clean and colorful output using `colorama` + `rich` (CLI version).
- **Modern Web Interface:** User-friendly web interface with responsive design (Web version).
- **Chat History:** Storage of Chat History to enhance the User Experience to provide Personalized Results.

---

## Notes  
- Keep your `.api_key.txt` private. Do **not** share or push it to GitHub.  
- Internet connection is required since ProjGen depends on Google's Gemini cloud API.
- Both CLI and web versions can be used independently based on your preference.
- The web interface provides a more interactive and visually appealing experience.

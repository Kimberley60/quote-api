# 🧾 Building a Simple Quote API with Flask – Beginner Guide

---

## 1. 🎯 Title & Objective

**Technology Chosen:** Flask (Python Web Framework)

**Why Flask?**  
Flask is lightweight, easy to learn, and ideal for beginners building APIs quickly.

**End Goal:**  
To build a simple REST API that:
- Retrieves quotes
- Adds new quotes
- Can be tested using Postman

---

## 2. 📌 Quick Summary of the Technology

Flask is a lightweight Python framework used to build web applications and APIs.

**Where it is used:**
- Backend systems
- REST APIs
- Microservices

**Real-world example:**  
Startups often use Flask to quickly build backend services for web and mobile apps.

---

## 3. ⚙️ System Requirements

- OS: Windows / Linux / Mac
- Python 3.x
- pip (Python package manager)
- Code Editor: PyCharm or VS Code
- Postman (API testing tool)

---

## 4. 🚀 Installation & Setup Instructions

```bash
# Create project folder
mkdir quote-api
cd quote-api

# Create virtual environment
python -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate

# Install Flask
pip install flask

# Save dependencies
pip freeze > requirements.txt

# Run the app
python app.py

5. 🧪 Minimal Working Example

This API provides:

GET /quotes → returns all quotes
GET /quotes/random → returns a random quote
POST /quotes → adds a new quote
Example POST Request
{
  "text": "Learning APIs step by step"
}
Expected Response
{
  "id": 3,
  "text": "Learning APIs step by step"
}


6. 🤖 AI Prompt Journal
Prompt 1

"Create a simple Flask API with GET and POST endpoints"

Outcome:
Generated base API structure.

Evaluation:
Helpful for quick setup.

Prompt 2

"Fix 400 Bad Request error in Flask POST request"

Outcome:
Learned how to handle JSON using:

request.get_json(silent=True)

Evaluation:
Very useful for debugging.

Prompt 3

"How to test a Flask API using Postman"

Outcome:
Learned how to:

Send GET requests
Send POST requests with JSON

Evaluation:
Improved API testing understanding.

7. ⚠️ Common Issues & Fixes
1. 400 Bad Request

Cause: Missing or invalid JSON
Fix: Set Body → raw → JSON in Postman

2. 405 Method Not Allowed

Cause: Wrong HTTP method
Fix: Use POST instead of GET

3. Flask Not Installed

Cause: Missing dependency
Fix:

pip install flask
4. Duplicate Quotes

Cause: No validation
Fix: Added duplicate check in API

🧠 Observations & Insights
Data is stored in memory (not permanent)
Data resets when server restarts
Duplicate prevention improved API quality

This shows how testing helps improve API reliability.

🔁 Peer Testing

A peer tested the project and initially had issues activating the virtual environment.

Fix:
Improved setup instructions.

Result:
Project became easier to replicate.

🧪 API Testing with Postman
GET /quotes

POST /quotes

📚 References
Flask Official Documentation
Postman Documentation
StackOverflow
YouTube Tutorials
🧠 Reflection

Using AI significantly improved my learning speed by helping debug errors and understand API concepts faster.





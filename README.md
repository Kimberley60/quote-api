# Quote API (Flask)

## 📌 Project Overview
This project is a simple REST API built using Flask. It allows users to retrieve and add quotes. The API is tested using Postman and demonstrates basic backend development concepts.

## 🎯 Objective
To learn how to:
- Build a REST API using Flask
- Test endpoints using Postman
- Document setup and usage clearly for replication

---

## ⚙️ Tech Stack
- Python 3
- Flask
- Postman (API testing)

---

## 📁 Project Structure

- quote-api/
- │
- ├── app.py
- ├── requirements.txt
- ├── README.md
- ├── .gitignore
- └── docs/
- ├── toolkit.md
- └── images/


---

## 🚀 Setup Instructions

1. Clone the repository:
   git clone https://github.com/Kimberley60/quote-api.git

   cd quote-api


2. Create virtual environment:

python -m venv .venv


3. Activate environment:

.venv\Scripts\activate


4. Install dependencies:

pip install -r requirements.txt


5. Run the application:

python app.py


---

## 🌐 API Endpoints

### GET /quotes
Returns all quotes

### GET /quotes/random
Returns a random quote

### POST /quotes
Adds a new quote

#### Example Request:

POST /quotes
Content-Type: application/json


```json
{
  "text": "Learning APIs step by step"
}
Example Response:

{
  "id": 3,
  "text": "Learning APIs step by step"
}

🧪 Testing the API

The API was tested using Postman.

Example:
GET request to /quotes returns all quotes
POST request adds a new quote
⚠️ Notes
Data is stored in memory (not persistent)
Duplicate quotes are prevented using validation logic
📚 Documentation

Detailed setup, testing steps, AI prompts, and reflections are included in:

docs/toolkit.md
👩‍💻 Author

JANET KIMBERLEY


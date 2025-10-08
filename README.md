🧠 Smart Content Moderator API

A FastAPI-based AI service that analyzes user-submitted content for inappropriate material.

📘 Overview

The Smart Content Moderator API is a backend service built with FastAPI that detects and classifies inappropriate or harmful content (text or images).
It uses OpenAI GPT models for text moderation, stores results in a SQLite database, and provides user-specific moderation analytics.

🔹 This version includes core functionality up to result storage.
(Notification and Docker modules are optional extensions.)

🚀 Features

Analyze text or image URLs for toxicity, spam, or harassment

Store all moderation results and request logs in a SQLite database

Retrieve moderation summaries by user email

Built using FastAPI + SQLAlchemy (async)

Extensible for email/Slack notifications (future scope)

🏗️ Tech Stack
Component	Technology Used
Framework	FastAPI (Python 3.9+)
Database	SQLite (via SQLAlchemy ORM)
AI Model	OpenAI GPT-4 / GPT-3.5
Environment	Virtualenv / Conda
Server	Uvicorn (ASGI)
📂 Project Structure
Content_Mod/
│
├── main.py                 # Main FastAPI application
├── database.py             # DB setup and models
├── models.py               # SQLAlchemy ORM models
├── schemas.py              # Pydantic request/response models
├── requirements.txt        # Dependencies list
├── .env                    # Environment variables (API keys)
└── README.md               # Project documentation

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Content_Mod.git
cd Content_Mod

2️⃣ Create Virtual Environment

Using venv:

python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate   # on macOS/Linux


Or using conda:

conda create -n content_mod python=3.10 -y
conda activate content_mod

This one worked for me as I am working on conda.

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variables

Create a .env file in your project root:

OPENAI_API_KEY=your_openai_api_key_here

5️⃣ Initialize Database
python
>>> from database import init_db
>>> init_db()
>>> exit()


This creates a moderation.db SQLite file.

6️⃣ Run the Server
uvicorn main:app --reload


Now visit: 👉 http://127.0.0.1:8000/docs

You’ll see the Swagger UI for testing your endpoints.

🧩 API Documentation
🔹 1. POST /api/v1/moderate/text

Description: Analyze user text for inappropriate or harmful content.

Request Body:

{
  "email": "user@example.com",
  "text": "You are an idiot"
}


Response:

{
  "classification": "toxic",
  "confidence": 0.92,
  "reasoning": "Contains insult and abusive language."
}

🔹 2. POST /api/v1/moderate/image

Description: Analyze an image (via URL) for explicit or inappropriate content.

Request Body:

{
  "email": "user@example.com",
  "image_url": "https://example.com/image.jpg"
}


Response:

{
  "classification": "safe",
  "confidence": 0.88,
  "reasoning": "No explicit content detected."
}

🔹 3. GET /api/v1/analytics/summary?user=user@example.com

Description: Get the moderation summary for a specific user.

Response:

{
  "total_requests": 10,
  "toxic": 3,
  "safe": 6,
  "spam": 1
}

🧠 How It Works

User sends text/image via API request.

The content is sent to OpenAI GPT for classification.

The model returns a classification and confidence score.

The results are stored in the SQLite database.

(Optional) Notifications can be sent via Slack or email when toxic content is detected.

🧩 Database Schema
moderation_requests
Column	Type	Description
id	Integer	Primary key
content_type	String	'text' or 'image'
content_hash	String	Unique hash of content
status	String	'processed', 'pending'
created_at	DateTime	Timestamp
moderation_results
Column	Type	Description
id	Integer	Primary key
request_id	ForeignKey	Links to moderation_requests
classification	String	Category (toxic/spam/safe)
confidence	Float	Confidence score
reasoning	Text	LLM explanation
llm_response	JSON	Raw model output
🧰 Future Enhancements

🔔 Slack/Email alerts for flagged content

🐳 Docker Compose setup (FastAPI + Postgres)

📊 Detailed analytics dashboard

⚙️ Celery-based async background tasks

🧑‍💻 Author

Harshit Kashyap
Final Year B.Tech CSE (AIML) — UPES Dehradun
📧 harshitkashyap@example.com

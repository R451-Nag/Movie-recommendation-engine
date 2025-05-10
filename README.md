![image alt](https://github.com/R451-Nag/Movie-recommendation-engine/blob/acfdd65822f08cdcee1b22d9f0354518ae322338/Screenshot%202025-05-10%20104502.png)
# Movie-recommendation-engine
This is a simple AI-powered **recommendation system** that suggests similar movies based on a user’s input. The backend is built using **Flask** and **scikit-learn**, and it exposes a **RESTful API** to deliver intelligent recommendations. The frontend is a visually appealing web interface built with plain HTML, CSS, and JavaScript.

---

## ✨ Features

- 🔍 Content-based recommendation engine using **TF-IDF** and **cosine similarity**
- ⚙️ REST API backend with **Flask**
- 🌐 Interactive web interface to input movie names and view suggestions
- 🔄 Cross-Origin Resource Sharing (CORS) enabled for frontend-backend communication
- 🧠 Built using **AI/ML libraries** (scikit-learn, pandas)

---

## 🛠️ Tech Stack

| Layer       | Technology              |
|-------------|--------------------------|
| Backend     | Python, Flask, scikit-learn, pandas |
| Frontend    | HTML, CSS, JavaScript    |
| ML Model    | TF-IDF + Cosine Similarity |
| API Style   | RESTful                  |

---

## 📁 Project Structure
ai_recommendation_engine/
├── app.py # Flask app with API endpoint
├── recommender.py # AI model logic
├── frontend/
│ └── index.html # User interface
└── README.md # Project instructions

## Create virtual environment
-python -m venv venv
-.\venv\Scripts\activate

## Install dependencies
-pip install flask flask-cors scikit-learn pandas

## Run backend and frontend
-python app.py
-Navigate to frontend/index.html
-Open it using Live Server (recommended) or right-click → "Open in Browser"

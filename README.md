# 🧠 Natural Language → SQL AI Agent

An end-to-end AI-powered SQL agent that allows users to query a PostgreSQL (Supabase) database using plain English, with memory, department-wise filtering, and dynamic aggregation — deployed as a Streamlit web app.

---

## 🚀 Features

* 🔤 Ask questions in natural language
* 🧠 Intent detection (highest / lowest / average / select)
* 🏢 Department-wise queries (Engineering, Sales, HR, etc.)
* 📊 Salary analytics:
  - Highest salary
  - Lowest salary
  - Average salary
* 🧾 Session memory (stores last user queries & answers)
* 🌐 Deployed as a web application
* ☁️ Uses Supabase (PostgreSQL) as backend database
* 🤖 Lightweight ML model trained on Text-to-SQL dataset

----

### 🏗️ Architecture Overview
```pgsql
User (Web UI - Streamlit)
        ↓
Natural Language Query
        ↓
Rule-based + ML Intent Detection
        ↓
Business Logic (Python)
        ↓
Supabase (PostgreSQL)
        ↓
Formatted Natural Language Answer
        ↓
Session Memory (Query History)
```

----

### 🛠️ Tech Stack

- Frontend: Streamlit
- Backend Logic: Python
- Database: Supabase (PostgreSQL)
- ML Model: TF-IDF + Logistic Regression
- Model Training: Kaggle (Text-to-SQL dataset)
- Deployment: Streamlit Cloud

---

### 📂 Project Structure
```yaml
sql-ai-agent/
│
├── app.py                     # Streamlit web app
├── query_intent_model.pkl     # Trained ML model
├── tfidf_vectorizer.pkl       # Text vectorizer
├── requirements.txt
└── README.md
```

----

### 🧪 Example Queries

- highest salary employee
- lowest salary in sales
- average salary in engineering
- show employees
- top paid employee in hr

----

### 🧠 How Intent Detection Works

- Rule-based logic handles common business queries (fast & explainable)
- ML model (trained on a Text-to-SQL dataset) acts as a fallback
- This hybrid approach avoids heavy LLMs while remaining reliable and efficient

----

### 🧾 Memory Feature

The agent maintains session-level memory, showing:
- Previous user questions
- Corresponding answers
  
This makes the agent feel stateful and conversational.

----

### ⚙️ Environment Variables

For local development (.env):
```ini
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

For Streamlit Cloud, the same values are added via Secrets (TOML format).

----

### 🌐 Deployment

The application is deployed using Streamlit Cloud and connects securely to Supabase using environment secrets.

----

### 📈 Future Enhancements

- Multi-table SQL support
- Role-based access control
- Advanced query parsing
- Export results as CSV
- LLM-based SQL generation 

-----

### 🧑‍💻 Author

Kumar Nihal
Generative AI / Agentic AI Engineer

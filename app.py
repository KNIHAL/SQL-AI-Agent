import os
import joblib
import warnings
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client

# ------------------ setup ------------------
warnings.filterwarnings("ignore")
load_dotenv()

# load ML (backup, optional)
model = joblib.load("query_intent_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# supabase client
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# session memory
if "history" not in st.session_state:
    st.session_state.history = []

# ------------------ UI ------------------
st.set_page_config(page_title="SQL AI Agent", layout="centered")
st.title("🧠 Natural Language → SQL AI Agent")

query = st.text_input("Ask your question (English):")

# ------------------ logic ------------------
if st.button("Run Query") and query:

    q = query.lower()

    # -------- intent detection --------
    if any(w in q for w in ["average", "avg", "mean"]):
        intent = "AVERAGE"
    elif any(w in q for w in ["lowest", "minimum", "min"]):
        intent = "LOWEST"
    elif any(w in q for w in ["highest", "maximum", "max", "top"]):
        intent = "HIGHEST"
    else:
        intent = "SELECT"

    # -------- department detection --------
    department = None
    departments = ["engineering", "sales", "hr", "marketing", "support"]

    for dept in departments:
        if dept in q:
            department = dept
            break

    # -------- fetch data --------
    data = supabase.table("employees").select("*").execute().data

    if not data:
        st.warning("No data found")
        st.stop()

    # -------- apply department filter FIRST --------
    if department:
        data = [
            d for d in data
            if d["department"].lower() == department
        ]

        if not data:
            st.warning(f"No data found for {department.capitalize()} department")
            st.stop()

    # -------- handle intents --------
    if intent == "HIGHEST":
        emp = max(data, key=lambda x: x["salary"])
        result = f"Highest paid employee in {emp['department']} is {emp['name']} with salary {emp['salary']}"
        st.success(result)

    elif intent == "LOWEST":
        emp = min(data, key=lambda x: x["salary"])
        result = f"Lowest paid employee in {emp['department']} is {emp['name']} with salary {emp['salary']}"
        st.success(result)

    elif intent == "AVERAGE":
        avg_salary = sum(e["salary"] for e in data) // len(data)
        if department:
            result = f"Average salary in {department.capitalize()} department is {avg_salary}"
        else:
            result = f"Average salary is {avg_salary}"
        st.success(result)

    else:
        result = data[:5]
        st.write(result)

    # -------- save to memory --------
    st.session_state.history.append({
        "query": query,
        "result": result
    })

# ------------------ memory UI ------------------
st.subheader("🧠 Query Memory (last 5)")

for item in reversed(st.session_state.history[-5:]):
    st.markdown(f"**Q:** {item['query']}")
    st.markdown(f"**A:** {item['result']}")
    st.markdown("---")

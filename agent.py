import os
import joblib
from dotenv import load_dotenv
from supabase import create_client
import warnings



load_dotenv()

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

model = joblib.load("query_intent_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# supabase client
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def agent(user_query):
    vec = vectorizer.transform([user_query])
    intent = model.predict(vec)[0]

    if intent == "AGGREGATION":
        response = supabase.table("employees") \
            .select("name, salary") \
            .order("salary", desc=True) \
            .limit(1) \
            .execute()
    else:
        response = supabase.table("employees") \
            .select("*") \
            .limit(5) \
            .execute()

    return response.data

print(agent("Show highest salary employee"))

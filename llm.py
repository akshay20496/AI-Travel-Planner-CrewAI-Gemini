import os
from crewai import LLM
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
# groq_key = os.getenv("groq_api")
# os.environ["GROQ_API_KEY"] = groq_key
gemini_key = os.getenv("gemini_api")

os.environ["GOOGLE_API_KEY"] = gemini_key

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.environ["GOOGLE_API_KEY"],
    temperature=0.5,
    verbose=True,
)

# print(gemini_key)  # Debugging: Check if the key is loaded correctly
# ---- Main LLM for heavy reasoning ----
# main_llm = LLM(
#     model="groq/llama3-8b-8192",
#     temperature=0.5,
#     verbose=True,
#     max_tokens=256,
#     top_p=0.9,
# )

# ---- Lightweight LLM for quick tasks ----
# fast_llm = LLM(
#     model="groq/gemma-7b-it",  # smaller → fewer tokens
#     temperature=0.5,
#     verbose=True,
#     max_tokens=256,
#     top_p=0.9,
# )

import os
import requests
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get your Serper API key from the environment
serper_key = os.getenv("serper_key")
if not serper_key:
    raise ValueError("Missing 'serper_key' in environment variables or .env file")

# Initialize Serper search tool
os.environ["SERPER_API_KEY"] = serper_key
search_tool = SerperDevTool()

# # Test search query
# query = "Pune to Shimla travel time and cost"

# # Serper API endpoint
# url = "https://google.serper.dev/search"

# # Headers
# headers = {
#     "X-API-KEY": serper_key,
#     "Content-Type": "application/json"
# }

# # Body
# payload = {
#     "q": query
# }

# # Make request
# response = requests.post(url, headers=headers, json=payload)

# # Print status and data
# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())

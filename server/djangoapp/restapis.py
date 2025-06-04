# Uncomment the imports below before you add the function code
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    # Baue die Parameter-Query-String
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
        params = params.rstrip("&")  # Entfernt das letzte &

    # Baue die vollständige URL
    request_url = f"{backend_url}{endpoint}"
    if params:
        request_url += f"?{params}"

    print(f"GET from {request_url}")

    try:
        # HTTP GET ausführen
        response = requests.get(request_url)
        response.raise_for_status()  # Für saubere Fehlerausgabe
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return {"error": str(e)}


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return {"error": str(err)}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
        return {"error": "Network error while posting review"}

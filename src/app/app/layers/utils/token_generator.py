import requests
import base64
import os


def get_headers():
    client_info = f"{os.getenv('CLIENT_ID')}:{os.getenv('CLIENT_SECRET')}"
    encoded_client_info = (base64.b64encode(bytes(client_info, "utf-8"))).decode("utf-8")
    headers = {"Authorization": f"Basic {encoded_client_info}"}

    return headers


def generate_tokens(code: str) -> tuple:
    headers = get_headers()
    spotify_get_token_url = os.getenv("SPOTIFY_GET_TOKEN_URL")

    response = requests.post(
        url=spotify_get_token_url,
        data={"grant_type": "authorization_code", "redirect_uri": os.getenv("REDIRECT_URI"), "code": code},
        headers=headers
    ).json()

    return response["access_token"], response["refresh_token"]


def refresh_tokens(refresh_token: str) -> str:
    headers = get_headers()
    spotify_get_token_url = os.getenv("SPOTIFY_GET_TOKEN_URL")

    response = requests.post(
        url=spotify_get_token_url,
        data={"grant_type": "refresh_token", "redirect_uri": os.getenv("REDIRECT_URI"), "refresh_token": refresh_token},
        headers=headers
    ).json()

    return response["access_token"]

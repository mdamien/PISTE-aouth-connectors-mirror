import os
from dotenv import load_dotenv
import requests
from requests_oauthlib import OAuth2Session

API_HOST = "https://sandbox-api.aife.economie.gouv.fr"
TOKEN_URL = 'https://sandbox-oauth.aife.economie.gouv.fr/api/oauth/token'

# 1. connect using the "client credentials" grant type
# the regular authentication methods don't work, we are passing
# the client id and secret as form data, as suggested by the PISTE team
load_dotenv()
client_id = os.getenv("OAUTH_CLIENT_ID")
client_secret = os.getenv("OAUTH_CLIENT_SECRET")
res = requests.post(
  TOKEN_URL,
  data={
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "openid"
  }
)
token = res.json()
client = OAuth2Session(client_id, token=token)

# import log_all_http

# 2. try a random request
payload = {
  "id": "KALIARTI000026231889"
}
res = client.post(
  "%s/dila/legifrance/lf-engine-app/consult/kaliArticle" % API_HOST,
  headers={
    "Accept": "application/json",  # might be redundant
    # "Content-Type": "application/json"
  },
  json=payload
)
print(f"status is {res.status_code}")
print("res is %s" % res.json())
"""
This contains methods to register token and get registered token.
The token is short-lived and expires in 1 hour. So once the token is
registered, it will be stored in memory store-redis to use it until
expiry. Upon expiry, the token will be registered again.
"""
import requests
import redis
from settings import *
from config import *

redis = redis.Redis(host='localhost', port=6379)


# Fetches token from redis if exists else register new
def get_token():
    token = redis.get('token')
    if not token:
        token = register_token()
    return token


# Registers new token and stores in redis
def register_token():
    params = {'client_id': CLIENT_ID,
              'email': EMAIL,
              'name': NAME}
    try:
        response = requests.post(sns_token_api, data=params)
        response.raise_for_status()
        response_json = response.json()
        token = response_json['data']['sl_token']
        redis.set('token', token)
        redis.expire('token', 3500)
    except requests.exceptions.HTTPError as err:
        print(f"Error : {str(err)}")
        token = None
    except Exception as err:
        print(f"Error : {str(err)}")
        token = None

    return token

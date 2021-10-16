"""
This script uses registered token to fetch posts from api. The posts api
needs token and page number to fetch posts. The response JSON data is then
appended to dataframe for further processing.
"""
import requests
import pandas as pd
from src import auth
from config import *


# Fetch posts using registered token and return all posts dataframe
def get_posts():
    try:
        token = auth.get_token()

        if token:
            posts_df = pd.DataFrame()
            for page_num in range(10):
                payload = {'sl_token': token, 'page:': page_num}
                response = requests.get(sns_posts_api, params=payload)
                response.raise_for_status()
                response_json = response.json()
                response_posts = response_json['data']['posts']
                posts_df = posts_df.append(response_posts)

                posts_df = posts_df.convert_dtypes()

                # Convert created_time string to datetime object to extract year, month
                # and week information
                posts_df['created_time'] = pd.to_datetime(posts_df['created_time'])
                posts_df['year'] = posts_df['created_time'].dt.year
                posts_df['month'] = posts_df['created_time'].dt.month
                posts_df['week'] = posts_df['created_time'].dt.isocalendar().week

                return posts_df
        else:
            raise Exception("Token value is missing.")
    except requests.exceptions.HTTPError as err:
        print(f"Error : {str(err)}")
        return None
    except Exception as err:
        print(f"Error : {str(err)}")
        return None



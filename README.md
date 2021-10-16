Social Network Systems' posts data analysis :

This code registers a token on a fictional social network system API. 
It uses this token to fetch user posts from the fictional social network systems' 
posts API. These posts are then processed for some Exploratory Data Analysis (EDA).

- The posts_eda.py gets user posts related data in a pandas dataframe from
posts.py.
- After processing the posts data, below stats are genarated :
  - Average character length of posts per month
  - Longest post by character length per month
  - Total posts split by week number
  - Average number of posts per user per month
- These stats are displayed in JSON format.


"""
Exploratory data analysis for social network systems'(sns) posts data
to get some stats like
- Average character length of posts per month
- Longest post by character length per month
- Total posts split by week number
- Average number of posts per user per month
"""
import json
import numpy as np
from src import posts


# Average character length of posts per month
def get_avglen_post_per_month(posts_df):
    df = posts_df.groupby(["year", "month"])['message'].apply(lambda x: np.mean(x.str.len())).reset_index(
        name='avg_len_post').round(2)
    df_to_json(df, "Average character length of posts per month")


# Longest post by character length per month
def get_longest_post_per_month(posts_df):
    df = posts_df.groupby(["year", "month"])['message'].apply(lambda x: x.str.len().max()).reset_index(
        name='max_len_post')
    df_to_json(df, "Longest post by character length per month")


# Total posts split by week number
def get_tot_posts_per_week(posts_df):
    df = posts_df.groupby(["year", "week"]).size().reset_index(name='posts_count')
    df_to_json(df, "Total posts split by week number")


# Average number of posts per user per month
def get_avgnum_posts_per_user_per_month(posts_df):
    df = posts_df.groupby(["year", "month"]).agg(tot_posts=('message', 'size'),
                                                 tot_unique_users=('from_id', 'nunique')).reset_index()
    df['avg_num_posts'] = (df['tot_posts']/(df['tot_unique_users'])).round(2)
    df_to_json(df, "Average number of posts per user per month")


def df_to_json(df, result_descr_str, orient="records"):
    result = df.to_json(orient=orient)
    parsed = json.loads(result)
    print(f"==={result_descr_str}===")
    print(json.dumps(parsed, indent=4))


def main():
    posts_df = posts.get_posts()
    print(posts_df.shape)
    get_avglen_post_per_month(posts_df)
    get_longest_post_per_month(posts_df)
    get_tot_posts_per_week(posts_df)
    get_avgnum_posts_per_user_per_month(posts_df)


main()

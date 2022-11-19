# Import Libraries
import requests
import json
import datetime
import pandas as pd

def extract_data():
    # Define Parameters Dictionary
    params = dict()
    params['access_token'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Access Token generated from graph api tools    
    params['graph_domain'] = 'https://graph.facebook.com' 
    params['graph_version'] = 'v15.0' # API version 
    params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/' #url
    params['instagram_account_id'] = 'xxxxxxxxxx'    # instagram business account id
    params['ig_username'] = '_itachiu__' #instagram username

    # Define Endpoint Parameters
    endpointParams = dict()
    endpointParams['input_token'] = params['access_token']
    endpointParams['access_token'] = params['access_token']

    # Define URL
    url = params['graph_domain'] + '/debug_token'

    # Requests Data
    data = requests.get(url, endpointParams)
    access_token_data = json.loads(data.content)

    #print(access_token_data)
    print("Token Expires: ", datetime.datetime.fromtimestamp(access_token_data['data']['expires_at']))

    # Define URL
    url_insta = params['endpoint_base'] + params['instagram_account_id'] + '/media'

    # Define Endpoint Parameters
    endpointParams = dict()
    endpointParams['fields'] = 'id,caption,media_url,permalink,thumbnail_url,username,like_count,comments_count,engagement,impressions,reach,saved'
    endpointParams['access_token'] = params['access_token']

    # Requests Data
    data = requests.get(url_insta, endpointParams )
    basic_insight = json.loads(data.content)
    print(basic_insight)

    #Using Pandas for table formed data
    df = pd.DataFrame(basic_insight['data'])
    df.columns = ['id', 'Caption', 'Media_URL', 'Permalink', 'Username', 'Likes', 'Comments']
    print(df.head())

    # Loop Over 'Media IDs'
    media_insight = []

    for i in basic_insight['data']:
        params['latest_media_id'] = i['id']
        
        # Define URL
        url_insight = params['endpoint_base'] + params['latest_media_id'] + '/insights'

        # Define Endpoint Parameters
        endpointParams = dict() 
        endpointParams['metric'] = 'engagement,impressions,reach,saved'
        endpointParams['access_token'] = params['access_token'] 
        print(endpointParams)
        # Requests Data
        data = requests.get(url_insight, endpointParams)
        json_data_temp = json.loads(data.content)
        media_insight.append(list(json_data_temp['data']))

    # Initialize Empty Container
    engagement_list = []
    impressions_list = []
    reach_list = []
    saved_list = []

    # Loop Over Insights to Fill Container
    for insight in media_insight:
        engagement_list.append(insight[0]['values'][0]['value'])
        impressions_list.append(insight[1]['values'][0]['value'])
        reach_list.append(insight[2]['values'][0]['value'])
        saved_list.append(insight[3]['values'][0]['value'])
        
    # Create DataFrame
    df_media_insight = pd.DataFrame(list(zip(engagement_list, impressions_list, reach_list, saved_list)), columns =['Engagement', 'Impressions', 'Reach', 'Saved'])
    print(df_media_insight.head())

    # Complete Dataframe
    df_complete = pd.concat([df, df_media_insight], axis=1)
    print(df_complete.head())
    return df_complete
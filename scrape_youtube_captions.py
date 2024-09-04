# %% [markdown]
# ### A-I 574 - Natural Language Processing (FA24)
# #### **Discussion Topic for Lesson 2 (Scrapping online textual data):** *Extracting YoutTube videos captions for a certain subject*
# #### **Instructor**: Dr. Satish Srinivasan      |       **Student**:    Aureo Zanon         |       **Date**:       09/02/2024
# 

# %% [markdown]
# <hr/>

# %% [markdown]
# ### Initial Setup for YouTube Captions Web Scrapping

# %%
# Create and activate new conda environment (uncomment the lines below to run the conda commands)
#!conda create -n WebScrapping python=3.10
#!conda activate WebScrapping

# %%
# Installing required Python packages (uncomment the lines below to pip install the required Python packages)
#!pip install google-api-python-client pandas
#!pip install google-api-python-client youtube-transcript-api pandas
#!pip install youtube_transcript_api

# %%
# Loading required Libraries
import os
import pandas as pd
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

# %% [markdown]
# <hr/>

# %% [markdown]
# ### Instructions to Create the YouTube Data API v3 Key
# #### In order to use this Python script, you will need to create a key for the YouTube Data API v3. Please see more details at the link <https://developers.google.com/youtube/v3/getting-started>

# %% [markdown]
# <hr/>

# %% [markdown]
# ### Calling the API Key and Building the API Client

# %%
# YouTube API key (Replace with your own API key)
api_key = 'AIzaSyDCDdSDXERNCmA-YavCc1yIh1n44Q9N8Ws' # I revoked this key before posting this code
#api_key = 'YOUR_API_KEY - follow the instructions from the link above to get it'

# %%
# Build the YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# %% [markdown]
# <hr/>

# %% [markdown]
# ### Building the Functions to search for videos according to a certain subject and grab their captions

# %%
# Function to search for videos related to the subject in the last n days and capture captions
def search_videos_last_24_hours_with_captions(query, max_results=100):
    # Get the current UTC time and calculate the time 24 hours ago
    n = 1
    published_after = (datetime.now(timezone.utc) - timedelta(days=n)).isoformat()
    
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results,
        publishedAfter=published_after,
        order="date"  # Order results by date to get the latest videos
    )
    response = request.execute()
    
    videos = []
    
    for item in response['items']:
        video_id = item['id']['videoId']
        video_data = {
            "Video Title": item['snippet']['title'],
            "Channel Name": item['snippet']['channelTitle'],
            "Published Date": item['snippet']['publishedAt'],
            "Video ID": video_id,
            "Video URL": f"https://www.youtube.com/watch?v={video_id}",
            "Captions": get_video_captions(video_id)  # Capture captions
        }
        videos.append(video_data)
    
    return videos



# %%
# Function to get captions for a video
def get_video_captions(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        captions = " ".join([entry['text'] for entry in transcript])
        return captions
    except NoTranscriptFound:
        return "No captions found"
    except TranscriptsDisabled:
        return "Captions are disabled for this video"

# %%
# Web Scraping the captions from YouTube videos related to the selected subject
subject = 'Elon Musk'
videos_with_captions = search_videos_last_24_hours_with_captions(subject, max_results=100)


# %%
# Save to CSV
df = pd.DataFrame(videos_with_captions)
df.to_csv("generative_ai_videos_with_captions.csv", index=False)

# %%
print(df)



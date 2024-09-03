### YouTube Video Captions Scraper

This Python project scrapes captions from YouTube videos related to a selected subject, published in the last n days. The script uses the YouTube Data API v3 to search for videos and the youtube_transcript_api library to fetch video captions. The resulting data, including video details and captions, is saved to a CSV file.

Table of Contents
Features
Installation
Usage
Data Details
Requirements
API Key Setup
Example
Credits
Features
Search for YouTube videos related to a specific subject published in the last 24 hours.
Fetch video details including title, channel name, published date, and video URL.
Retrieve captions (if available) for each video.
Save the collected data to a CSV file for further analysis.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/youtube-captions-scraper.git
cd youtube-captions-scraper
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Usage
Obtain a YouTube Data API Key: Follow the instructions in the API Key Setup section to create your API key.

Set the Subject: In the script, change the subject variable to the topic you want to search for.

Run the Script:

bash
Copy code
python scrape_youtube_captions.py
Output: The script will generate a CSV file containing video details and captions related to the selected subject.

Data Details
Fields in the CSV file:

Video Title: The title of the video.
Channel Name: The name of the YouTube channel that published the video.
Published Date: The date and time when the video was published.
Video ID: The unique identifier for the video.
Video URL: The direct link to the video on YouTube.
Captions: The text of the captions retrieved from the video, or a message if captions are not available.
File Format: The data is saved in CSV format.

Requirements
Python 3.x
google-api-python-client: To interact with the YouTube Data API.
youtube-transcript-api: To fetch captions from YouTube videos.
pandas: For data manipulation and saving the data to a CSV file.
API Key Setup
Go to the Google Cloud Console.
Create a new project or select an existing project.
Enable the YouTube Data API v3.
Create API credentials and obtain your API key.
Replace the placeholder YOUR_API_KEY in the script with your actual API key.
Example
Suppose you want to scrape captions from YouTube videos related to "Elon Musk" published in the last 24 hours. Update the subject variable in the script:

python
Copy code
subject = 'Elon Musk'
Run the script:

This project was created to demonstrate how to use an API to scrape and analyze online content, specifically focusing on video metadata and captions from YouTube.

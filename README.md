
# YouTube Video Captions Scraper

This Python project scrapes captions from YouTube videos related to a selected subject, published in the last 24 hours. The script uses the YouTube Data API v3 to search for videos and the `youtube_transcript_api` library to fetch video captions. The resulting data, including video details and captions, is saved to a CSV file.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Details](#data-details)
- [Requirements](#requirements)
- [API Key Setup](#api-key-setup)
- [Example](#example)
- [Credits](#credits)

## Features

- Search for YouTube videos related to a specific subject published in the last 24 hours.
- Fetch video details including title, channel name, published date, and video URL.
- Retrieve captions (if available) for each video.
- Save the collected data to a CSV file for further analysis.


## Installation

1. **Create and activate a new conda environment**:
   ```bash
   conda create --name youtube-scraper-env python=3.9
   conda activate youtube-scraper-env
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/youtube-captions-scraper.git
    cd youtube-captions-scraper
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Obtain a YouTube Data API Key**: Follow the instructions in the [API Key Setup](#api-key-setup) section to create your API key.

2. **Set the Subject**: In the script, change the `subject` variable to the topic you want to search for.

3. **Run the Script**:

    ```bash
    python scrape_youtube_captions.py
    ```

4. **Output**: The script will generate a CSV file containing video details and captions related to the selected subject.

## Data Details

- **Fields in the CSV file**:
  - **Video Title**: The title of the video.
  - **Channel Name**: The name of the YouTube channel that published the video.
  - **Published Date**: The date and time when the video was published.
  - **Video ID**: The unique identifier for the video.
  - **Video URL**: The direct link to the video on YouTube.
  - **Captions**: The text of the captions retrieved from the video, or a message if captions are not available.

- **File Format**: The data is saved in CSV format.

## Requirements

- Python 3.x
- `google-api-python-client`: To interact with the YouTube Data API.
- `youtube-transcript-api`: To fetch captions from YouTube videos.
- `pandas`: For data manipulation and saving the data to a CSV file.

## API Key Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Enable the **YouTube Data API v3**.
4. Create API credentials and obtain your API key.
5. Replace the placeholder `YOUR_API_KEY` in the script with your actual API key.

## Example

Suppose you want to scrape captions from YouTube videos related to "Elon Musk" published in the last 24 hours. Update the `subject` variable in the script:

```python
subject = 'Elon Musk'
```

Run the script:

```bash
python scrape_youtube_captions.py
```

The script will output a CSV file named `elon_musk_videos_with_captions.csv` containing the video details and captions.

## Credits

- **YouTube Data API**: For providing access to video metadata.
- **youtube-transcript-api**: For facilitating the retrieval of video captions.
- **Pandas**: For data manipulation and CSV handling.

This project was created to demonstrate how to use an API to scrape and analyze online content, specifically focusing on video metadata and captions from YouTube.

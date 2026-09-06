import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

VIDEO_FILE = "assets/final/final_short.mp4"

creds = Credentials(
    None,
    refresh_token=os.environ["YOUTUBE_REFRESH_TOKEN"],
    token_uri="https://oauth2.googleapis.com/token",
    client_id=os.environ["YOUTUBE_CLIENT_ID"],
    client_secret=os.environ["YOUTUBE_CLIENT_SECRET"]
)

youtube = build("youtube", "v3", credentials=creds)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Amazing AI Fact #shorts",
            "description": "Automatically generated with AI #shorts",
            "tags": ["shorts", "ai"],
            "categoryId": "28"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload(VIDEO_FILE)
)

response = request.execute()

print("UPLOAD SUCCESS")
print(response)

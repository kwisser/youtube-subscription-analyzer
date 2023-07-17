import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    return youtube

def get_subscriptions(youtube):
    subscriptions = []
    next_page_token = None

    while True:
        response = youtube.subscriptions().list(
            part="snippet",
            mine=True,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        subscriptions += response["items"]
        next_page_token = response.get("nextPageToken")

        if next_page_token is None:
            break

    return subscriptions

if __name__ == "__main__":
    youtube = get_authenticated_service()
    subscriptions = get_subscriptions(youtube)

    for subscription in subscriptions:
        print(subscription["snippet"]["title"])


import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service():
    credentials_path = "credentials.pickle"
    if os.path.exists(credentials_path):
        with open(credentials_path, "rb") as f:
            credentials = pickle.load(f)
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", scopes)
        credentials = flow.run_console()
        with open(credentials_path, "wb") as f:
            pickle.dump(credentials, f)

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

    # Zugriff auf die topicDetails jeder Subscription
    for subscription in subscriptions:
        snippet = subscription["snippet"]
        title = snippet["title"]
        channelId = snippet["resourceId"]["channelId"]

        # Anfrage für topicDetails
        response = youtube.channels().list(
            part="topicDetails",
            id=channelId
        ).execute()

        items = response.get("items", [])
        if items:
            topicDetails = items[0].get("topicDetails", {})
        else:
            topicDetails = {"topicCategories": []}

        print("Kanal-Titel:", title)
        print("Themenbereiche:", topicDetails.get("topicCategories", []))
        print("\n")

    return subscriptions


if __name__ == "__main__":
    youtube = get_authenticated_service()
    subscriptions = get_subscriptions(youtube)

    for subscription in subscriptions:
        print(subscription["snippet"])
        print("\n")


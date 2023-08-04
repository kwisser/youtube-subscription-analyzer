import os
import pickle
from collections import defaultdict
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import matplotlib.pyplot as plt

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
    topic_count = defaultdict(int)  # Default dictionary to hold count of each topic

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

    # Access the topicDetails of each subscription
    for subscription in subscriptions:
        snippet = subscription["snippet"]
        title = snippet["title"]
        channelId = snippet["resourceId"]["channelId"]

        # Request for topicDetails
        response = youtube.channels().list(
            part="topicDetails",
            id=channelId
        ).execute()

        items = response.get("items", [])
        if items:
            topicDetails = items[0].get("topicDetails", {})
            topicCategories = topicDetails.get("topicCategories", [])
        else:
            topicCategories = []

        # Count the occurrence of each topic category
        for topic in topicCategories:
            topic_count[topic] += 1

        print("Channel Title:", title)
        print("Topic Categories:", topicCategories)
        print("\n")

    print("Topic counts:")
    topics = []
    counts = []
    for topic, count in topic_count.items():
        print(topic, count)
        topics.append(topic.replace("https://en.wikipedia.org/wiki/", ""))
        counts.append(count)

    plt.bar(topics, counts)
    plt.xlabel('Topics')
    plt.ylabel('Counts')
    plt.title('Distribution of Topics in YouTube Subscriptions')
    plt.xticks(rotation='vertical')
    plt.show()

    return subscriptions


if __name__ == "__main__":
    youtube = get_authenticated_service()
    subscriptions = get_subscriptions(youtube)

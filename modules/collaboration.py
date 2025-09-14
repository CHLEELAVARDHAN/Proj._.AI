import json
import os

FEED_FILE = "data/feed.json"

# Ensure data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

def load_feed():
    try:
        with open(FEED_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_feed(feed):
    with open(FEED_FILE, "w") as f:
        json.dump(feed, f, indent=4)

def collaborate(user_name, idea, sector, language):
    # Load existing feed
    if os.path.exists(FEED_FILE):
        with open(FEED_FILE, "r") as f:
            feed = json.load(f)
    else:
        feed = {}

    # User ideas array
    if user_name not in feed:
        feed[user_name] = []

    # Add new idea
    feed[user_name].append({
        "idea": idea,
        "sector": sector,
        "language": language,
        "comments": []
    })

    # Save back
    with open(FEED_FILE, "w") as f:
        json.dump(feed, f, indent=4)


# 2️⃣ Show feed function: ideas display cheyyali
def show_feed():
    if os.path.exists(FEED_FILE):
        with open(FEED_FILE, "r") as f:
            feed = json.load(f)
        return feed
    return {}

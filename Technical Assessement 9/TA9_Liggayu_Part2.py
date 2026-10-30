
import pandas as pd
import sqlite3
import regex as re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pathlib import Path

# Import the dataset folder
dataset_path = Path("sorted_data_acl")

# Read positive and negative review files
reviews = []

for file_path in dataset_path.rglob("*.review"):

    sentiment = file_path.stem

    if sentiment not in ["positive", "negative"]:
        continue

    with open(file_path, "r", encoding="latin-1") as file:
        content = file.read()

    # Extract review texts
    review_texts = re.findall(
        r"<review_text>(.*?)</review_text>",
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    for review in review_texts:
        reviews.append({
            "text": review,
            "sentiment": sentiment
        })

# Create dataframe
df = pd.DataFrame(reviews)

# Exploratory analysis
print("Positive reviews:", len(df[df.sentiment == "positive"]))
print("Negative reviews:", len(df[df.sentiment == "negative"]))
print("Dataset shape:", df.shape)

# Remove duplicate records
df = df.drop_duplicates()
df = df.reset_index(drop=True)

print("Shape after removing duplicates:", df.shape)

# Clean the texts
clean_desc = []

for w in range(len(df.text)):

    desc = df["text"][w].lower()

    # Remove punctuation
    desc = re.sub("[^a-zA-Z]", " ", desc)

    # Remove tags
    desc = re.sub("&lt;/?.*?&gt;", " ", desc)

    # Remove digits and special characters
    desc = re.sub(r"(\d|\W)+", " ", desc)

    clean_desc.append(desc)

# Assign cleaned descriptions to dataframe
df["text"] = clean_desc

# Remove stop words
stop_words = [
    "is", "you", "your", "and", "the", "to", "from", "or",
    "i", "for", "do", "get", "not", "here", "in", "im",
    "have", "on", "re", "new", "subject"
]

# Generate Word Cloud for all reviews
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="black",
    stopwords=stop_words,
    max_words=1000,
    min_font_size=20
).generate(" ".join(df["text"]))

# Display the Word Cloud
fig = plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("challenge_wordcloud.png", bbox_inches="tight")
plt.show()

# Generate separate positive and negative Word Clouds
for sentiment in ["positive", "negative"]:

    text_data = " ".join(
        df.loc[df["sentiment"] == sentiment, "text"]
    )

    if text_data.strip():

        wordcloud = WordCloud(
            width=800,
            height=800,
            background_color="black",
            stopwords=stop_words,
            max_words=1000,
            min_font_size=20
        ).generate(text_data)

        plt.figure(figsize=(8, 8))
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.title(sentiment.capitalize() + " Reviews")
        plt.savefig(
            sentiment + "_wordcloud.png",
            bbox_inches="tight"
        )
        plt.show()

import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

# Read the CSV file
# replace with the exact location of your file
df = pd.read_csv(
    r"C:\Users\CL401_07\Sakshi_CSE\SIT_Canteen_Google_Form_Feedback.csv"
)

sia = SentimentIntensityAnalyzer()


def analyze_sentiment(feedback):
    if not isinstance(feedback, str):
        return pd.Series([0.0, "neutral"])

    score = sia.polarity_scores(feedback)["compound"]

    if score >= 0.05:
        sentiment = "positive"
    elif score <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    # Properly unindented return statement
    return pd.Series([score, sentiment])


# Apply sentiment function across the dataframe
df[["Sentiment_Score", "Sentiment"]] = df["Canteen_Feedback"].apply(
    analyze_sentiment
)

# Print output
print(
    df[
        [
            "Student_Staff_ID",
            "Canteen_Feedback",
            "Sentiment_Score",
            "Sentiment",
        ]
    ]
)

# Save result to CSV
df.to_csv("Canteen_Feedback_With_Sentiment.csv", index=False)

print("\nSentiment analysis completed.")
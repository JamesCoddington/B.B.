from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

"""
run pip install vaderSentiment
"""

analyzer = SentimentIntensityAnalyzer()
user_messages = ["hello", "bitch", "you're an ass", "you're pretty", "Buh bye"]

negative_score = 0

for message in user_messages:
    message_score = analyzer.polarity_scores(message)
    print("{:-<65} {}".format(message, str(message_score)))
    negative_score += message_score["neg"]

overall_negative_score = negative_score / len(user_messages)

print(f"The user's overall negative score is: {overall_negative_score}")
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

"""
run pip install vaderSentiment
"""

def analyze(messages):
    analyzer = SentimentIntensityAnalyzer()
    negative_score = 0

    for message in messages:
        message_score = analyzer.polarity_scores(message)
        negative_score += message_score["neg"]

    overall_negative_score = negative_score / len(messages)

    return round(overall_negative_score, 3)
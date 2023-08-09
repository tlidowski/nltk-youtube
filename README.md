# YT_sentiment_analysis

# Research Question:
Can a sentiment analysis using the Youtube Data API of Youtube video comments
provide an accurate means of determining the favorability of a video?

# What do we want to study
By gauging the audience's reaction to a video, content creators and analysts will be able
to gain deeper insights into the emotional reactions of their users. Our research aims to conduct a sentiment analysis of the comments on YouTube videos. 

The objective is to leverage the YouTube Data API to collect data on viewer comments, analyze the language used, and classify each comment as positive, negative, or neutral sentiment. The goal is to determine the overall sentiment of comments and provide insights into the exact favorability of a particular YouTube video.

# Instructions to run

If you are running the jupyter notebook locally, run init.py first. This will install the libraries needed.

If you are using anaconda, uncomment the import statements on the top of the file and run the cell to install the libraries needed. After uncommenting, you can also just run the entire file at once.

The ".env" file consists of the API_KEY needed to make API requests to the YouTube Data API

# Prereqs
```pip install reportlab```

```pip install python-dotenv```

- Python 2.7 or Python 3.5+
- The pip package management tool
- The Google APIs Client Library for Python:

```pip install --upgrade google-api-python-client```

- The ```google-auth-oauthlib``` and ```google-auth-httplib2``` libraries for user authorization.

```pip install --upgrade google-auth-oauthlib google-auth-httplib2```

# Sentiment Analysis Methods used:
- POS tagging
    - Using hugging face sentiment analysis menthod, with Twitter roBERTa model.

# Issues encountered
- For music videos some people just comment the song lyrics. Doesn't say anything but adds to positive score. This cannot be taken as a positive comment because lyrics can have both sentiments, and the sentiment of lyrics and the sentiment of the user can be different.

- YouTube comments are in all different langauges

- Sarcasm analysis isn't there.


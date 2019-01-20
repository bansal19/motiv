"""Given an emotion into the function, you return a single string formatted like so:
'Artist-SongTitle, Artist-SongTitle, ...' """
import os
import pandas as pd

data = pd.read_csv('allEmotions.csv')


def click_circle(emotion_name):
    """Circle has been clicked, we're going to return """


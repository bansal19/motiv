"""Exploring toxicity of songs"""

import re
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import seaborn as sns

df = pd.read_csv("train.csv", encoding="ISO-8859-1")
df.head()

# create file for toxicity. create count of various types of toxicity.
dftoxic = df.drop(['id', 'comment_text'], axis=1)
types = list(dftoxic.columns.values)
counts = []
for i in types:
    counts.append((i, dftoxic[i].sum()))

# convert into a dataframe
dfstats = pd.DataFrame(counts, columns=['type', 'stats'])
dfstats

rowsums = df.iloc[:, 2:].sum(axis=1)
x = rowsums.value_counts()

length = df.comment_text.str.len()
plt.hist(length, bins=np.arange(0, 5000, 50))
plt.show()


def clean_text(text):
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"\'scuse", " excuse ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')
    return text


df['comment_text'] = df['comment_text'].apply(lambda x: clean_text(x))
df['comment_text']

categories = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
train, test = train_test_split(df, random_state=42, test_size=0.43, shuffle=True)
X_train = train.comment_text
X_test = test.comment_text

vectorizer = TfidfVectorizer(stop_words=stop_words)
for category in categories:
    vectorizer.fit(X_train, train[category])

vectors = vectorizer.fit_transform(X_train, train['toxic'])
clf = OneVsRestClassifier(MultinomialNB(fit_prior=True, class_prior=None))
clf.fit(vectors, train['toxic'])
clf.predict(X_test)

NB_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words=stop_words)),
    ('clf', OneVsRestClassifier(MultinomialNB(
        fit_prior=True, class_prior=None))),
])
for category in categories:
    print('... Processing {}'.format(category))
    NB_pipeline.fit(X_train, train[category])
    prediction = NB_pipeline.predict(X_test)
    print('Test accuracy is {}'.format(accuracy_score(test[category], prediction)))

SVC_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words=stop_words)),
    ('clf', OneVsRestClassifier(LinearSVC(), n_jobs=1)),
])
for category in categories:
    print('... Processing {}'.format(category))
    # train the model using X_dtm & y
    SVC_pipeline.fit(X_train, train[category])
    # compute the testing accuracy
    prediction = SVC_pipeline.predict(X_test)
    print('Test accuracy is {}'.format(accuracy_score(test[category], prediction)))

vector = TfidfVectorizer(stop_words=stop_words)
test = vector.fit_transform(sample_text)
print(vector.get_params())
sample_text = ['hello this is a test to remove my stop words and see how this program works']

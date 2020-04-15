#import matplotlib.pyplot as plt
import tensorflow as tf
import random as rn
import numpy as np
import osp
os.environ['PYTHONHASHSEED'] = '0'
# Setting the seed for numpy-generated random numbers
np.random.seed(45)

# Setting the graph-level random seed.
tf.set_random_seed(1337)

rn.seed(73)

from keras import backend as K

session_conf = tf.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)

#Force Tensorflow to use a single thread
sess = tf.Session(graph=tf.get_default_graph(), config=session_conf)

K.set_session(sess)
import math
import pandas as pd

import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Reshape, MaxPooling2D, Dropout
from keras.layers import Conv2D, Dense, Flatten
from keras.callbacks import TensorBoard, EarlyStopping
from keras.optimizers import Adam, Adamax, RMSprop
from keras.models import load_model
from keras import regularizers

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelBinarizer, LabelEncoder, MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split
from sklearn.metrics import precision_recall_fscore_support

#Set Up Data
c_df = pd.read_csv("lowqualall.csv")

values_df = c_df.iloc[:, 2:-1]
def apply_split(s1):
    return_s = s1.split(",")
    return return_s
values_df = values_df.applymap(apply_split)

def apply_casting(l1):
    return_list = []
    for i in l1:
        return_list.append(float(i))
    return return_list
values_df = values_df.applymap(apply_casting)

target_df = c_df.iloc[:, -1].values

target_names = c_df.iloc[:, -1].unique()
num_classes = len(target_names)
#Ensure that train set encompases the data.
#assert num_classes == 10 #Number of Emotions

x_train, x_test, y_train, y_test = train_test_split(values_df, target_df, stratify=target_df, test_size=0.2) #stratify may cause issues

#Reshape the Train Data
x_train = x_train.values
x_train = x_train.tolist()
x_train = np.array(x_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 10))

#Reshape the Test DAta
x_test = x_test.values
x_test = x_test.tolist()
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 10))

#Need to scale each feature separately

scalers = {}
for i in range(x_train.shape[2]):
    scalers[i] = MinMaxScaler(feature_range=(0, 1))
    x_train[:, i, :] = scalers[i].fit_transform(x_train[:, i, :])
X_train = x_train

for i in range(x_test.shape[2]):
    x_test[:, i, :] = scalers[i].transform(x_test[:, i, :])
X_test = x_test

#Encode the Y's
encoder = LabelEncoder()
encoder = encoder.fit(y_train) #Can Hard Code Emotions Here
y_train_encoded = encoder.transform(y_train) #Classes given the indices
y_train_categorical = keras.utils.to_categorical(y_train_encoded, num_classes) #Binary Matrix Representation of Inputs
y_test_encoded = encoder.transform(y_test)
y_test_categorical = keras.utils.to_categorical(y_test_encoded, num_classes)

#Create Model Structure
classifier = Sequential()
#4 LSTM layers plus Dropouts within the stack
classifier.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2]))) #Input shape
classifier.add(Dropout(0.2))
classifier.add(LSTM(units=50, return_sequences=True))
classifier.add(Dropout(0.2))
classifier.add(LSTM(units=50, return_sequences=True))
classifier.add(Dropout(0.2))
classifier.add(LSTM(units=50))
classifier.add(Dropout(0.2))
#Output Layer
classifier.add(Dense(units=num_classes, activation='softmax'))

#Compile and Train
classifier.compile(optimizer=RMSprop(), loss='categorical_crossentropy')
classifier.fit(X_train, y_train_categorical, epochs=15, batch_size=32)

classifier.save("NewestModel.h5")
del classifier
K.clear_session()

classifier = load_model("NewestModel.h5")
#Test and Analyze Data
predictions = classifier.predict(X_test)
predictions_classes = np.argmax(predictions, axis=1)

test_labels_names = y_test_categorical.tolist()
print(f"Predictions_classes {predictions_classes}")
accuracy = np.sum(predictions_classes == np.argmax(y_test_categorical, axis=1)) / (y_test_categorical.shape[0])
print(f"Accuracy: {accuracy}")

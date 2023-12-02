import numpy as np
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense, LSTM, SimpleRNN, Dropout
from keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import OneHotEncoder
from pickle import dump

# read data
data = np.loadtxt("testing.csv",
                 delimiter=",")

print(data.shape)

# sample number = total / time steps (10)
sample_num = len(data)//10

print(sample_num)

# reshape into 2d space
data = data.reshape(len(data), 12)

# set feature 12 as uniques
data[:,11] = np.where(data[:,11] < 0.4, 2, data[:,11])
data[:,11] = np.where(data[:,11] < 0.6, 3, data[:,11])
data[:,11] = np.where(data[:,11] < 0.8, 4, data[:,11])
data[:,11] = np.where(data[:,11] <= 1, 5, data[:,11])

# encode data
encoder = OneHotEncoder(categories='auto')
data = encoder.fit_transform(data).toarray()

print(data.shape)

# reshape into input space
data = data.reshape(sample_num, 10, 50)

print(data.shape)

# divide data into train and test
val_ind = int(sample_num*0.95)
train = data[:val_ind,:,:]
val = data[val_ind:,:,:]

X_train = train[:,:9,:]
y_train = np.squeeze(train[:,9:,46:50])

X_val = val[:,:9,:]
y_val = np.squeeze(val[:,9:,46:50])

print(X_train.shape)
print(y_train.shape)

# Create model
rnnModel = Sequential() 
rnnModel.add(SimpleRNN(128, input_shape=(9,50), return_sequences=False)) # timespan of 10, function space of 12
rnnModel.add(Dense(4, activation='softmax')) # output is feature space for predicted value
rnnModel.build()
rnnModel.summary()

rnnModel.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

# fit model
rnnModel.fit(X_train, y_train, validation_data=(X_val,y_val), epochs=50, batch_size=128)

# save model
# rnnModel.save("specialization.h5")
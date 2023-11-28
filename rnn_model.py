import numpy as np
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.preprocessing.sequence import TimeseriesGenerator

# read data
data = np.loadtxt("ratings.csv",
                 delimiter=",")

# sample number = total / time steps (10)
sample_num = len(data)//10

# reshape into input space (feature = 13 since +1 for y value)
data = data.reshape(sample_num, 10, 13)

# divide data into train and test
train_ind = int(sample_num*0.8)
train = data[:train_ind,:,:12]
test = data[train_ind:,:,:12]

X_train = train[:,:9,:]
y_train = train[:,9:,:]

X_test = test[:,:9,:]
y_test = test[:,9:,:]

# Create model
rnnModel = Sequential() 
rnnModel.add(LSTM(128, input_shape=(9,12))) # timespan of 10, function space of 12
rnnModel.add(Dense(12)) # output is feature space for predicted value
rnnModel.build()
rnnModel.summary()

rnnModel.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# fit model
rnnModel.fit(X_train, y_train, epochs=10, batch_size=32)

# save model
rnnModel.save("rnnModel.h5")

# get accuracy
y_pred = rnnModel.predict(X_test)

print(y_pred)

mse = np.mean((y_pred - y_test)**2)

print(mse)
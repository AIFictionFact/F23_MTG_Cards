import numpy as np
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.preprocessing.sequence import TimeseriesGenerator

# read data
data = np.genfromtxt('dataset.csv')

# sample number = total / (time steps (10) * (features + target) (13))
sample_num = len(data)//130

# reshape into input space (feature = 13 since +1 for y value)
data = data.reshape(sample_num, 10, 13)

# divide data into train and test
train_ind = int(sample_num*0.8)*130
train = data[:train_ind]
test = data[train_ind:]

X_train = train[:,:12]
y_train = train[:,12]

X_test = test[:,:12]
y_test = test[:,12]

# Create model
rnnModel = Sequential() 
rnnModel.add(LSTM(128, input_shape=(10,12))) # timespan of 10, function space of 12
rnnModel.add(Dense(1)) # output is 1 value
rnnModel.build()
rnnModel.summary()

# fit model
rnnModel.fit(X_train, y_train, epochs=10, batch_size=32)

# save model
rnnModel.model("rnnModel.keras")

# get accuracy
y_pred = rnnModel.predict(X_test)
mse = np.mean((y_pred - y_test)**2)

print(mse)
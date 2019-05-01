from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten

import wandb
from wandb.keras import WandbCallback

# logging code
run = wandb.init()
config = run.config

# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

is_five_train = y_train == 5    #T/F for each value in y_train, T means 5
is_five_test = y_test == 5      #same but for y_test
labels = ["Not Five", "Is Five"]

img_width = X_train.shape[1]
img_height = X_train.shape[2]

# create model
model = Sequential()
model.add(Flatten(input_shape=(img_width, img_height)))
model.add(Dense(1, activation="sigmoid"))    #Dense means each input is going to result in a learned weight; 1 for an argument means 1 output value; sigmoid is the activation function type
model.compile(loss='mse', optimizer='adam',
              metrics=['binary_accuracy'])

# Fit the model
model.fit(X_train, is_five_train, epochs=5, validation_data=(X_test, is_five_test),
          callbacks=[WandbCallback(data_type="image", labels=labels, save_model=False)])
model.save('perceptron.h5')

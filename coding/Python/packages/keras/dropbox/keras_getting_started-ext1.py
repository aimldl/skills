# Keras
#
# keras_getting_started-ext1.py
#
#   This example code is in "Getting started: 30 seconds to Keras" 
# in the official Keras homepage. It's like hello-world for Keras.
# ext1 stands for extension 1.
#
# A command to run this script on Docker is:
#
#  $ docker run -it --name keras_test -v ~/aimldl/keras:/home/user/uploads aimldl/keras_base_image
#  your_docker_container $ python3 keras_hello_world.py
#
# To-do:
#   - There're some errors in the # parts. Correct them.
#   - In the keras base image,
#   - alias python='python3'
#   - mkdir keras
#
#   Last updated on 2018-09-20 (Thu)
#   First written on 2018-09-18 (Tue)
#   Written by Tae-Hyung "T" Kim, Ph.D.

from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 28*28=784
x_train = x_train.reshape(60000, 784).astype('float32') / 255.0
x_test  = x_test.reshape(10000, 784).astype('float32') / 255.0
y_train = np_utils.to_categorical( y_train )
y_test  = np_utils.to_categorical( y_test )

model = Sequential()
model.add( Dense(units=64, activation='relu', input_dim=28*28) )
model.add( Dense(units=10, activation='softmax') )
model.compile( loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

hist = model.fit( x_train, y_train, epochs=5, batch_size=32 )
print('loss : ' + str( hist.history['loss'] ) )
print('acc : ' + str( hist.history['acc'] ) )



#hist = model.fit( x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test,y_test ) )
#print('val_loss : ' + str( hist.history['val_loss'] ))
#print('val_acc : ' + str( hist.history['val_acc'] ))

from __future__ import print_function
from Monoencoder_Load import training_data
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.layers import Conv2D

# Run this to rebuild the Neural Network and save it to this device.

# x_train, y_train, x_test, y_test = training_data(6000)
# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
# y_train = keras.utils.to_categorical(y_train, 4)
# y_test = keras.utils.to_categorical(y_test, 4)
# inputs = keras.Input(shape=(256, 4))

# model = Sequential()

# model.add(Conv2D(4, (1, 1), padding='same'))
# model.add(Activation('relu'))
# model.add(Dense(256))
# model.add(Activation('softmax'))

# model.compile(loss='categorical_crossentropy',
              # optimizer=keras.optimizers.RMSprop(learning_rate=0.001, decay=1e-6),
              # metrics=['accuracy'])

# model.fit(x_train, y_train, batch_size=20, epochs=10, validation_data=(x_test, y_test), shuffle=True)
# scores = model.evaluate(x_test, y_test, verbose=2)
# print('Test loss:', scores[0])
# print('Test accuracy:', scores[1])

# model.save('Monoencoder_CNN')


def method_select(neural_net, case):
    selection = neural_net(case, training=False)
    return selection

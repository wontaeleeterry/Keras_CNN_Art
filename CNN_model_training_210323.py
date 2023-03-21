from tensorflow import keras
from tensorflow.keras.layers import Dropout, Dense
from tensorflow.keras.layers import Flatten, Convolution2D, MaxPooling2D
import numpy as np

X_train, X_test, Y_train, Y_test = np.load('./img_data.npy', allow_pickle=True)

categories = ["Cezanne", "Gauguin", "Gogh", "Klimt", "Mondrian", "Monet", "Picasso", ]
num_classes = len(categories)

model = keras.Sequential()
model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=X_train.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 주석처리하면 트레이닝 시간이 더 많이 소요
# model.add(Convolution2D(64, (3, 3)))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(num_classes, activation='softmax'))
# model.add(Dense(num_classes, activation='sigmoid'))

# 완전연결 네트워크 - https://jackyoon5737.tistory.com/136
# 단일/다중 라벨 : https://wikidocs.net/84581
# model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# optimizer : adam,  rmsprop
model.fit(X_train, Y_train, batch_size=10, epochs=50)

model.save('Train.h5')

# 출처 : https://twinw.tistory.com/252

import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

groups_folder_path = "/Users/wontaelee/PycharmProjects/CNN_Art_Pjt_mac_210325/cnn_sample/"
categories = ["Cezanne", "Gauguin", "Gogh", "Klimt", "Mondrian", "Monet", "Picasso"]

num_classes = len(categories)

image_w = 250
image_h = 200

X = []
Y = []

for idex, categorie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idex] = 1
    image_dir = groups_folder_path + categorie + '/'

# .DS_Store 파일을 읽는 문제점(210421) 해결
# ttps://stackoverflow.com/questions/48001890/how-to-read-images-from-a-directory-with-python-and-opencv
# 각 경로에 저장된 이미지 파일을 정확하게 jpg 파일 사용할 것 : 임의로 파일 속성명을 일괄 지정하여 발생하는 문제점

    for top, dir, f in os.walk(image_dir):
        for filename in f:
            if not filename.startswith('.'):   # Mac에서 : ".DS_Store" 파일을 읽는 문제점 해결을 위한 코드 추가
                filename = str(filename)       # 코드 추가
                print(image_dir + filename)
                img = cv2.imread(image_dir + filename)
                img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
                X.append(img/256)
                Y.append(label)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
xy = (X_train, X_test, Y_train, Y_test)

np.save("./img_data.npy", xy)
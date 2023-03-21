import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

categories = ["Cezanne", "Gauguin", "Gogh", "Klimt", "Mondrian", "Monet", "Picasso"]

def Dataization(img_path):
    image_w = 250
    image_h = 200   # 28 -> 200 으로 변경 / 그림을 상세하게 보는 효과? (210324)
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w / img.shape[1], fy=image_h / img.shape[0])
    return (img / 256)

src = []
name = []
test = []
image_dir = './predict_sample/'

for file in os.listdir(image_dir):
    if (file.find('.jpg') != -1):
        src.append(image_dir + file)
        name.append(file)
        test.append(Dataization(image_dir + file))

# 0~6까지 값을 출
test = np.array(test)

# model = load_model('Train_optimizer_Adam_211209.h5')
# model = load_model('Train_categorical_crossentp_Adam.h5')
model = load_model('Train.h5')

predict = model.predict_classes(test)
probabilities = model.predict_proba(test)

np.set_printoptions(formatter={'float': lambda x: "{0:0.1f}".format(x)})
print(probabilities)
print(predict)

for i in range(len(test)):
    print(name[i] + " : , Predict : " + str(categories[predict[i]]))

# 예측 결과의 정확도를 확률로 표시 해준는 옵션? (210426, 아이디어) (211209, probability 추가)
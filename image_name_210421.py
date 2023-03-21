import os

def changeName(path, cName):
    i = 1
    for filename in os.listdir(path):
        print(path + filename, '=>', path + str(cName) + str(i) + '.jpg')
        os.rename(path + filename, path + str(cName) + str(i) + '.jpg')
        i += 1

# 문제점 -> 이미 동일한 이름의 파일이 있는 경우, 중복 파일이 사라지는 문제점
# 여러번 실행시키면 안됨 : 한 번만 실행하던지, 파일 이름 옵션을 변경할

changeName('/Users/wontaelee/PycharmProjects/CNN_Art_Pjt_mac_210325/cnn_sample/Cezanne/', 'Cezanne')
# changeName('/Users/wontaelee/PycharmProjects/CNN_Art_Pjt_mac_210325/cnn_sample/Gauguin/', 'Gauguin')
# changeName('/Users/wontaelee/PycharmProjects/CNN_Art_Pjt_mac_210325/cnn_sample/Gogh/', 'Gogh')
# changeName('/Users/wontaelee/PycharmProjects/CNN_Art_Pjt_mac_210325/cnn_sample/Klimt/', 'Klimt')
# changeName('/Users/wontaelee/PycharmProjects/CNN_Art_Pjt_mac_210325/cnn_sample/Mondrian/', 'Mondrian')
# changeName('/Users/wontaelee/PycharmProjects/CNN_Art_Pjt_mac_210325/cnn_sample/Monet/', 'Monet')
# changeName('/Users/wontaelee/PycharmProjects/CNN_Art_Pjt_mac_210325/cnn_sample/Picasso/', 'Picasso')
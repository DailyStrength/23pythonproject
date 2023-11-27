a = 'a'
b = 'b'

while True:
    a = input("영어 단어를 입력하세요: ")
    if a == 'q':
        break
    b = input("한국어 뜻을 입력하세요: ")
    if b == 'q':
        break
    with open('vocabulary.txt', 'a') as f:
        f.write("{}: ".format(a))
        f.write("{}\n".format(b))
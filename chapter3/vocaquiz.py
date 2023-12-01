with open("vocabulary.txt", "r") as file:
    for line in file:
        line
        if answer == line:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(line))
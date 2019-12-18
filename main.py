import os


def main():
    if os.path.exists("./data.txt") is False:
        print("data file not exists")
        return

    # Read data
    f = open("./data.txt")
    row = f.readlines()
    ja_animal_list = []

    for line in row:
        line = list(line.strip().split(','))
        tmp = []
        for i in line:
            tmp.append(str(i))
        ja_animal_list.append(tmp)

    f = open("./thai_data.txt")
    row = f.readlines()
    thai_data = []
    for line in row:
        thai_data.append(line.strip())
    f.close()

    run = True
    while run:
        thai = ""
        thai = input("Please input thai onomatopoeia:\n\
        (bokbok, mewmew, jibjib, momo, aooaoo,\n\
        aeuaeaaea, gapgap, baba, opop, soosoo,\n\
        gaga, humhum, pantpant, jeiujeiu,\n\
        jeetjeet, heyhey, woowoo, koo,\n\
        quit with \"q\")\n")

        # quit
        if thai == "q":
            run = False
            continue

        # if the input not in thai_data.txt continue
        thai_label = False
        for i in thai_data:
            if thai == i:
                thai_label = True
                break
        if thai_label is False:
            continue

        # wight summing
        wight = []
        for i in ja_animal_list:
            wight_tmp = 0
            for k in range(0, len(thai)):
                if len(i[0]) - 1 < k:
                    break
                if i[0][k] == thai[k]:
                    wight_tmp += 1
            if len(thai) == len(i[0]):
                wight_tmp += 1
            wight.append(wight_tmp)
        print(wight)
        # output
        if wight.count(max(wight)) == 1:
            print("The animal is a " + ja_animal_list[wight.index(max(wight))][1])
        else:
            max_wight_index = []
            for i in range(0, len(wight)):
                if wight[i] == max(wight):
                    max_wight_index.append(i)
            print("The animal may be a ", end='')
            k = 0
            for i in max_wight_index:
                print(str(ja_animal_list[i][1]), end='')
                k += 1
                if k == len(max_wight_index):
                    print("")
                    break
                print(" or a ", end='')


main()

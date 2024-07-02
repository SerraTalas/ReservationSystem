seats1 = []
seats2 = []
seats3 = []
seats4 = []
prices = []
end1 = []
end2 = []
end3 = []
end4 = []
total = 0
discount = 0
List = list(range(5, 0, -1))+list(range(16, 21))

file = open("indirim.txt", "r")
for line in file:
    prices.append(line.strip().split("-"))


def seat_prices(k, num):
    print("\n")
    if k == int(prices[1][0]) and int(prices[5][1]) <= num <= int(prices[5][2]):
        total = int(prices[1][1]) * num
        discount = ((total) * int(prices[5][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end1.append(price)

    elif k == int(prices[1][0]) and int(prices[6][1]) <= num <= int(prices[6][2]):
        total =  int(prices[1][1]) * num
        discount = ((total) * int(prices[6][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end1.append(price)

    elif k == int(prices[1][0]) and int(prices[7][1]) <= num <= int(prices[0][1]):
        total = int(prices[1][1]) * num
        discount =  ((total) * int(prices[7][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end1.append(price)

    elif k == int(prices[1][0]):
        total = int(prices[1][1]) * num
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim: 0", "Net tutar:", total)
        end1.append(total)

    elif k == int(prices[2][0]) and int(prices[8][1]) <= num <= int(prices[8][2]):
        total = int(prices[2][1]) * num
        discount = ((total) * int(prices[8][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end2.append(price)

    elif k == int(prices[2][0]) and int(prices[9][1]) <= num <= int(prices[9][2]):
        total = int(prices[2][1]) * num
        discount = ((total) * int(prices[9][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end2.append(price)

    elif k == int(prices[2][0]) and int(prices[10][1]) <= num <= int(prices[0][1]):
        total = int(prices[2][1]) * num
        discount = ((total) * int(prices[10][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end2.append(price)

    elif k == int(prices[2][0]):
        total = int(prices[2][1]) * num
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim: 0", "Net tutar:", total)
        end2.append(total)

    elif k == int(prices[3][0]) and int(prices[11][1]) <= num <= int(prices[11][2]):
        total = int(prices[3][1]) * num
        discount = ((total) * int(prices[11][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end3.append(price)

    elif k == int(prices[3][0]) and int(prices[12][1]) <= num <= int(prices[12][2]):
        total = int(prices[3][1]) * num
        discount = ((total) * int(prices[12][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end3.append(price)

    elif k == int(prices[3][0]) and int(prices[13][1]) <= num <= int(prices[0][1]):
        total = int(prices[3][1]) * num
        discount = ((total) * int(prices[13][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end3.append(price)

    elif k == int(prices[3][0]):
        total = int(prices[3][1]) * num
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim: 0", "Net tutar:", total)
        end3.append(total)

    elif k == int(prices[4][0]) and int(prices[14][1]) <= num <= int(prices[14][2]):
        total = int(prices[4][1]) * num
        discount = ((total) * int(prices[14][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end4.append(price)

    elif k == int(prices[4][0]) and int(prices[15][1]) <= num <= int(prices[15][2]):
        total = int(prices[4][1]) * num
        discount = ((total) * int(prices[15][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end4.append(price)

    elif k == int(prices[4][0]) and int(prices[16][1]) <= num <= int(prices[0][1]):
        total = int(prices[4][1]) * num
        discount = ((total) * int(prices[16][3])) / 100
        price = total - discount
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim:", discount, "Net tutar:", price)
        end4.append(price)

    elif k == int(prices[4][0]):
        total = int(prices[4][1]) * num
        print("Bilet adedi:", num, "Toplam tutar:", total, "Yapılan indirim: 0", "Net tutar:", total)
        end4.append(total)

    print("\n")


def endorsement():
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    for i in end1:
        total1 += i
    for i in end2:
        total2 += i
    for i in end3:
        total3 += i
    for i in end4:
        total4 += i
    print("1. kategorinin cirosu: ", total1)
    print("2. kategorinin cirosu: ", total2)
    print("3. kategorinin cirosu: ", total3)
    print("4. kategorinin cirosu: ", total4)
    print("Toplam ciro ", total1+total2+total3+total4)
    print("\n")


def display_seats1(num):
    control = 0
    emptySeats = 100 - len(seats1)
    if num <= emptySeats:
        print("Koltuklarınız: ", end="")
        for i in range(1, 11):
            for j in range(6, 16):
                if (i, j) not in seats1:
                    if control != num:
                        print(i, "-", j, end=" ")
                        seats1.append((i, j))
                    else:
                        break
                    control += 1
        seat_prices(1, num)
    else:
        print("Yeterli sayida koltuk kalmamistir bos koltuk sayisi: ", emptySeats)
    print("\n")


def display_seats2(num):
    control = 0
    emptySeats = 100 - len(seats2)
    if num <= emptySeats:
        print("Koltuklarınız: ", end="")
        for i in range(1, 11):
            for j in List:
                if (i, j) not in seats2:
                    if control != num:
                        print(i, "-", j, end=" ")
                        seats2.append((i, j))
                    else:
                        break
                    control += 1
        seat_prices(2, num)
    else:
        print("Yeterli sayida koltuk kalmamistir bos koltuk sayisi: ", emptySeats)
    print("\n")


def display_seats3(num):
    control = 0
    emptySeats = 100 - len(seats3)
    if num <= emptySeats:
        print("Koltuklarınız: ", end="")
        for i in range(11, 21):
            for j in range(6, 16):
                if (i, j) not in seats3:
                    if control != num:
                        print(i, "-", j, end=" ")
                        seats3.append((i, j))
                    else:
                        break
                    control += 1
        seat_prices(3, num)
    else:
        print("Yeterli sayida koltuk kalmamistir bos koltuk sayisi: ", emptySeats)
    print("\n")


def display_seats4(num):
    control = 0
    emptySeats = 100 - len(seats4)
    if num <= emptySeats:
        print("Koltuklarınız: ", end="")
        for i in range(11, 21):
            for j in List:
                if (i, j) not in seats4:
                    if control != num:
                        print(i, "-", j, end=" ")
                        seats4.append((i, j))
                    else:
                        break
                    control += 1
        seat_prices(4, num)
    else:
        print("Yeterli sayida koltuk kalmamistir bos koltuk sayisi: ", emptySeats)
    print("\n")


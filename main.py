import funcs
from funcs import display_seats1, display_seats2, display_seats3, display_seats4, endorsement
choice = -1
p = 0
num = 0
k = 0
while choice != 0:
    s = "ANA MENÜ"
    m = s.center(15, "*")
    print(m)
    print("1. Rezervasyon\n2. Salonu Yazdır\n3. Yeni Etkinlik\n4. Toplam Ciro\n0. Çıkış")
    print("*"*15)
    choice = int(input("Seçiminiz?  "))

    if choice == 0:
        exit(1)

    if choice == 1:
        k = int(input("Kategori(1-4) ?"))
        if k < 1 or k > 4:
            k = int(input("Kategori(1-4) ?"))
        num = int(input("Bilet adedi(1-30)? "))
        if num < 1 or num > 30:
            print("Tek seferde alinabilecek bilet sayisini gecmeyin lutfen\n")
            print(m)
            print("1. Rezervasyon\n2. Salonu Yazdır\n3. Yeni Etkinlik\n4. Toplam Ciro\n0. Çıkış")
            print("*" * 15)
            choice = int(input("Seçiminiz?  "))

        if k == 1:
            display_seats1(num)

        if k == 2:
            display_seats2(num)

        if k == 3:
           display_seats3(num)

        if k == 4:
            display_seats4(num)

    if choice == 2:
        seats = funcs.seats1 + funcs.seats2 + funcs.seats3 + funcs.seats4
        for i in range(1, 21):
            for j in range(1, 21):
                if (i, j) in seats:
                    print("x", end="")
                else:
                    print("-", end="")
            print("\n")

    if choice == 3:
        funcs.seats1 = []
        funcs.seats2 = []
        funcs.seats3 = []
        funcs.seats4 = []
        num = 0
        funcs.end1 = []
        funcs.end2 = []
        funcs.end3 = []
        funcs.end4 = []
        print("Salon boşaltıldı")
        print("\n")

    if choice == 4:
        endorsement()


peselFromUser = input('Podaj numer pesel i kliknij enter...')

badPesel = False

def calculateControlNumber(pesel):
    tableOfWeight = [1,3,7,9,1,3,7,9,1,3]
    sum = 0
    i = 0
    for v in pesel:
        number = int(v)*tableOfWeight[i]
        if number >= 10:
            number = number % 10
        sum = sum + number
        i+=1
    print("suma: "+str(sum))
    if sum > 10:
        sum = 10 - sum % 10
    else:
        sum = 10 - sum
    if sum == 10:
        return 0
    return sum

def isMonthCorrect(peselFromUser):
    correctMonth = False
    if 12 >= int(peselFromUser[2:4]) >= 1:
        print("lata 1900")
        if isDayCorrect(peselFromUser):
            correctMonth = True
    elif 92 >= int(peselFromUser[2:4]) >= 81:
        print("lata 1800")
        if isDayCorrect(peselFromUser):
            correctMonth = True
    elif 32 >= int(peselFromUser[2:4]) >= 21:
        print("lata 2000")
        if isDayCorrect(peselFromUser):
            correctMonth = True
    elif 52 >= int(peselFromUser[2:4]) >= 41:
        print("lata 2100")
        if isDayCorrect(peselFromUser):
            correctMonth = True
    elif 72 >= int(peselFromUser[2:4]) >= 61:
        print("lata 2200")
        if isDayCorrect(peselFromUser):
            correctMonth = True
    return correctMonth

def isDayCorrect(peselFromUser):
    correctDayOfMonth = False
    if int(peselFromUser[2:4]) in [1, 3, 5, 7, 8, 10, 12]+[21, 23, 25, 27, 28, 30, 32]+[81, 83, 85, 87, 88, 90, 92]:
        if int(peselFromUser[4:6]) <= 31:
            correctDayOfMonth = True
    if int(peselFromUser[2:4]) in [4, 6, 9, 11]+[24, 26, 29 ,31]+[84, 86, 89, 91]:
        if int(peselFromUser[4:6]) <= 30:
            correctDayOfMonth = True
    if int(peselFromUser[0:2]) % 4 == 0:  # rok przestępny, czyli luty ma 29 dni
        if int(peselFromUser[2:4]) in [2, 22, 82]:
            if int(peselFromUser[4:6]) <= 29:
                correctDayOfMonth = True
    if not int(peselFromUser[0:2]) % 4 == 0:  # rok nie jest przestępny, czyli luty ma 28 dni
        if int(peselFromUser[2:4]) in [2, 22, 82]:
            if int(peselFromUser[4:6]) <= 28:
                correctDayOfMonth = True
    if correctDayOfMonth:
        print("Dzień w peselu poprawny")
    return correctDayOfMonth

#pesel ma 11 cyfr
if len(peselFromUser) == 11:
    # RR - to 2 ostanie cyfry roku urodzenia, minimalnie może być 0, maksymalnie może być 99
    print("Długość peselu poprawna")
    if 99 >= int(peselFromUser[0:2]) >= 0:
        print("Rok w peselu poprawny")
        if isMonthCorrect(peselFromUser):
            print("Miesiąc w peselu poprawny")
            if 31 >= int(peselFromUser[4:6]) >= 1:
                print("Zakres dni w peselu poprawny")
                print("Liczba kontrolna: " + str(calculateControlNumber(peselFromUser[0:10])))
                if calculateControlNumber(peselFromUser[0:10]) == int(peselFromUser[10:11]):
                    print("Suma kontrolna w peselu poprawna")
                    print("Pesel poprawny!")
                    if int(peselFromUser[9:10]) % 2 == 0:
                        plec = "K"
                    elif not int(peselFromUser[9:10]) % 2 == 0:
                        plec = "M"
                    print("Płeć osoby, do której należy pesel (M/K):" + plec)
                    badPesel = True
if not badPesel:
    print("Pesel niepoprawny!")
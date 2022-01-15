print("""
▄▀█ █░░ █░░   █▀▀ █▀█ █▀█ █▄█ █▀█ █ █▀▀ █░█ ▀█▀   █▀▄▀█ ░ █▀▀ █▀ █▀ ▄▀█ █▀▄▀█   ▀█ █▀█ ▀█ ▀█
█▀█ █▄▄ █▄▄   █▄▄ █▄█ █▀▀ ░█░ █▀▄ █ █▄█ █▀█ ░█░   █░▀░█ ▄ ██▄ ▄█ ▄█ █▀█ █░▀░█   █▄ █▄█ █▄ █▄
powerd by Mohammed Essam Al-Qershi
""")

one1 = "░░███╗░░\t"
one2 = "░████║░░\t"
one3 = "██╔██║░░\t"
one4 = "╚═╝██║░░\t"
one5 = "███████╗\t"
one6 = "╚══════╝\t"

two1 = "██████╗░\t"
two2 = "╚════██╗\t"
two3 = "░░███╔═╝\t"
two4 = "██╔══╝░░\t"
two5 = "███████╗\t"
two6 = "╚══════╝\t"

three1 = "██████╗░\t"
three2 = "╚════██╗\t"
three3 = "░█████╔╝\t"
three4 = "░╚═══██╗\t"
three5 = "██████╔╝\t"
three6 = "╚═════╝░\t"

four1 = "░░██╗██╗\t"
four2 = "░██╔╝██║\t"
four3 = "██╔╝░██║\t"
four4 = "███████║\t"
four5 = "╚════██║\t"
four6 = "░░░░░╚═╝\t"

five1 = "███████╗\t"
five2 = "██╔════╝\t"
five3 = "██████╗░\t"
five4 = "╚════██╗\t"
five5 = "██████╔╝\t"
five6 = "╚═════╝░\t"

six1 = "░█████╗░\t"
six2 = "██╔═══╝░\t"
six3 = "██████╗░\t"
six4 = "██╔══██╗\t"
six5 = "╚█████╔╝\t"
six6 = "░╚════╝░\t"

seven1 = "███████╗\t"
seven2 = "╚════██║\t"
seven3 = "░░░░██╔╝\t"
seven4 = "░░░██╔╝░\t"
seven5 = "░░██╔╝░░\t"
seven6 = "░░╚═╝░░░\t"

eight1 = "░█████╗░\t"
eight2 = "██╔══██╗\t"
eight3 = "╚█████╔╝\t"
eight4 = "██╔══██╗\t"
eight5 = "╚█████╔╝\t"
eight6 = "░╚════╝░\t"

nine1 = "░█████╗░\t"
nine2 = "██╔══██╗\t"
nine3 = "╚██████║\t"
nine4 = "░╚═══██║\t"
nine5 = "░█████╔╝\t"
nine6 = "░╚════╝░\t"


zero1 = "░█████╗░\t"
zero2 = "██╔══██╗\t"
zero3 = "██║░░██║\t"
zero4 = "██║░░██║\t"
zero5 = "╚█████╔╝\t"
zero6 = "░╚════╝░\t"


def printNmber(first, second):
    print("{} {}".format(first.expandtabs(2), second))

def secondNumber(res, *first):
    if res == 0 :
        printNmber(first[0], zero1)
        printNmber(first[1], zero2)
        printNmber(first[2], zero3)
        printNmber(first[3], zero4)
        printNmber(first[4], zero5)
        printNmber(first[5], zero6)
    elif res == 1 :
        printNmber(first[0], one1)
        printNmber(first[1], one2)
        printNmber(first[2], one3)
        printNmber(first[3], one4)
        printNmber(first[4], one5)
        printNmber(first[5], one6)
    elif res == 2 :
        printNmber(first[0], two1)
        printNmber(first[1], two2)
        printNmber(first[2], two3)
        printNmber(first[3], two4)
        printNmber(first[4], two5)
        printNmber(first[5], two6)
    elif res == 3 :
        printNmber(first[0], three1)
        printNmber(first[1], three2)
        printNmber(first[2], three3)
        printNmber(first[3], three4)
        printNmber(first[4], three5)
        printNmber(first[5], three6)
    elif res == 4 :
        printNmber(first[0], four1)
        printNmber(first[1], four2)
        printNmber(first[2], four3)
        printNmber(first[3], four4)
        printNmber(first[4], four5)
        printNmber(first[5], four6)
    elif res == 5 :
        printNmber(first[0], five1)
        printNmber(first[1], five2)
        printNmber(first[2], five3)
        printNmber(first[3], five4)
        printNmber(first[4], five5)
        printNmber(first[5], five6)
    elif res == 6 :
        printNmber(first[0], six1)
        printNmber(first[1], six2)
        printNmber(first[2], six3)
        printNmber(first[3], six4)
        printNmber(first[4], six5)
        printNmber(first[5], six6)
    elif res == 7 :
        printNmber(first[0], seven1)
        printNmber(first[1], seven2)
        printNmber(first[2], seven3)
        printNmber(first[3], seven4)
        printNmber(first[4], seven5)
        printNmber(first[5], seven6)
    elif res == 8 :
        printNmber(first[0], eight1)
        printNmber(first[1], eight2)
        printNmber(first[2], eight3)
        printNmber(first[3], eight4)
        printNmber(first[4], eight5)
        printNmber(first[5], eight6)
    elif res == 9 :
        printNmber(first[0], nine1)
        printNmber(first[1], nine2)
        printNmber(first[2], nine3)
        printNmber(first[3], nine4)
        printNmber(first[4], nine5)
        printNmber(first[5], nine6)

def enterNumber():
    num = input("Enter Any Number between 0 to 99: ")
    print()
    num = num.zfill(2)
    res = [int(x) for x in str(num)]

    if res[0] == 0 :
        secondNumber(res[1], zero1, zero2, zero3, zero4, zero5, zero6)
    elif res[0] == 1 :
        secondNumber(res[1], one1, one2, one3, one4, one5, one6)
    elif res[0] == 2 :
        secondNumber(res[1], two1, two2, two3, two4, two5, two6)
    elif res[0] == 3 :
        secondNumber(res[1], three1, three2, three3, three4, three5, three6)
    elif res[0] == 4 :
        secondNumber(res[1], four1, four2, four3, four4, four5, four6)
    elif res[0] == 5 :
        secondNumber(res[1], five1, five2, five3, five4, five5, five6)
    elif res[0] == 6 :
        secondNumber(res[1], six1, six2, six3, six4, six5, six6)
    elif res[0] == 7 :
        secondNumber(res[1], seven1, seven2, seven3, seven4, seven5, seven6)
    elif res[0] == 8 :
        secondNumber(res[1], eight1, eight2, eight3, eight4, eight5, eight6)
    elif res[0] == 9 :
        secondNumber(res[1], nine1, nine2, nine3, nine4, nine5, nine6)
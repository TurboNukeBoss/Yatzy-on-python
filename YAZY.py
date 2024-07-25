import random
def check_full(red,blue):
    done = 1
    for i in range(len(red)):
        if red[i] == 0:
            done = 0
    for i in range(len(blue)):
        if blue[i] == 0:
            done = 0
    return done
def valdt(qn,options):
    x = input(qn)
    if x not in options or len(x)!= 1:
        print("Input is not valid, try again.")
        return valdt(qn,options)
    else:
        return int(x)
def cal_length_1(x):
    return (5 - len(str(x))) // 2
def cal_length_2(x):
    return int((5 - len(str(x))) / 2 + (5 - len(str(x))) % 2)
def cal_length_3(x):
    return (6 - len(str(x))) // 2
def cal_length_4(x):
    return int((6 - len(str(x))) // 2 + (6 - len(str(x))) % 2)
def cal_lengths(red_val,blu_val):
    w,x,y,z = cal_length_1(red_val),cal_length_2(red_val), cal_length_3(blu_val), cal_length_4(blu_val)
    return w, x, y, z
def print_table(red_lst,blu_lst):
    longst = "All 5 same  "
    ##HEADING
    print(len(longst) * " " + "|" + " red " + "|" + " blue " + "|")
    ##DICE NUMBERS
    w, x, y, z = cal_lengths(red_lst[0],blu_lst[0])
    print("one" + (len(longst) - 3)* " " + "|" + w * " " + str(red_lst[0]) + x * " " + "|" + y * " "+ str(blu_lst[0]) + z * " " + "|")
    w, x, y, z = cal_lengths(red_lst[1],blu_lst[1])
    print("two" + (len(longst) - 3)* " " + "|" + w * " " + str(red_lst[1]) + x * " " + "|" + y * " "+ str(blu_lst[1]) + z * " " + "|")
    w, x, y, z = cal_lengths(red_lst[2],blu_lst[2])
    print("three" + (len(longst) - 5)* " " + "|" + w * " " + str(red_lst[2]) + x * " " + "|" + y * " "+ str(blu_lst[2]) + z * " " + "|")
    w, x, y, z = cal_lengths(red_lst[3],blu_lst[3])
    print("four" + (len(longst) - 4)* " " + "|" + w * " " + str(red_lst[3]) + x * " " + "|" + y * " "+ str(blu_lst[3]) + z * " " + "|")
    w, x, y, z = cal_lengths(red_lst[4],blu_lst[4])
    print("five" + (len(longst) - 4)* " " + "|" + w * " " + str(red_lst[4]) + x * " " + "|" + y * " "+ str(blu_lst[4]) + z * " " + "|")
    w, x, y, z = cal_lengths(red_lst[5],blu_lst[5])
    print("six" + (len(longst) - 3)* " " + "|" + w * " " + str(red_lst[5]) + x * " " + "|" + y * " "+ str(blu_lst[5]) + z * " " + "|")
    ##REST OF DA TABLE
    w, x, y, z = cal_lengths(red_lst[6],blu_lst[6])
    print("3 same" + (len(longst) - 6)* " " + "|" + w * " " + str(red_lst[6]) + x * " " + "|" + y * " "+ str(blu_lst[6]) + z * " " + "|")
    w, x, y, z = cal_lengths(red_lst[7],blu_lst[7])
    print("4 same" + (len(longst) - 6)* " " + "|" + w * " " + str(red_lst[7]) + x * " " + "|" + y * " "+ str(blu_lst[7]) + z * " " + "|")
    w, x, y, z = cal_lengths(red_lst[8],blu_lst[8])
    print("3, 2" + (len(longst) - 4)* " " + "|" + w * " " + str(red_lst[8]) + x * " " + "|" + y * " "+ str(blu_lst[8]) + z * " " + "|")
    w, x, y, z = cal_lengths(red_lst[9],blu_lst[9])
    print("inc ord" + (len(longst) - 7)* " " + "|" + w * " " + str(red_lst[9]) + x * " " + "|" + y * " "+ str(blu_lst[9]) + z * " " + "|")
    w, x, y, z = cal_lengths(red_lst[10],blu_lst[10])
    print("All 5 same" + (len(longst) - 10)* " " + "|" + w * " " + str(red_lst[10]) + x * " " + "|" + y * " "+ str(blu_lst[10]) + z * " " + "|")
def roll_dice(x):
    genr = []
    for i in range(x):
        genr.append(random.randint(1,6))
    return genr
def display_dice(x,y):
    print("Your dice are: " + str(x))
    kept = ""
    for i in range(len(y)):
        if y[i] != 0:
            if kept != "":
                kept += ", "
            kept += str(y[i])
    if y == [0,0,0,0,0]:
        print("You have no kept dice.")
    else:
        print("Your kept dice are " + kept)
def row_filter(x, y):
    if x >= 1 and x <= 6:
        num_of = 0
        for i in range(5):
            if x == y[i]:
                num_of += 1
        return num_of * x
    elif x == 7:
        is_there = 0
        for i in range(5):
            checked = y[i]
            num_of = 0
            for j in range(5):
                if checked == y[j]:
                    num_of += 1
                    if num_of == 3:
                        is_there = 1
                        break
        if is_there == 1:
            sum = 0
            for i in range(5):
                sum += y[i]
            return sum
        else:
            return 0
    elif x == 8:
        is_there = 0
        for i in range(5):
            checked = y[i]
            num_of = 0
            for j in range(5):
                if checked == y[j]:
                    num_of += 1
                    if num_of == 4:
                        is_there = 1
                        break
        if is_there == 1:
            sum = 0
            for i in range(5):
                sum += y[i]
            return sum
        else:
            return 0
    elif x == 9:
        is_there = 0
        rep_3 = 0
        for i in range(5):
            checked = y[i]
            num_of = 0
            for j in range(5):
                if checked == y[j]:
                    num_of += 1
                    if num_of == 3:
                        is_there += 2
                        rep_3 = y[j]
                        break
            if is_there == 2:
                break
        if is_there == 2:
            for i in range(3):
                y.remove(rep_3)
            if y[0] == y[1]:
                is_there -= 1
        if is_there == 1:
            return 25
        else:
            return 0
    elif x == 10:
        y.sort()
        string = ""
        for i in range(5):
            string += str(y[i])
        if "12345" in string or "23456" in string:
            return 40
        else:
            return 0
    elif x == 11:
        first = y[0]
        for i in range(5):
            if y[i] != first:
                return 0
        return 50
def turn(chooselst,vallst,otherlst,colour):
    dice_val = roll_dice(5)
    kept_dice = [0,0,0,0,0]
    display_dice(dice_val,kept_dice)
    turn_end = 0
    dice_roll = 1
    while turn_end == 0:
        if colour == 1:
            print_table(vallst,otherlst)
        else:
            print_table(otherlst,vallst)
        if dice_roll == 3:
            choice = valdt("1.Select row" + "\n", "1") + 2
        else:
            choice = valdt("1.Roll dice" + "\n" + "2.Select/Deselect dice" + "\n" + "3.Select row" + "\n", "123")
        if choice == 1:
            if dice_val == kept_dice:
                print("You cannot roll dice since you selected all of them")
            else:
                for i in range(5):
                    if dice_val[i] != kept_dice[i]:
                        dice_val[i] = roll_dice(1)[0]
                dice_roll += 1
                print("You have " + str(3 - dice_roll) + " dice roll(s) left.")
            display_dice(dice_val, kept_dice)
        elif choice == 2:
            chosen_die = int(valdt("Which die do you want to select? (As in 1(st),2(nd),3(rd))" + "\n","12345")) - 1
            if kept_dice[chosen_die] == 0:
                kept_dice[chosen_die] = dice_val[chosen_die]
                print("You have selected " + str(dice_val[chosen_die]))
                display_dice(dice_val, kept_dice)
            else:
                kept_dice[chosen_die] = 0
                print("You have deselected " + str(dice_val[chosen_die]))
                display_dice(dice_val, kept_dice)
        elif choice ==  3:
            rows_avail = ""
            for i in range(11):
                if chooselst[i] == 0:
                    rows_avail += str(i + 1)
            x = int(valdt("Which row do you want to select?" + "\n", rows_avail)) - 1
            chooselst[x] = 1
            vallst[x] = row_filter(x + 1,dice_val)
            turn_end = 1
    return chooselst,vallst
def yazy():
    red_chooselst = [0,0,0,0,0,0,0,0,0,0,0]
    blu_chooselst = [0,0,0,0,0,0,0,0,0,0,0]
    red_lst = [0,0,0,0,0,0,0,0,0,0,0]
    blu_lst = [0,0,0,0,0,0,0,0,0,0,0]
    all_filled = 0
    while all_filled == 0:
        print("It is now red's turn!")
        red_chooselst, red_lst = turn(red_chooselst,red_lst,blu_lst,1)
        print("It is now blue's turn!")
        blu_chooselst, blu_lst = turn(blu_chooselst,blu_lst,red_lst,2)
        all_filled = check_full(red_chooselst,blu_chooselst)
yazy()

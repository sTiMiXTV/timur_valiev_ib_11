kol_people = int(input('How many people: '))
iq_people = 0
sum_iq = 0
for j in range(1, kol_people + 1):
    iq = int(input('How much of: '))
    sredn = (iq + sum_iq) / j
    sum_iq += iq
    if iq == sredn:
        print('0')
    elif iq > sredn:
        print('>')
    elif iq < sredn:
        print('<')
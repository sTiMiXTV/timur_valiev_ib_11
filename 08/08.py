coin = input()
combomax = 0
combo = 0
for i in coin:
    if i == "о":
        combo += 1
        if combo > combomax:
            combomax = combo
    else:
        combo = 0
print(combomax)

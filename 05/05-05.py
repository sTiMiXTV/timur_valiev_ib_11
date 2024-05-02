coshka_v_stroke = False
text = ""
kol_strokes = 0
number_cot = 0
while "СТОП" != text:
    text = input("Enter a text: ")
    kol_strokes += 1
    if ('Кот' in text) or ('кот' in text):
        coshka_v_stroke = True
        if coshka_v_stroke:
            number_cot = kol_strokes
            break
if coshka_v_stroke:
    print(number_cot)
else: print("-1")
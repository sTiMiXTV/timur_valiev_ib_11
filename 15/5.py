import math

def number_in_english(n):
    words_19 = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    words_99 = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if n <= 19:
        return words_19[n]
    
    edin = n % 10
    desat = math.floor(n / 10) % 10
    sot = math.floor(n / 100)
    word = words_99[desat - 2]
    if edin != 0:
        word += ' ' + words_19[edin]
    if sot != 0:
        word = words_19[sot] + ' hundred and ' + word
    return word

print(number_in_english(1).lower())

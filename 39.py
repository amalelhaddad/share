number_words = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

def number_to_words(num):
    if num &lt; 10:
        return number_words[num]
    else:
        return "Number is out of range"

# اختبار البرنامج
num = int(input("Enter a number: "))
print(number_to_words(num))

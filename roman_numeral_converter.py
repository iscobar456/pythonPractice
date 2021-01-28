import math


def int_to_roman():
    num = int(input("Enter a digit between 1-1000: "))
    initial_num = num
    while num < 1 or num > 1000:
        num = int(input("Try again: "))

    conv_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    end_numeral = ""
    numerals = list(conv_dict.keys())

    for n in range(len(conv_dict) - 1, -1, -1):
        divi_am = math.floor(num / conv_dict[numerals[n]])
        if divi_am < 4:
            for x in range(divi_am):
                end_numeral += numerals[n]
        else:
            end_numeral += numerals[n] + numerals[n + 1]

        num %= conv_dict[numerals[n]]

    print(f"The number {initial_num} in roman numerals is {end_numeral}")


if __name__ == '__main__':
    int_to_roman()

import math
import standards

description = """\
Converts any number in range 1-1000 to a roman numeral.

ex.
  1) 1 -> I
  2) 5 -> V
  3) 

"""
input_prompt = "Enter a number (n) where 0 < n < 1001: "
index_info = {
    "title": "Integer to Roman Numeral",
    "source": "https://youtu.be/9mFaPhwsAb4",
    "date": "2021-01-29"
}

def int_to_roman(num):
    initial_num = num

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


response_class = standards.Problem(
    description=description,
    run_function=int_to_roman,
    input_prompt=input_prompt
)

# Import statements
import standards


description = """\
Squares every digit in a number and concatenates them together.
ex.
  1) 7798 -> 49498164
"""

# If necessary, replace the following variable with an input generator.
input_generator = None

input_prompt = "Enter a number: "

index_info = {
    "title": "Square Every Digit",
    "source": "https://www.codewars.com/kata/546e2562b03326a88e000020/train/python",  # i.e. where I found this idea.
    "date": "2021-01-29",  # Format YYYY-MM-DD
    "time_spent": 0  # In seconds
}


def main_function(func_input):
    return "".join([str(int(x) ** 2) for x in str(func_input)])


response_class = standards.Problem(
    description=description,
    run_function=main_function,
    input_generator=input_generator,
    input_prompt=input_prompt,
    index_info=index_info
)

if __name__ == "__main__":
    i = input(input_prompt)
    print(i, main_function(i))

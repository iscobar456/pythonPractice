# Import statements
import standards


description = """\
"""

# If necessary, replace the following variable with an input generator.
input_generator = None

input_prompt = "Input: "

index_info = {
    "title": "",
    "source": "",  # i.e. where I found this idea.
    "date": "",  # Format YYYY-MM-DD
    "time_spent": ""
}


def main_function(func_input):
    pass


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

# Import statements
import standards
import random
import os, psutil

description = """\
Given a 2D array of numbers between 1 and 10 that represent diamonds, find out the smallest rectangular region that sums to a target number of diamonds.
If multiple rectangles are found, return all of them.

ex.

  4 5 0 2
  1 1 2 0
  1 0 2 1
  0 0 1 0

  outputs
  
  [
    [(1, 1), (1, 2)], 
    [(2, 2), (2, 3)], 
    [(2, 2), (3, 2)] 
  ]
  or
  - - - -
  - + + -
  - + + +
  - - + -
"""

input_prompt = "Number of diamonds to find on smallest piece of land: "


# If necessary, replace the following variable with an input generator.
def input_generator(size=(10, 10), dev=False):
    num_of_diamonds = int(input(input_prompt))

    if dev:
        dev_map = [
            [1, 5, 3, 7],
            [0, 0, 4, 4],
            [9, 2, 1, 6],
            [8, 2, 0, 10]
        ]
        return dev_map, num_of_diamonds

    diamond_map = []
    for r in range(size[0]):
        diamond_map.append([random.randint(1, 10) for n in range(size[1])])

    return diamond_map, num_of_diamonds


index_info = {
    "title": "Counting Diamonds",
    "source": "https://www.codewars.com/kata/5ff0fc329e7d0f0010004c03",  # i.e. where I found this idea.
    "date": "2021-01-30",  # Format YYYY-MM-DD
    "time_spent": ""
}


def main_function(func_input):
    diamond_map = func_input[0]
    target_diamond_amount = func_input[1]
    solutions = []

    top_left = [0, 0]
    bottom_right = [0, 0]

    process = psutil.Process(os.getpid())
    print(process.memory_info().rss / 10 ** 6)

    while True:
        rectangle_sum = 0
        # Crop by top left
        top_left_bound_applied = [r[top_left[1]:] for r in diamond_map[top_left[0]:]]
        # Crop by bottom right
        current_search = [r[:bottom_right[1]+1-top_left[1]] for r in top_left_bound_applied[:bottom_right[0]+1-top_left[0]]]

        for row in current_search:
            rectangle_sum += sum(row)

        if rectangle_sum < target_diamond_amount:  # If rectangle does not contain enough diamonds.
            if bottom_right[1] + 1 < len(diamond_map[0]):  # Expand rectangle to the right if possible.
                bottom_right[1] += 1
            else:
                # If rectangle cannot be expanded right, then expand down and set width to 1.
                if bottom_right[0] + 1 < len(diamond_map):
                    bottom_right[0] += 1
                    bottom_right[1] = top_left[1]
                else:
                    top_left[1] += 1
        else:  # If rectangle passes or has excess diamonds...
            if rectangle_sum == target_diamond_amount:
                solutions.append([(top_left[0], top_left[1]), (bottom_right[0], bottom_right[1])])

            if bottom_right[0] + 1 < len(diamond_map):  # Expand rectangle downwards if possible.
                bottom_right[0] += 1
                bottom_right[1] = top_left[1]
            else:  # If rectangle cannot be expanded downwards, shift top left bound.
                if top_left[1] + 1 != len(diamond_map):  # Shift top left bound right if possible.
                    top_left[1] += 1
                    bottom_right = top_left[:]
                else:
                    top_left[0] += 1
                    top_left[1] = 0
                    bottom_right = top_left[:]

        if top_left == [len(diamond_map) - 1, len(diamond_map[0]) - 1]:
            break

    def rsize(coord_pair):
        return str((coord_pair[1][0] - coord_pair[0][0]) * (coord_pair[1][1] - coord_pair[0][1]))

    scored_solutions = {}
    for solution in solutions:
        solution_score = rsize(solution)
        if solution_score not in scored_solutions:
            scored_solutions[solution_score] = [solution]
        else:
            scored_solutions[solution_score].append(solution)

    lowest_score = min([int(score) for score in scored_solutions.keys()])
    unsorted_solutions = scored_solutions[str(lowest_score)]
    sorted_solutions = sorted(unsorted_solutions, key=lambda s: (s[0][0], s[0][1]))

    return sorted_solutions


response_class = standards.Problem(
    description=description,
    run_function=main_function,
    input_generator=input_generator,
    input_prompt=input_prompt,
    index_info=index_info
)


if __name__ == "__main__":
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss / 10 ** 6)
    i = input_generator(size=(5, 5))
    print(main_function(i))

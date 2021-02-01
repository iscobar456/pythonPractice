# import standards
import random
import time
import math

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

    for row in diamond_map:
        print(row)
    print("is the diamond map")

    def map_transpose(input_map):
        input_map_transpose = [[] for column in range(len(input_map[0]))]
        for r in range(len(input_map)):
            for c in range(len(input_map[r-1])):
                input_map_transpose[c].append(input_map[r][c])
        return input_map_transpose

    diamond_map_transpose = map_transpose(diamond_map)

    def section_sum(map_section):
        total_sum = 0
        for row in map_section:
            total_sum += sum(row)
        return total_sum

    # Row splitting
    def split_map(input_map):
        splitting_time = time.time()
        viable_sections = []
        for col_width in range(len(input_map[0])):
            for col_num in range(len(input_map[0]) - col_width):
                sub_section = [vrow[col_num:col_num+col_width] for vrow in input_map]
                if section_sum(sub_section) >= target_diamond_amount:
                    viable_sections.append(sub_section)
        return viable_sections

    # Row splitting
    viable_row_sections = split_map(diamond_map_transpose)

    # Column splitting
    viable_col_sections = split_map(diamond_map)

    def search_for_solutions(viable_sections, revert=False):
        smallest_solution_area = len(diamond_map) * len(diamond_map[0])
        smallest_possible_solution_area = math.floor(target_diamond_amount / 10)
        while viable_sections:
            current_section = viable_sections[0]
            if len(current_section[0]) > smallest_solution_area:
                viable_sections.pop(0)
                continue
            for row_height in range(len(current_section)):
                should_escalate = True
                if row_height * len(current_section[0]) > smallest_solution_area:
                    continue
                for row_num in range(len(current_section) - row_height):
                    sub_section = current_section[row_num:row_num + row_height + 1]
                    if section_sum(sub_section) == target_diamond_amount:
                        if len(sub_section) * len(sub_section[0]) < smallest_solution_area:
                            smallest_solution_area = len(sub_section) * len(sub_section[0])

                        if revert:
                            solutions.append(map_transpose(sub_section))
                        else:
                            solutions.append(sub_section)
                        should_escalate = False
                if not should_escalate:
                    break
            viable_sections.pop(0)

    searching_time = time.time()
    search_for_solutions(viable_col_sections)
    search_for_solutions(viable_row_sections, revert=True)
    # print("searching time", time.time() - searching_time)

    # Filter solutions
    if solutions:
        scored_solutions = {}
        for solution in solutions:
            solution_score = len(solution) * len(solution[0])
            if solution_score not in scored_solutions:
                scored_solutions[solution_score] = [solution]
            else:
                scored_solutions[solution_score].append(solution)

        lowest_score = min(scored_solutions.keys())
        unclean_solutions = scored_solutions[lowest_score]
        clean_solutions = []
        comparable_solutions = [",".join(["row".join([str(sss) for sss in ss]) for ss in s]) for s in unclean_solutions]
        for sol in comparable_solutions:
            if sol not in clean_solutions:
                clean_solutions.append(sol)

        def back_to_lists(solution):
            area = []
            for ss in solution.split(","):
                row_in_solution = [int(sss) for sss in ss.split("row")]
                area.append(row_in_solution)
            return area

        clean_solutions = list(map(back_to_lists, clean_solutions))

        def solutions_to_coordinates(solutions):
            coordinates = []
            for solution in solutions:
                tl_bound = [0, 0]
                br_bound = [len(solution), len(solution[0])]

                search_tl_bound = tl_bound.copy()
                search_br_bound = br_bound.copy()
                for i in range(0, len(diamond_map) - len(solution) + 1):
                    for j in range(0, len(diamond_map[0]) - len(solution[0]) + 1):
                        search_tl_bound[1] = tl_bound[1] + j
                        search_br_bound[1] = br_bound[1] + j

                        search_area_rows = diamond_map[search_tl_bound[0]:search_br_bound[0]]
                        search_area = [row[search_tl_bound[1]:search_br_bound[1]] for row in search_area_rows]
                        search_area_string = hash(tuple([tuple(s) for s in search_area]))
                        solution_string = hash(tuple([tuple(s) for s in solution]))
                        if search_area_string == solution_string:
                            coordinates.append(
                                [
                                    (search_tl_bound[0], search_tl_bound[1]),
                                    (search_br_bound[0] - 1, search_br_bound[1] - 1)
                                ]
                            )
                    search_tl_bound[0] += 1
                    search_br_bound[0] += 1
            return coordinates

        solution_coordinates = solutions_to_coordinates(clean_solutions)
        sorted_coordinates = sorted(solution_coordinates, key=lambda s: (s[0][0], s[0][1], s[1][0], s[1][1]))
        print(sorted_coordinates)
        return sorted_coordinates
    else:
        return solutions


# response_class = standards.Problem(
#     description=description,
#     run_function=main_function,
#     input_generator=input_generator,
#     input_prompt=input_prompt,
#     index_info=index_info
# )

if __name__ == "__main__":
    i = input_generator(size=(30, 30))
    whole_time_reference = time.time()
    main_function(i)
    print("Total time:", time.time() - whole_time_reference)

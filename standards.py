import traceback


class Problem:
    description = ""
    run_function = None
    input_generator = None
    input_prompt = None
    index_info = None

    def __init__(self, description=None, run_function=None, input_generator=None, input_prompt=None, index_info=None):
        self.description = description if description else "No description provided for this entry"
        self.run_function = run_function
        self.input_generator = input_generator
        self.input_prompt = input_prompt
        self.index_info = index_info
        print(self.description)

    def run(self):
        if self.input_generator:
            func_input = self.input_generator()
        else:
            func_input = input(self.input_prompt)

        try:
            print(self.run_function(func_input))
            run_again = input("Would you like to run this program again (y/n): ")
            if str(run_again).lower() in "yes":
                self.run()
            else:
                print("Done.")
        except:
            traceback.print_exc()
            print(f"\nInput \"{func_input}\" may be invalid, check above traceback to confirm")
            print("Restarting...")
            self.run()

import ya_academy_contest_problems

EXIT_CHOICE = 1
TOPIC_2_CHOICE = 2
TOPIC_3_CHOICE = 3
TOPIC_4_CHOICE = 4
TOPIC_5_CHOICE = 5
TOPIC_6_CHOICE = 6


def main():
    choice = 0
    while choice != EXIT_CHOICE:
        show_options()
        choice = int(input("Select TOPIC (2-6): "))
        if choice == TOPIC_2_CHOICE:
            problem = (input("Select problem (A-T): ")).lower()
            if problem == "a":
                pass  # eval(ya_academy_contest_problems.python_basics.input_output_formatting.problem_a)
            print("Executing selected problem...")
        #            for execution_choice in problem_selector:
        #                if problem
        elif choice == TOPIC_3_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == TOPIC_4_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == TOPIC_5_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == TOPIC_6_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == EXIT_CHOICE:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")


def show_options():
    print(
        """This is an interactive navigation menu
    2 — TOPIC 2. Python basics.
    3 — TOPIC 3. Collections and memory management.
    4 — TOPIC 4. Functions and their features.
    5 — TOPIC 5. Object-oriented programming.
    6 — TOPIC 6. Libraries for data collecting and processing.
    1 — Exit
    """
    )


main()

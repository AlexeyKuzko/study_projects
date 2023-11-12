from ya_academy_contest_problems import *
from sow_python_problems import *
from code_basics_python import *

EXIT_CHOICE = 1
# yandex
YA_CHOICE = "ya"
TOPIC_2_CHOICE = 2
TOPIC_3_CHOICE = 3
TOPIC_4_CHOICE = 4
TOPIC_5_CHOICE = 5
TOPIC_6_CHOICE = 6
# sow_python
SOWPY_CHOICE = "sowpy"
CHAPTER_2_CHOICE = 2
CHAPTER_3_CHOICE = 3
CHAPTER_4_CHOICE = 4
CHAPTER_5_CHOICE = 5
CHAPTER_6_CHOICE = 6
CHAPTER_7_CHOICE = 7
CHAPTER_8_CHOICE = 8
CHAPTER_9_CHOICE = 9
CHAPTER_10_CHOICE = 10
CHAPTER_11_CHOICE = 11
CHAPTER_12_CHOICE = 12
CHAPTER_13_CHOICE = 13
CHAPTER_14_CHOICE = 14
CHAPTER_15_CHOICE = 15


def start():
    print("Ya or SOWPY?")
    choice = input("Choose a project to show:")
    if choice == YA_CHOICE:
        ya_main()
    elif choice == SOWPY_CHOICE:
        sowpy_main()


def ya_main():
    choice = 0
    while choice != EXIT_CHOICE:
        ya_show_options()
        choice = int(input("Select topic (2-6): "))
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


def ya_show_options():
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


def sowpy_main():
    choice = 0
    while choice != EXIT_CHOICE:
        sowpy_show()
        choice = int(input("Select chapter (2-6): "))
        if choice == CHAPTER_2_CHOICE:
            #            problem_selector = (input("Select problem (A-T): ")).lower()
            print("Executing selected problem...")
        #            for execution_choice in problem_selector:
        #                if problem
        elif choice == CHAPTER_3_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_4_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_5_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_6_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_7_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_8_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_9_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_10_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_11_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_12_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_13_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_14_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == CHAPTER_15_CHOICE:
            print("Not implemented yet")
            pass
        elif choice == EXIT_CHOICE:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")


def sowpy_show():
    print(
        """This is an interactive navigation menu
    1 — Exit
    2 — Chapter 2. Input, Processing, and Output
    3 — Chapter 3. Decision Structures and Boolean Logic
    4 — Chapter 4. Repetition Structures
    5 — Chapter 5. Functions
    6 — Chapter 6. Files and Exceptions
    7 — Chapter 7. Lists and Tuples
    8 — Chapter 8. More About Strings
    9 — Chapter 9. Dictionaries and Sets
    10 — Chapter 10. Classes and Object-Oriented Programming
    11 — Chapter 11. Inheritance
    12 — Chapter 12. Recursion
    13 — Chapter 13. GUI Programming
    14 — Chapter 14. Database Programming
    15 — Chapter 15. Functional Programming
    """
    )


start()

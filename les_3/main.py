from program import Program

programs = (
    { 'name': 'exercise_1', 'desc': 'exercise 3_1 (functie met 3 parameters)', 'file': 'les_3.exercise_1'},
    { 'name': 'exercise_2', 'desc': 'exercise 3_2 (functie met list-parameter)', 'file': 'les_3.exercise_2'},
    { 'name': 'exercise_3', 'desc': 'exercise 3_3 (functie met if)', 'file': 'les_3.exercise_3'},
    { 'name': 'exercise_4', 'desc': 'exercise 3_4 (functie met if)', 'file': 'les_3.exercise_4'},
    { 'name': 'exercise_5', 'desc': 'exercise 3_5 (functie met list-parameter en for-loop)', 'file': 'les_3.exercise_5'},
    { 'name': 'exercise_6', 'desc': 'exercise 3_6 (functie met (im)mutable parameter)', 'file': 'les_3.exercise_6'},
    { 'name': 'final', 'desc': 'Final assignment for lesson 3', 'file': 'les_3.final_assignment'},
)
program = Program('Block 1 - les 3 - Nick Bout - HBO ict - HU', programs)
# Start the program loop
program.start()

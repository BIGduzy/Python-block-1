from program import Program

programs = (
    { 'name': 'exercise_1', 'desc': 'exercise 4_1 (Formatting)', 'file': 'les_4.exercise_1'},
    { 'name': 'exercise_2', 'desc': 'exercise 4_2 (files lezen)', 'file': 'les_4.exercise_2'},
    { 'name': 'exercise_3', 'desc': 'exercise 4_3 (files lezen)', 'file': 'les_4.exercise_3'},
    { 'name': 'exercise_4', 'desc': 'exercise 4_4 (files schrijven)', 'file': 'les_4.exercise_4'},
    { 'name': 'final', 'desc': 'Final assignment for lesson 4', 'file': 'les_4.final_assignment'},
)
program = Program('Block 1 - les 3 - Nick Bout - HBO ict - HU', programs)
# Start the program loop
program.start()

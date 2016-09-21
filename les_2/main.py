from program import Program

programs = (
    { 'name': 'exercise_1', 'desc': 'exercise 2_1 (input & eval)', 'file': 'les_2.exercise_1'},
    { 'name': 'exercise_2', 'desc': 'exercise 2_2 (if-statement)', 'file': 'les_2.exercise_2'},
    { 'name': 'exercise_3', 'desc': 'exercise 2_3 (if met 2 booleaanse operators)', 'file': 'les_2.exercise_3'},
    { 'name': 'exercise_4', 'desc': 'exercise 2_4 (if-else)', 'file': 'les_2.exercise_4'},
    { 'name': 'exercise_5', 'desc': 'exercise 2_5 (for + if)', 'file': 'les_2.exercise_5'},
    { 'name': 'final', 'desc': 'Final assignment for lesson 2', 'file': 'les_2.final_assignment'},
)
program = Program('Block 1 - les 2 - Nick Bout - HBO ict - HU', programs)
# Start the program loop
program.start()

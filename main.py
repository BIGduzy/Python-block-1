from program import Program

programs = (
    { 'name': 'les_1', 'desc': 'All exercises for lesson 1', 'file': 'les_1.les_1' },
    { 'name': 'les_2', 'desc': 'All exercises for lesson 2', 'file': 'les_2.main' },
    { 'name': 'les_3', 'desc': 'All exercises for lesson 3', 'file': 'les_3.main' },
    { 'name': 'les_4', 'desc': 'All exercises for lesson 4', 'file': 'les_4.main' },
)
program = Program('Python programming Block 1 - Nick Bout - 1709217 - HBO ICT - HU', programs)
# Start the program loop
program.start()

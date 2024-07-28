"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        [
    {
        "input": [["O Senhor dos Anéis", "1984", "Dom Casmurro"], "1984"],
        "answer": 1
    },
    {
        "input": [["O Senhor dos Anéis", "1984", "Dom Casmurro"], "Harry Potter"],
        "answer": -1
    },
    {
        "input": [["O Alquimista", "O Pequeno Príncipe", "1984"], "O Pequeno Príncipe"],
        "answer": 1
    },
    {
        "input": [["1984", "Dom Casmurro"], "1984"],
        "answer": 0
    }
]

    ]
}

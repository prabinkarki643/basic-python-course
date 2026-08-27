"""The question bank for the Quiz Game.

Each question is a dictionary with four keys:

    "category"  the subject the question belongs to
    "question"  the question text shown to the player
    "options"   a list of four possible answers
    "answer"    the position of the correct option in that list
                (0 is the first option, 1 the second, and so on)

To add a question, copy any dictionary below, change the four values,
and make sure "answer" points at the correct option. Nothing else in
the program needs to change.
"""

QUESTIONS = [
    {
        "category": "Physics",
        "question": "What is the SI unit of force?",
        "options": ["Joule", "Newton", "Watt", "Pascal"],
        "answer": 1,
    },
    {
        "category": "Physics",
        "question": "What is the approximate acceleration due to gravity on Earth?",
        "options": ["3.7 m/s^2", "6.0 m/s^2", "9.8 m/s^2", "12.5 m/s^2"],
        "answer": 2,
    },
    {
        "category": "Physics",
        "question": "What is the approximate speed of light in a vacuum?",
        "options": [
            "3 x 10^6 m/s",
            "3 x 10^8 m/s",
            "3 x 10^10 m/s",
            "3 x 10^12 m/s",
        ],
        "answer": 1,
    },
    {
        "category": "Chemistry",
        "question": "What is the chemical symbol for sodium?",
        "options": ["So", "Sd", "Na", "S"],
        "answer": 2,
    },
    {
        "category": "Chemistry",
        "question": "What is the atomic number of carbon?",
        "options": ["4", "6", "8", "12"],
        "answer": 1,
    },
    {
        "category": "Chemistry",
        "question": "What is the approximate value of Avogadro's number?",
        "options": [
            "6.022 x 10^21",
            "6.022 x 10^23",
            "3.14 x 10^23",
            "1.602 x 10^19",
        ],
        "answer": 1,
    },
    {
        "category": "Biology",
        "question": "Which organelle is known as the powerhouse of the cell?",
        "options": ["Ribosome", "Nucleus", "Mitochondrion", "Golgi body"],
        "answer": 2,
    },
    {
        "category": "Biology",
        "question": "How many chromosomes are there in a normal human body cell?",
        "options": ["23", "44", "46", "48"],
        "answer": 2,
    },
    {
        "category": "Biology",
        "question": "Which gas do plants absorb from the air during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": 2,
    },
    {
        "category": "Maths",
        "question": "What is the value of pi, correct to two decimal places?",
        "options": ["3.12", "3.14", "3.16", "3.18"],
        "answer": 1,
    },
    {
        "category": "Maths",
        "question": "What is the derivative of x squared with respect to x?",
        "options": ["x", "2x", "x^3 / 3", "2"],
        "answer": 1,
    },
    {
        "category": "Maths",
        "question": "What is the value of sin 90 degrees?",
        "options": ["0", "0.5", "1", "Undefined"],
        "answer": 2,
    },
    {
        "category": "Python",
        "question": "Which symbol starts a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": 1,
    },
    {
        "category": "Python",
        "question": "Which function displays a message on the screen?",
        "options": ["show()", "echo()", "print()", "display()"],
        "answer": 2,
    },
    {
        "category": "Python",
        "question": "What type of value does input() always give you?",
        "options": ["int", "float", "bool", "str"],
        "answer": 3,
    },
]

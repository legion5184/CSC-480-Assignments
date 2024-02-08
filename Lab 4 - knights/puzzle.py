from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # If A is a knight, we know A must be a knight and knave
    Implication(AKnight, And(AKnight, AKnave)),
    # We know A has to be a Knight or Knave
    Or(AKnave, AKnight),
    # We know A can't be both a Knight or Knave
    Not(And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # If A is a knight, we know A and B must be knights
    Implication(AKnight, And(AKnave, BKnave)),
    # A must be a knight or knave
    Or(AKnave, AKnight),
    # B must be a knight or knave
    Or(BKnave, BKnight),
    # A or B cannot be both knight or knave
    Not(And(AKnight, AKnave)),
    Not(And(BKnave, BKnight))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # If A is a knight, A is a knight iff B is a knight
    Implication(AKnight, Biconditional(AKnight, BKnight)),
    # If A is a knave, A is a knight iff B is a knave and vice versa
    Implication(AKnave, Or(Biconditional(AKnight, BKnave), Biconditional(AKnave, BKnight))),
    # A must be a knight or knave
    Or(AKnave, AKnight),
    # B must be a knight or knave
    Or(BKnave, BKnight),
    # A or B cannot be both knight or knave
    Not(And(AKnight, AKnave)),
    Not(And(BKnave, BKnight))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # If C is a knight, A is a knight
    Implication(CKnight, AKnight),
    # If B is a knight/knave, C is a knave/knight
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    # If C is a knave, A is a knave
    Implication(CKnave, Not(AKnight)),
    # If C is a knave, B is a knight
    Implication(CKnave, BKnight),
    # If B is a knight, A must have said it's a knave
    # If A is a knave, it must lie, so not a knight
    # If A is a knight, it must tell truth, so A is a knight
    Implication(BKnight, Or(And(AKnight, AKnight), And(AKnave, Not(AKnave)))),
    # If B is a knave, A must have said it's a knight
    # If A is a knight, it must be a knight
    # If A is a knave, is must not be a knight
    Implication(BKnave, Or(And(AKnight, AKnight), And(AKnave, Not(AKnight)))),
    # A,B,C must be a knight or knave
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(CKnight, CKnave),
    # A or B cannot be both knight or knave
    Not(And(AKnight, AKnave)),
    Not(And(BKnave, BKnight)),
    Not(And(CKnight, CKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

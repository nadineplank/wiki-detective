

def reveal_next_clue(case, clues_revealed):
    """
    Reveal the next clue for the selected mystery case.

    Args:
        case: The mystery case containing the clues.
        clues_revealed: The number of clues already revealed.

    Returns:
        The updated number of clues revealed, or the unchanged
        count if all clues have already been revealed.
    """
    if clues_revealed >= len(case.clues):
        print("All clues have been revealed.")
        return clues_revealed

    print()
    print(case.clues[clues_revealed])
    print()
    return clues_revealed + 1


def check_guess(guess, case):
    """
    Check whether the player's guess matches the case answer.

    Args:
        guess: The answer provided by the player.
        case: The mystery case containing the correct answer.

    Returns:
        True if the guess matches the answer, ignoring capitalization
        and leading or trailing whitespace; otherwise, False.
    """

    return guess.strip().casefold() == case.answer.strip().casefold()


def calculate_score(case, clues_revealed):
    """
    Calculate the score for solving a mystery case.

    Deduct points based on the number of clues revealed. The fewer
    clues revealed, the higher the score.

    Args:
        case: The mystery case containing the maximum points and clues.
        clues_revealed: The number of clues revealed during the investigation.

    Returns:
        The calculated score as a rounded integer.
    """
    deduction = case.points / (len(case.clues) + 1)
    score = case.points - (deduction * clues_revealed)

    return round(score)

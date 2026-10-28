

def reveal_next_clue(case, clues_revealed):
    """Reveal the next clue for the selected mystery case.

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

    print(case.clues[clues_revealed])
    return clues_revealed + 1


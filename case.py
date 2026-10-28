from enum import Enum

class Difficulty(Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

class Case:
    """Represent a predefined mystery case in the game."""
    def __init__(
            self,
            title: str,
            description: str,
            answer: str,
            clues: list[str],
            points: int,
            difficulty: Difficulty
    ) -> None:
        self.title = title
        self.description = description
        self.answer = answer
        self.clues = clues
        self.points = points
        self.difficulty = difficulty


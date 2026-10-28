from case import Case, Difficulty

case_001 = Case(
    "The Revolutionary Physicist",
    "Investigate a mystery from the world of physics and scientific discovery.",
    "Albert Einstein",
    [
        "This person made major contributions to science.",
        "Their work transformed our understanding of space and time.",
        "They developed the theory of relativity."
    ],
    100,
    Difficulty.EASY)

case_002 = Case(
    "The Gothic Creator",
    "Investigate a mystery from the world of literature and classic fiction.",
    "Mary Shelley",
    [
        "This person was a British writer.",
        "One of their best-known works explores the consequences of creating life.",
        "They wrote Frankenstein; or, The Modern Prometheus."
    ],
    100,
    Difficulty.MEDIUM
)

case_003 = Case(
    "The Analytical Pioneer",
    "Explore the early history of computing and the people who shaped it.",
    "Ada Lovelace",
    [
        "This person lived during the nineteenth century.",
        "They worked on ideas involving a mechanical computing machine.",
        "Their notes included an algorithm intended for Charles Babbage's Analytical Engine."
    ],
    100,
    Difficulty.HARD
)

cases = [case_001, case_002, case_003]

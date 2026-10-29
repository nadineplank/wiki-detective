import os
import json

from dotenv import load_dotenv
from openrouter import OpenRouter
from case import Case


load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OpenRouter API key not found.")


def generate_mystery(topic, difficulty):
    """
    Generates a mystery case based on a user-provided topic.

     Args:
        topic: The topic chosen by the user.
        difficulty: The difficulty chosen by the user.

    Returns:
        A Case object containing the generated title, description,
        answer, clues, points, and difficulty.
    """

    prompt = f"""
    You are generating mystery cases for Wikipedia Detective, a
    Python console game about identifying real people through
    Wikipedia research and factual clues.

    The player chooses a topic, receives a short case briefing,
    investigates Wikipedia articles, reveals clues, and guesses
    the mystery person's identity.

    Generate one mystery case based on this topic: {topic}
    The player has selected {difficulty.name} difficulty.

    Choose a notable real person who is relevant to the topic.

    Return only valid JSON using this exact structure:
    {{
        "title": "...",
        "description": "...",
        "answer": "...",
        "clues": ["...", "...", "..."]
    }}

    Follow these requirements:

    TITLE
    - Use a short, intriguing title of 3–7 words.
    - The title should hint at the person's field or achievements.
    - Do not reveal the person's name.

    DESCRIPTION
    - Write 1–2 sentences, with a maximum of 40 words.
    - Give the player a meaningful starting direction for research.
    - Identify the person's field and narrow it using relevant
      context, such as historical period, location, movement,
      specialty, or type of contribution.
    - Include a distinctive but non-identifying aspect of the
      person's work or historical significance.
    - Avoid generic descriptions that could apply to hundreds
      of people in the same field.
    - Do not reveal the person's name or simply list the clues.
    - Do not invent fictional events or storylines.

    ANSWER
    - Return only the person's full, commonly recognized name.
    - Do not include a sentence, explanation, or additional text.

    CLUES
    - Generate 3–5 concise, factual clues about the person.
    - Order the clues from least revealing to most revealing.
    - Each clue should provide a useful fact about the person's
      life, work, achievements, or historical significance.
    - Do not mention the person's name in any clue.
    - Avoid repeating the same information across clues.
    - Use specific facts that can be checked against Wikipedia.
    - Do not invent facts or claim certainty when unsure.

    DIFFICULTY
    - Use the difficulty selected by the player. Do not choose a
      different difficulty.

    - EASY:
      Give a relatively specific research direction in the
      description. Use familiar achievements and recognizable
      clues that make the person easier to identify.

    - MEDIUM:
      Give a useful but broader research direction. Require the
      player to connect several facts from the clues to identify
      the person.

    - HARD:
      Give a less obvious research direction without making the
      description vague or unhelpful. Use less widely known but
      verifiable facts as clues, requiring deeper investigation.

    - For every difficulty, the description must help the player
      decide what to search for on Wikipedia without revealing
      the person's identity.

    - The clues must become progressively more revealing,
      regardless of difficulty.

    GENERAL RULES
    - The game is about identifying real people, not solving
      fictional crimes or investigating invented events.
    - Keep the content suitable for a general audience.
    - Do not include points; the application assigns them.
    - Return valid JSON only, with no Markdown fences,
      introduction, explanation, or text outside the JSON.
    - Ensure all required fields are present and correctly typed.
    """


    with OpenRouter(api_key=api_key) as client:
        response = client.chat.send(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            stream=False,
        )

    response_text = response.choices[0].message.content

    try:
        mystery_data = json.loads(response_text)
    except json.JSONDecodeError as error:
        raise ValueError("The AI returned invalid JSON.") from error

    if not isinstance(mystery_data, dict):
        raise ValueError("The AI response must be a JSON object.")

    required_fields = ["title", "description", "answer", "clues"]


    if not all(field in mystery_data for field in required_fields):
        raise ValueError("Missing fields in the AI response.")

    if not all(
        isinstance(mystery_data[field], str)
        for field in required_fields[:3]
    ):
        raise ValueError("Fields must be strings.")

    clues = mystery_data["clues"]

    if not isinstance(clues, list):
        raise ValueError("The clues must be a list.")

    if not 3 <= len(clues) <= 5:
        raise ValueError("There must be between 3 and 5 clues.")

    if not all(isinstance(clue, str) for clue in clues):
        raise ValueError("Every clue must be a string.")

    generated_mystery = Case(
        mystery_data["title"],
        mystery_data["description"],
        mystery_data["answer"],
        mystery_data["clues"],
        100,
        difficulty
    )

    return generated_mystery



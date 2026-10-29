# 🕵️ Wikipedia Detective

Wikipedia Detective is a Python-based terminal game where players solve mysteries about real people by uncovering clues and investigating Wikipedia articles. Players can choose predefined cases or generate new mysteries using AI.

## ✨ Features

- **Predefined mysteries:** Investigate cases featuring notable historical figures.
- **AI-generated mysteries:** Generate new mysteries using an LLM via OpenRouter.
- **Three difficulty levels:** Easy, Medium, and Hard.
- **Clue-based gameplay:** Reveal clues and use them to identify the mystery's answer.
- **Wikipedia investigation:** Search for articles and read their summaries.
- **Section exploration:** Browse individual sections of Wikipedia articles for more information.
- **Readable terminal output:** Use Rich to format long text and improve readability.

## 🛠️ Tech Stack

- **Python 3.14.7**
- [Wikipedia-API](https://pypi.org/project/Wikipedia-API/)
- [OpenRouter](https://openrouter.ai/)
- [Rich](https://rich.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## 🚀 Getting Started

### Prerequisites

- Python 3.14.7
- An OpenRouter API key for AI-generated mysteries

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nadineplank/wiki-detective.git
   cd wiki-detective
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment.

   **macOS / Linux:**

   ```bash
   source .venv/bin/activate
   ```

   **Windows (PowerShell):**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add your OpenRouter API key:

   ```text
   OPENROUTER_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your actual API key. Keep the `.env` file private and never commit your API key to GitHub.

### Run the Game

Start the game from the project root:

```bash
python main.py
```

Follow the terminal prompts to start a game and investigate a mystery.

## 🎮 How to Play

1. Start the game and select a mystery.
2. Choose a difficulty level where prompted.
3. Read the mystery description and available clues.
4. Investigate relevant Wikipedia articles.
5. Explore article sections to uncover additional information.
6. Reveal clues and submit your guess.
7. Use the information you've gathered to solve the mystery.

## 🤖 AI Mystery Generation

Wikipedia Detective uses an LLM accessed through OpenRouter to generate mysteries.

The generator requests structured JSON containing the mystery's title, description, answer, and clues. The response is validated before being converted into a `Case` object for gameplay.

The goal is to create mysteries about real people using factual information rather than invented narratives.

## 📁 Project Structure

- `main.py` — Main menu and gameplay flow
- `case.py` — `Case` class and `Difficulty` enum
- `cases.py` — Predefined mystery cases
- `investigation.py` — Wikipedia article retrieval and section exploration
- `ai/mystery_generator.py` — AI-powered mystery generation

## 🔮 Future Improvements

- Expand the collection of predefined mysteries.
- Improve clue and scoring mechanics.
- Add more investigation options.
- Expand automated testing and error handling.

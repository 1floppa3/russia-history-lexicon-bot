import json
import difflib
import random
from pathlib import Path

class LexiconService:
    def __init__(self, json_path: Path):
        with open(json_path, 'r', encoding='utf-8') as f:
            self.words: list[dict] = json.load(f)
        self.sources: list[str] = sorted({w['source'] for w in self.words})

    def find(self, word: str) -> list[dict]:
        return [w for w in self.words if w['word'].lower() == word.lower()]

    def nearest(self, word: str, max_results: int = 1) -> list[dict]:
        all_words = [w['word'] for w in self.words]
        matches = difflib.get_close_matches(word, all_words, max_results)
        return [w for w in self.words if w['word'] in matches]

    def random_word(self) -> dict:
        return random.choice(self.words)

    def list_books(self) -> list[str]:
        return self.sources

    def generate_quiz(self) -> tuple[dict, list[str]]:
        correct = self.random_word()
        defs = [w['definition'] for w in self.words if w['definition'] != correct['definition']]
        options = random.sample(defs, 3) + [correct['definition']]
        random.shuffle(options)
        return correct, options
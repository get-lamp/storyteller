from dataclasses import dataclass
import random

male_first_names = [
    'Finn',
    'Arthur',
    'Bort'
]

last_names = [
    'Jaenke',
    'Kooch',
    'Hood'
]

adjectives = [
    'incompetent',
    'marvellous',
    'beautiful',
    'eccentric',
    'ambitious',
    'reluctant'
]

concrete_nouns = [
    'computer',
    'violin',
    'physics'
]

occupation_nouns = [
    'hacker',
    'erudite',
    'genius',
    'professor',
    'enthusiast',
    'amateur'
]


def generate_apposite_noun():
    return Noun(
        text=f'{random.choice(concrete_nouns)} '
             f'{random.choice(occupation_nouns)}'
    )


def generate_character():
    return Character(
        first_name=random.choice(male_first_names),
        last_name=random.choice(last_names),
        pronoun='he'
    )


def generate_noun_phrase():
    return Phrase(text=f'{random.choice(adjectives)} {generate_apposite_noun().text}')


@dataclass
class Character:
    first_name: str
    last_name: str
    pronoun: str

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


@dataclass
class Noun:
    text: str

@dataclass
class Phrase:
    text: str

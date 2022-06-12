from jinja2 import Environment, PackageLoader, select_autoescape

from storyteller.entity import generate_character, generate_noun_phrase
import random


env = Environment(
    loader=PackageLoader("storyteller"),
    autoescape=select_autoescape()
)

template = env.get_template("state_subject.tmpl")


data = [{
    'subject': generate_character().full_name,
    'noun': generate_noun_phrase().text,
    'verb': random.choice(['is', 'was'])
} for _ in range(10)]

for d in data:
    print(template.render(**d))


"""
demonyms = [
    ('Africa', 'African', 'Afro'),
    ('America', 'American', 'Americo'),
    ('France', 'French', 'Franco'),
    ('Canada', 'Canadian', 'Canado'),
    ('Africa', 'African', 'Afro'),
    ('South America', 'South American', 'Latin'),
    ('Jew', 'Jewish', 'Judeo'),
    ('Ireland', 'Irish', 'Hiberno'),
    ('England', 'English', 'Anglo')
]
"""

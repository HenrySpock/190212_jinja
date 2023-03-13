"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, title, id):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title
        self.id = id

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story1 = Story( 
    ["place", "noun", "verb", "adjective", "plural_noun", 'exclamation'],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}. {exclamation}!""", 'Story 1',
       id=1
)

story2 = Story( 
    ['adjective', 'creature', 'location', 'person', 'item'], 
    """Once upon a time, there was a {adjective} {creature} who lived in a {location}. 
    One day, {creature} met a {adjective} {person} who asked for {creature}'s {item}.""", 'Story 2',
    id=2
)

story3 = Story( 
    ['year', 'achievement', 'professionals', 'location', 'adjective', 'creature', 'noun'],
    """In the year {year}, humanity has achieved {achievement}, but with that comes new 
    dangers. A team of {professionals} are sent on a mission to {location} to stop a 
    {adjective} {creature} from destroying {noun} once and for all.""", 'Story 3',
    id=3
)

story4 = Story( 
    ['name', 'location', 'adjective', 'noun', 'verb', 'action'],
    """It was a dark and stormy night, and {name} was all alone in their {location}. 
    Suddenly, they heard a {adjective} {noun} scratching at the door. {name} {verb} to 
    {action}, hoping to escape the {adjective} {noun}.""", 'Story 4',
    id=4
)

story5 = Story( 
    ['person', 'adjective', 'food', 'number', 'ingredients', 'verb', 'utensil', 'condiment', 'flavor'],
    """{person} was in the mood for something {adjective} to eat, so they decided to 
    make {food}. They gathered {number} of {ingredients} and started {verb} them together 
    in a {utensil}. Finally, they added some {condiment} for extra {flavor}.""", 'Story 5',
    id=5
)

story6 = Story( 
    ['adjective', 'person', 'ride', 'game', 'number', 'food', 'prize', 'booth', 'animal'],
    """It's time for the annual {adjective} fair! {person} can't wait to ride the 
    {ride} and play some {game}. They're planning to eat {number} {food} and win a {prize} 
    at the {booth}. The only thing that worries them is the {adjective} {animal} exhibit.""", 'Story 6',
    id=6
)
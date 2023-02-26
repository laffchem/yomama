from ninja import Schema

class JokeIn(Schema):
    joke: str
    category: str


class JokeOut(Schema):
    joke: str
    category: str


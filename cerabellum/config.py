import yaml
import os

def load_config(path):
    if not os.path.isabs(path):
        base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base, path)
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config


class State:
    def __init__(self, name, data):
        self._name = name
        self._data = data

    @property
    def name(self):
        return self._name

    @property
    def base(self):
        return self._data['base']

    @property
    def expression(self):
        return self._data['expression']

    @property
    def eyes(self):
        return self._data['eyes']

    @property
    def note(self):
        return self._data.get('note')

    @property
    def warning(self):
        return self._data.get('warning')


class Character:
    def __init__(self, char_id, data):
        self._char_id = char_id
        self._data = data

    @property
    def char_id(self):
        return self._char_id

    @property
    def display_name(self):
        return self._data['display_name']

    @property
    def shorthand(self):
        return self._data['shorthand']

    @property
    def colour(self):
        return self._data['colour']

    @property
    def flower(self):
        return self._data['flower']

    @property
    def default_base(self):
        return self._data.get('defaults', {}).get('base')

    @property
    def default_eyes(self):
        return self._data.get('defaults', {}).get('eyes')

    @property
    def default_expression(self):
        return self._data.get('defaults', {}).get('expression')

    @property
    def side_image(self):
        # returns True if this character uses the side image system
        # side image characters do not need explicit \\ hide: calls
        return self._data.get('side_image', False)

    @property
    def states(self):
        raw = self._data.get('states', {})
        return {name: State(name, data) for name, data in raw.items()}

    def get_state(self, state_name):
        return self.states.get(state_name)

    def get_sprite_paths(self, state_name):
        state = self.get_state(state_name)
        if state is None:
            return None
        return {
            'base':       self._data['bases'].get(state.base),
            'expression': self._data['expressions'].get(state.expression),
            'eyes':       self._data['eyes'].get(state.eyes)
        }


class Config:
    def __init__(self, path):
        self._data = load_config(path)

    @property
    def characters(self):
        if not hasattr(self, '_characters'):
            self._characters = {
                char_id: Character(char_id, data)
                for char_id, data in self._data.get('characters', {}).items()
            }
        return self._characters

    def get_character(self, char_id):
        return self.characters.get(char_id)

    def is_side_image(self, char_id):
        # convenience method — check if a character uses side images
        char = self.get_character(char_id)
        if char is None:
            return False
        return char.side_image

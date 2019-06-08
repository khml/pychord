# coding:utf-8

from enum import Enum

SHARP = "Sharp"
SHARP_MARK = "#"


class Note(Enum):
    A = 0
    ASharp = 1
    B = 2
    C = 3
    CSharp = 4
    D = 5
    DSharp = 6
    E = 7
    F = 8
    FSharp = 9
    G = 10
    GSharp = 11
    ScaleSize = 12

    def __add__(self, other: int):
        return Note((self.value + other) % self.ScaleSize.value)

    def __sub__(self, other: int):
        return Note((self.value - other) % self.ScaleSize.value)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name

    @property
    def name(self) -> str:
        return super().name.replace(SHARP, SHARP_MARK)


def unroll_notes(base: Note, delta_list: list) -> list:
    """
    :param base:
    :param delta_list: list of int
    :return: list of note
    """
    return [base + c for c in delta_list]


class Scale(Enum):
    major = 0
    minor = 1

    def __hash__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value


class Key:
    def __init__(self, base: Note, scale: Scale):
        self._base = base
        self._scale = scale
        self._notes = unroll_notes(self._base, ScalingDict[scale])

    @property
    def base(self) -> Note:
        return self._base

    @property
    def scale(self) -> Scale:
        return self._scale

    @property
    def notes(self) -> list:
        """
        :return: list of Key
        """
        return self._notes

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    @property
    def name(self):
        return "{}{}".format(self._base.name, self._scale.name)


Notes = [Note(i) for i in range(Note.ScaleSize.value)]

ScalingDict = \
    {
        Scale.major: [0, 2, 4, 5, 7, 9, 11],
        Scale.minor: [0, 2, 3, 5, 7, 8, 10]
    }

KeyList = []
KeyList += [Key(key, Scale.major) for key in Notes]
KeyList += [Key(note, Scale.minor) for note in Notes]


def parse_note_name(key_name: str):
    for i in range(Note.ScaleSize.value):
        key = Note(i)
        if key_name == key.name:
            return key
    return False

# coding:utf-8

from enum import Enum

from Key import Note, Key, KeyList, unroll_notes, SHARP_MARK, parse_note_name


class ChordType(Enum):
    major = 0  # M
    minor = 1  # m
    seventh = 2  # 7
    minor7 = 3  # m7
    major7 = 4  # M7
    minor_major7 = 5  # mM7
    sus4 = 6  # sus4
    seventh_sus4 = 7  # 7sus4
    dim = 8  # dim
    m7_5 = 9  # m7-5
    aug = 10  # aug
    add9 = 11  # add9
    six = 12  # 6
    minor6 = 13  # m6
    end = 14

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    @property
    def name(self) -> str:
        chord_type = super().name.replace("minor", "m").replace("major", "M").replace("seventh", "7") \
            .replace("six", "6").replace("_", "-")
        return chord_type


ChordTypeDict = \
    {
        ChordType.major: [0, 4, 7],
        ChordType.minor: [0, 3, 7],
        ChordType.seventh: [0, 4, 7, 10],
        ChordType.minor7: [0, 3, 7, 10],
        ChordType.major7: [0, 4, 7, 11],
        ChordType.minor_major7: [0, 3, 7, 11],
        ChordType.sus4: [0, 5, 7],
        ChordType.seventh_sus4: [0, 5, 7, 10],
        ChordType.dim: [0, 3, 6, 9],
        ChordType.m7_5: [0, 3, 6, 10],
        ChordType.aug: [0, 4, 8],
        ChordType.add9: [0, 2, 7],
        ChordType.six: [0, 4, 7, 9],
        ChordType.minor6: [0, 3, 7, 9],
    }

ChordTypeList = [ChordType(i) for i in range(ChordType.end.value)]


class Chord:
    def __init__(self, base: Note, chord_type: ChordType):
        self._base = base
        self._type = chord_type
        self._notes = unroll_notes(self._base, ChordTypeDict[self._type])

    @property
    def base(self) -> Note:
        return self._base

    @property
    def type(self) -> ChordType:
        return self._type

    @property
    def notes(self) -> list:
        """
        :return: list of Key
        """
        return self._notes

    def __repr__(self):
        return "{}{}".format(self._base.name, self._type.name)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    @property
    def name(self) -> str:
        return self.__repr__()


class _UnrollAllChordsCache:
    def __init__(self):
        self._chords_in_key_dict = {}

    @property
    def is_not_empty(self) -> bool:
        return not len(self._chords_in_key_dict) == 0

    @property
    def chords_in_key_dict(self) -> dict:
        return self._chords_in_key_dict

    @chords_in_key_dict.setter
    def chords_in_key_dict(self, chords_in_scale_dict: dict):
        self._chords_in_key_dict = chords_in_scale_dict


_unroll_all_chords_cache = _UnrollAllChordsCache()


def unroll_all_chords() -> dict:
    """
    {Key: [Chord, Chord, ...]}
    :return:
    """
    if _unroll_all_chords_cache.is_not_empty:
        return _unroll_all_chords_cache.chords_in_key_dict

    chords_in_key_dict = {}
    for scale in KeyList:
        chord_list = []
        for key in scale.notes:
            chord_list += [Chord(key, chord_type) for chord_type in ChordTypeList]
        chords_in_key_dict[scale] = chord_list

    _unroll_all_chords_cache.chords_in_key_dict = chords_in_key_dict
    return chords_in_key_dict


def parse_type(type_name: str):
    for i in range(ChordType.end.value):
        chord_type = ChordType(i)
        if type_name == chord_type.name:
            return chord_type
    return False


def parse_str_chord(chord_name: str):
    chord_name = chord_name.strip()

    if chord_name[1] == SHARP_MARK:
        key = chord_name[:2]
        chord_type = chord_name[2:]
    else:
        key = chord_name[0]
        chord_type = chord_name[1:]

    key = parse_note_name(key)
    if key is False:
        return False

    chord_type = parse_type(chord_type)
    if chord_type is False:
        return False

    return Chord(key, chord_type)


def chord_in_key(chord: Chord, key: Key) -> bool:
    for note in chord.notes:
        if note not in key.notes:
            return False
    return True

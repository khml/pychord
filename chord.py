# coding:utf-8

from enum import Enum

from scale import Key, unroll, Scales, Scale, SHARP_MARK, parse_key


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

    @property
    def name(self):
        chord_name = super().name.replace("minor", "m").replace("major", "M").replace("seventh", "7") \
            .replace("six", "6").replace("_", "-")
        return chord_name


chord_type_dict = \
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


class _ChordsInScaleDict:
    def __init__(self):
        self._chords_in_scale_dict = {}

    @property
    def is_not_empty(self):
        return not len(self._chords_in_scale_dict) == 0

    @property
    def chords_in_scale_dict(self):
        return self._chords_in_scale_dict

    @chords_in_scale_dict.setter
    def chords_in_scale_dict(self, chords_in_scale_dict):
        self._chords_in_scale_dict = chords_in_scale_dict


_chords_in_scale_dict = _ChordsInScaleDict()


class Chord:
    def __init__(self, base: Key, chord_type: ChordType):
        self.base = base
        self.chord_type = chord_type
        self.keys = unroll(self.base, chord_type_dict[self.chord_type])

    def __repr__(self):
        return "{}{}".format(self.base.name, self.chord_type.name)

    def __eq__(self, other):
        return self.name == other.name

    @property
    def name(self):
        return self.__repr__()


def unroll_all_chords() -> dict:
    """
    {scale: [chord1, chord2, ...]}
    :return:
    """
    if _chords_in_scale_dict.is_not_empty:
        return _chords_in_scale_dict.chords_in_scale_dict

    keys = [Key(i) for i in range(Key.ScaleSize.value)]
    chord_types = [ChordType(i) for i in range(ChordType.end.value)]

    major_scales = [Scale(key, Scales.major) for key in keys]
    minor_scales = [Scale(key, Scales.minor) for key in keys]

    scales = []
    scales += major_scales
    scales += minor_scales

    chords_in_scale_dict = {}
    for scale in scales:
        chord_list = []
        for key in scale.keys:
            chord_list += [Chord(key, chord) for chord in chord_types]
        chords_in_scale_dict[scale] = chord_list

    _chords_in_scale_dict.chords_in_scale_dict = chords_in_scale_dict

    return chords_in_scale_dict


def parse_type(type_name: str):
    for i in range(ChordType.end.value):
        chord_type = ChordType(i)
        if type_name == chord_type.name:
            return chord_type
    return False


def parse_str_chord(chord_name: str):
    chord_name = chord_name.strip()

    key = ""
    if chord_name[1] == SHARP_MARK:
        key = chord_name[:2]
        chord_type = chord_name[2:]
    else:
        key = chord_name[0]
        chord_type = chord_name[1:]

    key = parse_key(key)
    if key is False:
        return False

    chord_type = parse_type(chord_type)
    if chord_type is False:
        return False

    return Chord(key, chord_type)

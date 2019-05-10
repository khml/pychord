# coding:utf-8

from enum import Enum

from scale import Key, unroll, Scales, Scale


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


class Chord:
    def __init__(self, base: Key, chord_type: ChordType):
        self.base = base
        self.chord_type = chord_type
        self.keys = unroll(self.base, chord_type_dict[self.chord_type])

    def __repr__(self):
        chord_name = self.chord_type.name.replace("minor", "m").replace("major", "M")\
            .replace("seventh", "7").replace("six", "6").replace("_", "-")
        return "{}{}".format(self.base.name, chord_name)


def unroll_all_chords():
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

    return chords_in_scale_dict

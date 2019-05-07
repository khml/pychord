# coding:utf-8

from enum import Enum

from scale import Key, unroll


class Chords(Enum):
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


chords_dict = \
    {
        Chords.major: [0, 4, 7],
        Chords.minor: [0, 3, 7],
        Chords.seventh: [0, 4, 7, 10],
        Chords.minor7: [0, 3, 7, 10],
        Chords.major7: [0, 4, 7, 11],
        Chords.minor_major7: [0, 3, 7, 11],
        Chords.sus4: [0, 5, 7],
        Chords.seventh_sus4: [0, 5, 7, 10],
        Chords.dim: [0, 3, 6, 9],
        Chords.m7_5: [0, 3, 6, 10],
        Chords.aug: [0, 4, 8],
        Chords.add9: [0, 2, 7],
        Chords.six: [0, 4, 7, 9],
        Chords.minor6: [0, 3, 7, 9],
    }


class Chord:
    def __init__(self, base: Key, chord_name: Chords):
        self.base = base
        self.chord_name = chord_name
        self.keys = unroll(self.base, chords_dict[self.chord_name])

    def __repr__(self):
        chord_name = self.chord_name.name.replace("minor", "m").replace("major", "M")\
            .replace("seventh", "7").replace("six", "6").replace("_", "-")
        return "{}{}".format(self.base.name, chord_name)

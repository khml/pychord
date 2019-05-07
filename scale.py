# coding:utf-8

from enum import Enum


class Key(Enum):
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
        return Key((self.value + other) % self.ScaleSize.value)

    def __sub__(self, other: int):
        return Key((self.value - other) % self.ScaleSize.value)

    @property
    def name(self):
        return super().name.replace("Sharp", "#")


class Scales(Enum):
    major = 0
    minor = 1


def unroll(base: Key, delta_list: list):
    return [base + c for c in delta_list]


scale_dict = \
    {
        Scales.major: [0, 2, 4, 5, 7, 9, 11],
        Scales.minor: [0, 2, 3, 5, 7, 8, 10]
    }


class Scale:
    def __init__(self, base: Key, scale: Scales):
        self.base = base
        self.scale = scale
        self.keys = unroll(self.base, scale_dict[scale])

    def __repr__(self):
        return "{}{}".format(self.base.name, self.scale.name)

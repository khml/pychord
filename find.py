# -*- cosing:utf-8 -*-

import argparse

from Chord import Chord, ChordType, parse_str_chord
from Diatonic import Diatonic, DiatonicChords


def parse_args():
    parser = argparse.ArgumentParser(description="find key by chord")
    parser.add_argument("chordNames", type=str, nargs="*")
    parser.add_argument("--types", action="store_true")
    args = parser.parse_args()
    return args


def get_common_set(old: set, new: set) -> set:
    if len(old) == 0:
        return new

    return old & new


def print_chord_types():
    for i in range(ChordType.end.value):
        print(ChordType(i).name)


def find_keys(chord: Chord) -> list:
    """
    :param chord:
    :return: list of Scale
    """
    keys = []
    diatonic: Diatonic
    for diatonic in DiatonicChords:
        if chord in diatonic.chords:
            keys.append(diatonic.key)
    return keys


def find_common_scales(chord_list: list):
    common_scales = set()
    for chord_name in chord_list:
        chord = parse_str_chord(chord_name)
        keys = set(find_keys(chord))
        print(chord)
        print(keys)
        for key in keys:
            diatonic = Diatonic(key)
            print(diatonic)
            print(diatonic.key.notes)
        print()
        common_scales = get_common_set(common_scales, keys)

    print("Common Scales")
    print(common_scales)


def main():
    args = parse_args()

    if args.types:
        print_chord_types()
        return

    find_common_scales(args.chordNames)


if __name__ == '__main__':
    main()

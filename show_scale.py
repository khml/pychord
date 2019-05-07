# coding:utf-8

from scale import Scale, Scales, Key
from chord import Chord, Chords


def main():
    keys = [Key(i) for i in range(Key.ScaleSize.value)]
    chords = [Chords(i) for i in range(Chords.end.value)]

    major_scales = [Scale(key, Scales.major) for key in keys]
    minor_scales = [Scale(key, Scales.minor) for key in keys]

    scales = []
    scales += major_scales
    scales += minor_scales

    for scale in scales:
        print(scale)
        for key in scale.keys:
            for chord in chords:
                print(Chord(key, chord), end=" ")
            print()
        print()


if __name__ == '__main__':
    main()

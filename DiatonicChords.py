# -*- coding:utf-8 -*-

from Key import Key, Scale, Notes
from Chord import ChordType, Chord

MajorKeyDiatonicChord = [
    ChordType.major,  # I
    ChordType.minor,  # IIm
    ChordType.minor,  # IIIm
    ChordType.major,  # IV
    ChordType.major,  # V
    ChordType.minor,  # VIm
    ChordType.minor,  # VIIm
]

MinorKeyDiatonicChord = [
    ChordType.minor,  # Im
    ChordType.minor,  # IIm
    ChordType.major,  # III
    ChordType.minor,  # IVm
    ChordType.minor,  # Vm
    ChordType.major,  # VI
    ChordType.major,  # VII
]

DiatonicChordsDict = {
    Scale.major: MajorKeyDiatonicChord,
    Scale.minor: MinorKeyDiatonicChord,
}


class DiatonicChords:
    def __init__(self, key: Key):
        self._key = key
        self._chords = []
        self._set_chords()

    def __repr__(self):
        return "Key = {}, Chords = {}".format(self.key, self.chords)

    @property
    def key(self):
        return self._key

    @property
    def chords(self):
        return self._chords

    def _set_chords(self):
        diatonic_chords = DiatonicChordsDict[self.key.scale]
        self._chords = [Chord(note, chord_type) for note, chord_type in zip(self.key.notes, diatonic_chords)]


def main():
    for scale in [Scale.major, Scale.minor]:
        for note in Notes:
            key = Key(note, scale)
            diatonic = DiatonicChords(key)
            print(diatonic)
            print()


if __name__ == '__main__':
    main()

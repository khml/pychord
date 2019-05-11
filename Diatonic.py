# -*- coding:utf-8 -*-

from Key import Key, Notes, Scale
from Chord import unroll_all_chords, Chord, chord_in_key


class Diatonic:
    def __init__(self, key: Key):
        self._key = key
        self._chords = []
        self._prepare_chords()

    def _prepare_chords(self):
        candidates: list = unroll_all_chords()[self.key]
        chord: Chord
        for chord in candidates:
            if chord_in_key(chord, self.key):
                self._chords.append(chord)

    @property
    def key(self):
        return self._key

    @property
    def chords(self):
        return self._chords

    def __repr__(self):
        return "{} : {}".format(self.key, self.chords)


DiatonicChords = []
DiatonicChords += [Diatonic(Key(note, Scale.major)) for note in Notes]
DiatonicChords += [Diatonic(Key(note, Scale.minor)) for note in Notes]

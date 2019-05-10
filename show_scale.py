# coding:utf-8

from chord import unroll_all_chords


def main():
    all_chords = unroll_all_chords()
    for key, chords in all_chords.items():
        print(key)
        print(chords)
        print()


if __name__ == '__main__':
    main()

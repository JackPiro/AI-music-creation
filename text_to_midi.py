import mido
from mido import Message, MidiFile, MidiTrack
import sys

NOTE_NAME_TO_NUMBER = {
    "C": 0,
    "C#": 1,
    "D": 2,
    "D#": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "G": 7,
    "G#": 8,
    "A": 9,
    "A#": 10,
    "B": 11
}

def note_name_to_number(name):
    octave = int(name[-1])
    pitch_class = NOTE_NAME_TO_NUMBER[name[:-1]]
    return pitch_class + octave * 12

def text_to_midi(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    for line in lines:
        parts = line.strip().split(', ')
        if len(parts) != 5:
            continue

        command, channel, note, velocity, time = parts
        note_number = note_name_to_number(note)

        if command == "note_on":
            track.append(Message('note_on', channel=int(channel), note=note_number, velocity=int(velocity), time=int(time)))
        elif command == "note_off":
            track.append(Message('note_off', channel=int(channel), note=note_number, velocity=int(velocity), time=int(time)))

    midi.save(output_file)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    text_to_midi(input_file, output_file)

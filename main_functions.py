from random import choice, randint
from itertools import repeat
from Note import Note


# returns 0 if down or 1 if up
def evaluate_pitch_direction(prob_up, prob_down):
    prob_table = []
    prob_table.extend(repeat(0, prob_down))
    prob_table.extend(repeat(1, prob_up))
    direction = choice(prob_table)
    return direction


# ustawianie interval_degree na pierwszą nutę
def first_note_interval_degree(first_note, notes_name):
    interval_degree = 0

    for counter, notes in enumerate(notes_name):
        if first_note in notes:
            interval_degree = counter

    return interval_degree


# ustawianie semitone_degree na pierwszą nutę
def first_note_semitone_degree(first_note, enharmonic_notes):
    semitone_degree = 0

    for counter, notes in enumerate(enharmonic_notes):
        if first_note in notes:
            semitone_degree = counter

    return semitone_degree


# generowanie pauzy
def generate_pause(full_time, rythmic_values, file):
    # czas trwania pauzy
    ind = randint(0, len(rythmic_values) - 1)
    rest_duration = rythmic_values[ind]

    # sprawdzamy czy wartość rytmiczna nie wychodzi poza ostatni takt
    # jeśli wychodzi, to ją zmniejszamy, aż do uzyskania odpowiedniej
    while 1 / rest_duration[0] > full_time:
        ind += 1
        rest_duration = rythmic_values[ind]

    file.write(" r" + rest_duration[1])
    print("rest")

    return rest_duration


# generowanie pierwszej nuty
def generate_first_note(first_note, rythmic_values, full_time, file):
    fnote = Note()
    fnote.pitch = first_note

    ind = randint(0, len(rythmic_values) - 1)
    fnote.time_stamp, time_str = rythmic_values[ind]

    while 1 / fnote.time_stamp > full_time:
        ind += 1
        fnote.time_stamp, time_str = rythmic_values[ind]

    file.write(fnote.pitch + time_str)
    print(first_note.replace(" ", ""))

    return fnote.time_stamp

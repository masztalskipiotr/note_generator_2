from random import choice
from itertools import repeat


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

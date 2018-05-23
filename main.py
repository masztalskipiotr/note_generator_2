from random import random
from notes_generator import *
from interval_generator import intervals
from setup import *
from main_functions import *

# jeśli prawdopodobieństwo wystąpienia każdego z interwałów
# jest zerowe, to wypełniamy takty pauzami
if not intervals:
    rest_prob = 1
else:
    rest_prob = rest_prob

# inicjacja zmiennych opisujących wysokości dźwięków
interval_degree = first_note_interval_degree(first_note, notes_name)
semitone_degree = first_note_semitone_degree(first_note, enharmonic_notes)
next_interval_degree = first_note_interval_degree(first_note, notes_name)
next_semitone_degree = first_note_semitone_degree(first_note, enharmonic_notes)

with open('generator.ly', 'w') as file1:
    file1.write(header)
    file1.write("{ \\time %d/4" % tempo)
    full_time = bar_count / (4 / tempo)
    first_note_generated = False  # flaga wygenerowania pierwszej nuty
    initial_pause_generated = False  # flaga wygenerowania pauzy na początku pliku

    # generujemy pauzę z prawdopodobieństwem zdefiniowanym przez użytkownika
    if random() <= rest_prob:

        rest_duration = generate_pause(full_time, rythmic_values, file1)
        full_time -= 1 / rest_duration[0]

    else:

        # pierwsza nuta
        f_note_duration = generate_first_note(first_note, rythmic_values, full_time, file1)
        full_time -= (1 / f_note_duration)
        first_note_generated = True

    while full_time > 0:
        rest_generated = False

        # generujemy pauzę z prawdopodobieństwem zdefiniowanym przez użytkownika
        if random() <= rest_prob:

            # jeśli wygenerowaliśmy pauzę na początku to w pierwszej iteracji
            # pomijamy blok generowania pauz, aby nie zaburzyć prawdopodobieństwa
            if initial_pause_generated:
                initial_pause_generated = False
            else:
                rest_duration = generate_pause(full_time, rythmic_values, file1)
                full_time -= 1 / rest_duration[0]

        else:
            # jeśli nie wygenerowaliśmy pierwszej nuty, bo wcześniej są same pauzy
            # to musimy ją wygenerować
            if not first_note_generated:

                f_note_duration = generate_first_note(first_note, rythmic_values, full_time, file1)
                full_time -= (1 / f_note_duration)
                first_note_generated = True

            # jeśli wcześniej wygenerowano pierwszą nutę, przechodzimy do normalnego działania programu
            else:
                # jeśli nie generujemy pauzy to generujemy nutę
                note = Note()

                # RYTM (tak jak w pauzie)
                ind = randint(0, len(rythmic_values) - 1)
                note.time_stamp, time_str = rythmic_values[ind]

                while 1 / note.time_stamp > full_time:
                    ind += 1
                    note.time_stamp, time_str = rythmic_values[ind]

                full_time -= 1 / note.time_stamp

                # MELODIA
                idx = randint(0, len(intervals) - 1)
                interval = intervals[idx]

                # sprawdzmy czy po skoku o dany iterwał w górę lub w dół zmieścimy się w ambitusie
                # jeśli się nie mieścimy, wybieramy mniejszy interwał
                # jeśli nie istnieje interwał, który spełnia założenia ambitusu zmuszamy program
                # do wygenerowania pauzy

                while True:
                    # sprawdzamy indeks półtonów dla interwału w górę i w dół
                    next_interval_degree_down = interval_degree - interval.degree  # rozmiar
                    next_semitone_degree_down = semitone_degree - interval.semitones  # półtony

                    next_interval_degree_up = interval_degree + interval.degree  # rozmiar
                    next_semitone_degree_up = semitone_degree + interval.semitones  # półtony

                    if next_semitone_degree_down < lowest_semitone_degree and \
                       next_semitone_degree_up > highest_semitone_degree:

                        # jeśli dźwięki nie mieszczą się w ambitusie, losujemy mniejszy interwał
                        try:
                            interval = choice(intervals[:idx])
                            idx -= 1

                        # jeśli nie istnieje taki interwał generujemy pauzę
                        except:
                            full_time += 1 / note.time_stamp
                            ind = randint(0, len(rythmic_values) - 1)
                            rest_duration = rythmic_values[ind]

                            while 1 / rest_duration[0] > full_time:
                                ind += 1
                                rest_duration = rythmic_values[ind]

                            file1.write(" r" + rest_duration[1])
                            full_time -= 1 / rest_duration[0]
                            rest_generated = True
                            print("rest")
                            break
                    else:
                        break

                # jeśli wygenerowano pauzę, przechodzimy do następnej iteracji pętli
                if rest_generated:
                    continue

                # jeśli nie można iść do góry, ale można iść w dół, to idziemy w dół
                if next_semitone_degree_up > highest_semitone_degree and \
                   next_semitone_degree_down >= lowest_semitone_degree:

                    print(interval.name + " down")
                    next_interval_degree = next_interval_degree_down  # rozmiar
                    next_semitone_degree = next_semitone_degree_down  # półtony

                # jeśli nie można iść w dół, ale można iść do góry , to idziemy do góry
                elif next_semitone_degree_up <= highest_semitone_degree and \
                        next_semitone_degree_down < lowest_semitone_degree:

                    print(interval.name + " up")
                    next_interval_degree = next_interval_degree_up  # rozmiar
                    next_semitone_degree = next_semitone_degree_up  # półtony

                # jeśli można iść w górę lub w dół to o kierunku decyduje prawdopodobieństwo
                # wystąpienia konkretnej wysokości w ramach oktawy
                else:
                    prob_down = 0
                    prob_up = 0

                    for pitch in pitch_prob:
                        for note in enharmonic_notes[next_semitone_degree_down]:
                            if pitch[0] in note:
                                prob_down += pitch[1]

                        for note in enharmonic_notes[next_semitone_degree_up]:
                            if pitch[0] in note:
                                prob_up += pitch[1]

                    direction = evaluate_pitch_direction(prob_up, prob_down)

                    if direction == 1:
                        print(interval.name + " up")
                        next_interval_degree = next_interval_degree_up  # rozmiar
                        next_semitone_degree = next_semitone_degree_up  # półtony
                    else:
                        print(interval.name + " down")
                        next_interval_degree = next_interval_degree_down  # rozmiar
                        next_semitone_degree = next_semitone_degree_down  # półtony

                note_signature_too_long = True  # flaga zmiany znaków

                # jeśli znajdujemy wspólną wartość w wektorach odpowiadających
                # za stopień interwału i liczbę półtonów to jest to szukana nuta
                for note in notes_name[next_interval_degree]:
                    if note in enharmonic_notes[next_semitone_degree]:
                        file1.write(note + time_str)
                        print(note.replace(" ", ""))
                        note_signature_too_long = False

                # jeśli nie ma wspólnej wartości w wektorach odpowiadających
                # za stopień interwału i liczbę półtonów to znaczy, że potrzebujemy
                # ponad 2 znaków przy nucie, w takim wypadku szukamy enharmonicznego
                # zamiennika losując nutę z komórki odpowiadającej tej samej wysokości
                if note_signature_too_long:
                    note = choice(enharmonic_notes[next_semitone_degree])
                    file1.write(note + time_str)
                    print(note.replace(" ", ""))

                    # podmieniliśmy nutę, więc musimy podmienić również stopień interwału
                    # odpowiadający tej nucie
                    for counter, notes in enumerate(notes_name):
                        if note in notes:
                            next_interval_degree = counter

            # przeazujemy obecne położenie nuty do następnej iteracji pętli
            interval_degree = next_interval_degree
            semitone_degree = next_semitone_degree

    file1.write('\\bar "||" }')

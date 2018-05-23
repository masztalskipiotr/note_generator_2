notes_name = [[" ceses", " ces", " c", " cis", " cisis"],
              [" deses", " des", " d", " dis", " disis"],
              [" eeses", " ees", " e", " eis", " eisis"],
              [" feses", " fes", " f", " fis", " fisis"],
              [" geses", " ges", " g", " gis", " gisis"],
              [" aeses", " aes", " a", " ais", " aisis"],
              [" beses", " bes", " b", " bis", " bisis"]]
notes_name_3 = []
notes_name_2 = []
notes_name_1 = []
notes_name1 = []
notes_name2 = []
notes_name3 = []
notes_name4 = []
notes_name5 = []

for vector in notes_name:
    notes_name_1.append([x + "," for x in vector])

for vector in notes_name:
    notes_name_2.append([x + ",," for x in vector])

for vector in notes_name:
    notes_name_3.append([x + ",,," for x in vector])

for vector in notes_name:
    notes_name1.append([x + "'" for x in vector])

for vector in notes_name:
    notes_name2.append([x + "''" for x in vector])

for vector in notes_name:
    notes_name3.append([x + "'''" for x in vector])

for vector in notes_name:
    notes_name4.append([x + "''''" for x in vector])

for vector in notes_name:
    notes_name5.append([x + "'''''" for x in vector])

notes_name_full = [notes_name_2, notes_name_1, notes_name, notes_name1,
                   notes_name2, notes_name3, notes_name4, notes_name5]

for el in notes_name_full:
    for vector in el:
        notes_name_3.append(vector)

notes_name = notes_name_3

if __name__ == '__main__':
    print(notes_name)

enharmonic_notes = [[" c", " bis,", " deses"], [" cis", " bisis,", " des"],
                    [" d", " cisis", " eeses"], [" dis", " ees", " feses"],
                    [" e", " disis", " fes"], [" f", " eis", " geses"],
                    [" fis", " eisis", " ges"], [" g", " fisis", " aeses"],
                    [" gis", " aes"], [" a", " gisis", " beses"],
                    [" ais", " bes", " ceses'"], [" b", " aisis", " ces'"]]

enharmonic_notes_3 = []
enharmonic_notes_2 = []
enharmonic_notes_1 = []
enharmonic_notes1 = []
enharmonic_notes2 = []
enharmonic_notes3 = []
enharmonic_notes4 = []
enharmonic_notes5 = []

for vector in enharmonic_notes:
    enharmonic_notes_1.append([x + "," for x in vector])

for vector in enharmonic_notes:
    enharmonic_notes_2.append([x + ",," for x in vector])

for vector in enharmonic_notes:
    enharmonic_notes_3.append([x + ",,," for x in vector])

for vector in enharmonic_notes:
    enharmonic_notes1.append([x + "'" for x in vector])

for vector in enharmonic_notes:
    enharmonic_notes2.append([x + "''" for x in vector])

for vector in enharmonic_notes:
    enharmonic_notes3.append([x + "'''" for x in vector])

for vector in enharmonic_notes:
    enharmonic_notes4.append([x + "''''" for x in vector])

for vector in enharmonic_notes:
    enharmonic_notes5.append([x + "'''''" for x in vector])


enharmonic_notes_full = [enharmonic_notes_2, enharmonic_notes_1, enharmonic_notes, enharmonic_notes1,
                         enharmonic_notes2, enharmonic_notes3, enharmonic_notes4, enharmonic_notes5]

for el in enharmonic_notes_full:
    for vector in el:
        enharmonic_notes_3.append(vector)

enharmonic_notes = enharmonic_notes_3

for idx1, vector in enumerate(enharmonic_notes):
    for idx2, el in enumerate(vector):
        if "'," in el:
            enharmonic_notes[idx1][idx2] = el.replace("',", "")

for idx1, vector in enumerate(enharmonic_notes):
    for idx2, el in enumerate(vector):
        if ",'" in el:
            enharmonic_notes[idx1][idx2] = el.replace(",'", "")

if __name__ == '__main__':
    print(enharmonic_notes)

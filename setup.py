from notes_generator import enharmonic_notes
from config import *

rythmic_values = [[1, '1'], [4 / 3, '2.'], [2, '2'], [8 / 3, '4.'], [4, '4'],
                  [16 / 3, '8.'], [8, '8'], [16, '16']]

header = '\\version "2.18.2" \n\
\paper {\n\
#(set-paper-size "a4landscape") \n\
} \n\
\header { \n\
  title = "LILIJE" \n\
  composer = "A. Mickiewicz" \n\
} \n\
\layout{ \n\
  indent = 0\in \n\
  ragged-last = ##f \n\
  \context { \n\
    \Score \n\
  } \n\
}\\new Voice \with { \n\
  \\remove "Note_heads_engraver" \n\
  \\consists "Completion_heads_engraver" \n\
  \\remove "Rest_engraver" \n\
  \\consists "Completion_rest_engraver"}'

lowest_semitone_degree = 0
highest_semitone_degree = 0

# obliczamy indeksy półtonów dla najwyższej i najniższej nuty
for counter, notes in enumerate(enharmonic_notes):
    if lowest_note in notes:
        lowest_semitone_degree = counter
    if highest_note in notes:
        highest_semitone_degree = counter

# inicjacja tablicy pozwalającej uzależniać kierunek skoku interwału
# od prawdopodobieństwa wystąpienia konkretnej wysokości

c = ["c", c_prob]
cis = ["cis", cis_prob]

d = ["d", d_prob]
dis = ["dis", dis_prob]

e = ["e", e_prob]
eis = ["eis", eis_prob]

f = ["f", f_prob]
fis = ["fis", fis_prob]

g = ["g", g_prob]
gis = ["gis", gis_prob]

a = ["a", a_prob]
ais = ["ais", ais_prob]

b = ["b", b_prob]
bis = ["bis", bis_prob]

pitch_prob = [c, cis, d, dis, e, eis, f, fis, g, gis, a, ais, b, bis]

if __name__ == '__main__':
    print(lowest_semitone_degree, highest_semitone_degree)

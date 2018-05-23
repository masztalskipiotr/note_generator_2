\version "2.18.2" 
\paper {
#(set-paper-size "a4landscape") 
} 
\header { 
  title = "LILIJE" 
  composer = "A. Mickiewicz" 
} 
\layout{ 
  indent = 0\in 
  ragged-last = ##f 
  \context { 
    \Score 
  } 
}\new Voice \with { 
  \remove "Note_heads_engraver" 
  \consists "Completion_heads_engraver" 
  \remove "Rest_engraver" 
  \consists "Completion_rest_engraver"}{ \time 4/4 c'8 aes'4. c'4. beses'4 beses'1 aeses'16 g''8 aes'8. fis''2. c''8. c''2 des'16\bar "||" }
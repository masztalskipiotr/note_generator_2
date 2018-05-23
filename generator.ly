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
  \consists "Completion_rest_engraver"}{ \time 4/4 d'4. cis'2. ees'1 deses'1 bisis2. dis'8\bar "||" }
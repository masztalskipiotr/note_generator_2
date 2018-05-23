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
  \consists "Completion_rest_engraver"}{ \time 4/4 c'4 fis'4. ees''16 fes'2 ceses''1 d''2 a'4. dis''2. a'8.\bar "||" }
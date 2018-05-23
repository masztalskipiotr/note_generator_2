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
  \consists "Completion_rest_engraver"}{ \time 4/4 d'8. e'2 d'2. des'1 fes'2. e'4 disis'2 bisis16\bar "||" }
musicOne = {
	g'4 g'4 a'2 g'2 c''2 b'2 r2 g'4 g'4 a'2 g'2 d''2 c''2 r2 g'4 g'4 g''2 e''2 c''2 b'2 a'2 r2 f''4 f''4 e''2 c''2 d''2 \override NoteHead.color = #red c''2 \override NoteHead.color = #black
}
verseOne = \lyricmode {
	Hap py birth day to you, hap py birth day to you, hap py birth day to you u, hap py birth day to you.
}
\score {
	<<
		\new Voice = "one" {
			\time 4/4
			\musicOne
		}
		\new Lyrics \lyricsto "one" {
			\verseOne
		}
	>>
}
musicOne =  {
  c4 b'8. a'16 g'4. f'8 e'4 d' c'2 c''2
}
verseOne = \lyricmode {
  Joy to the world, the Lord is come. 
}
\score {
  <<
    \new Voice = "one" {
      \time 2/4
      \musicOne
    }
    \new Lyrics \lyricsto "one" {
      \verseOne
    }
  >>
}
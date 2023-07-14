# cz-inflect
Inflection of Czech nouns

To build the project requirements, run
`bash build.sh`

To run the inflection script after building the requirements, run
`bash run.sh`

The inflection script reads stdin line by line. It expects one lemma (Czech noun in base form) per line.
It prints the tab-separated inflected forms to stdout.
The number of produced forms is 14 and they are printed in the following order:
S1	S2	S3	S4	S5	S6	S7	P1	P2	P3	P4	P5	P6	P7

(S=singular, P=plural, 1..7 are cases numbered as usual in Czech morphology: 1=nominative, ..., 7=instrumental)


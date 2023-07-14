# cz-inflect

## Inflection of Czech nouns

This project provides a morphological guesser for inflection of Czech nouns. It focuses on inflection of out-of-vocabulary words. (For other words we recommend MorphoDiTa tool https://lindat.mff.cuni.cz/services/morphodita/ )

The guesser is a LSTM-based encoder-decoder architecture with attention, trained with OpenNMT-py library on a training dataset consisting of approx. 360k Czech noun lemmata (data source: MorfFlex2.0 https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3186 ).


### On Linux

To build the project requirements, run
`bash build.sh`

To run the inflection script after building the requirements, run
`bash run.sh`

### Otherwise

Install python3 dependencies from file requirements.txt to you environment (ideally virtualenv).
Run the inflect.py script from the environment.

### Script information
To exit the running program, press `Ctrl+D`.

The inflection script reads stdin line by line. It expects one lemma (Czech noun in base form) per line.
It prints the tab-separated inflected forms to stdout.
The number of produced forms is 14 and they are printed in the following order:
S1	S2	S3	S4	S5	S6	S7	P1	P2	P3	P4	P5	P6	P7

(S=singular, P=plural, 1..7 are cases numbered as usual in Czech morphology: 1=nominative, ..., 7=instrumental)

#### Examples
Example input:
jablko

Example output:
jablko	jablka	jablku	jablko	jablko	jablku	jablkem	jablka	jablek	jablkům	jablka	jablka	jablkách	jablky

 
Example input:
pes

Example output (incorrect prediction):
pes	pesu	psi	pes	pese	psi	psem	psi	psů	psům	pse	psi	pesech	psi


### Additional information
Inflection of the first lemma takes relatively long time (~10s) due to loading the inflection model, other lemmata are inflected more quickly.

The inflection system is case-sensitive. It is not able to inflect phrases (it automatically deletes spaces in the input sequence). It is not capable of inflecting words containing almost any of special characters ('-', '_', ...), and it substitutes such characters by a character from its vocabulary.


#!/usr/bin/env python3


from inflect import inflect

# Inflecting a single lemma

lemma = "diskrétka"
inflected_forms = inflect(lemma)

print(f"Inflected forms of lemma {lemma}:")
print(", ".join(inflected_forms))


# Inflecting a list of lemmata

lemmata = ["lingebra", "matfyzák"]
inflected_lemmata = inflect(lemmata)

for (lemma, inflected_forms) in zip(lemmata, inflected_lemmata):
	print(f"Inflected forms of lemma {lemma}:")
	print(", ".join(inflected_forms))

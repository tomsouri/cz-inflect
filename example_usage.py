#!/usr/bin/env python3


from inflect import inflect

# Inflecting a single lemma

lemma = "jablko"
inflected_forms = inflect(lemma)

print(f"Inflected forms of lemma {lemma}:")
for form in inflected_forms:
	print(form)
print()


# Inflecting a list of lemmata

lemmata = ["kočka", "pes"]
inflected_lemmata = inflect(lemmata)

for (lemma, inflected_forms) in zip(lemmata, inflected_lemmata):
	print(f"Inflected forms of lemma {lemma}:")
	for form in inflected_forms:
		print(form)
	print()

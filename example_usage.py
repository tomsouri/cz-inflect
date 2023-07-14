#!/usr/bin/env python3


from inflect import inflect

lemma = "jablko"
inflected_forms = inflect(lemma)

print(f"Inflected forms of lemma {lemma}:")
for form in inflected_forms:
	print(form)

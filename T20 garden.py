import spacy

gardenpathSentences = ["The complex houses married and single soldiers and their families.",
                       "She told me a little white lie will come back to haunt me.",
                       "Mary gave the child a Band-Aid", "That Jill is never here hurts", 
                       "The cotton clothing is made of grows in Mississippi"]

nlp = spacy.load('en_core_web_sm')

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for token in doc:
        print([token.text, token.pos_])


namedEntity = []

for token in gardenpathSentences:
    doc = nlp(token)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    namedEntity.append(entities)

print(namedEntity)

print(spacy.explain("PROPN"))
print(spacy.explain("PERSON"))
print(spacy.explain("GPE"))

'''
I asked spaCy to explain PROPN, PERSON and GPE.
PROPN refers to a proper noun - tokens identified as PROPN are used in the EntityRecognizer
PERSON refers to any people including fictional characters,
for instance our list included Mary and Jill who are presumably two people.
GPE or Geopolitical entity refers to countries, cities or states.
Mississippi falls in this category as a state in the USA.
'''




    
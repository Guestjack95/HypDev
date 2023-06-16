import spacy

nlp = spacy.load('en_core_web_md')


word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word2.similarity(word3))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens: 
            print(token1.text, token2.text, token1.similarity(token2))
            

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I've lost my car in my car",
"I'd like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

'''
Run the example file with the simpler language model 'en_core_web_sm' and write a note on what you notice is different from the model 'en_core_web_md'

With the sm model, cat and monkey have decently high similarity (0.601) which matches our expectation
However there are some strange elements here - apple has high similarity with cat and monkey (0.696, 0.750), even moreso than cat and monkey have with each other
It identifies apple as having some similar features to both cat and monkey - perhaps it thinks apple is an animal? - it also has low similarity to banana
Banana has low similarity with all the other words.

With the md model, the similarities seem to map more closely to our intuitions
cat monkey (0.593) and apple banana (0.665) have decently high similarity being pairs of animals and fruit respectively
banana monkey (0.404) starts to have some similarity here also, identifying the common theme of monkeys eating bananas
The other items have low similarity as they don't have much obvious connection.

Another example could be: man, dog, bone
It would be interesting to see if spaCy identifies any similarities.
For example: man and dog being animals/mammals, both having bones, the themes of 'a dog with a bone' or dogs as 'man's best friend'

As for the sentence comparisons, in 'en_core_web_sm' spaCy identifies "Hello, there is my car" is the most similar sentence (0.565) followed by "I've lost my car in my car" (0.548)
'en_core_web_md' agrees that "Hello, there is my car" is the most similar sentence (0.803) and "I've lost my car in my car" remains the second most similar (0.679) 
but the difference between the two is larger - spaCy is much more confident about "Hello, there is my car" in the md model.
'''
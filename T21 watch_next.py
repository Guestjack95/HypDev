import spacy

nlp = spacy.load('en_core_web_md')

'''
Given the format of movies.txt being  name :description , movie_desc performs 2 splits. 
Firstly each line is split into an independent item 
Then the names and descriptions are split from one another and stripped of whitespace to form a dictionary.
'''
def movie_desc(file_path):
    movies_dict = {}
    with open(file_path, "r") as file:
        desc = file.read().splitlines()

    for line in desc:
        key, value = line.split(":")
        movies_dict[key.strip()] = value.strip()

    return movies_dict

'''
most_similar_movie requires a test_sentence and a dictionary as inputs
Using spaCy it checks the similarity of our test_sentence and each value in our dictionary
If similarity is higher than most_similar the variables most_similar and most_similar_key are updated 
After iterating over the entire dictionary, most_similar_key is returned
This contains the key of the dictionary item most similar to our test_sentence
'''
def most_similar_movie(test_sentence, dictionary):
    most_similar = 0.00
    most_similar_key = None

    for key, value in dictionary.items():
        doc1 = nlp(test_sentence)
        doc2 = nlp(value)
        similarity = doc1.similarity(doc2)

        if similarity > most_similar:
            most_similar = similarity
            most_similar_key = key
            
    return most_similar_key

file_path = 'movies.txt'

#Take the contents of movies.txt and apply our movie_desc function to it convert to a dictionary
descriptions = movie_desc(file_path)

comparison_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

#Compare the similarity of our comparison_description to the descriptions dictionary
recommendation = most_similar_movie(comparison_description, descriptions)

print(f"If you enjoyed Planet Hulk, you might also like {recommendation}.")
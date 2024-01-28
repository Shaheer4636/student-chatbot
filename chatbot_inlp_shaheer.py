# -*- coding: utf-8 -*-
"""Chatbot_INLP_Shaheer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ERE25AYCwzTrEBJg6vXfjaoxu_Knk_Fu
"""

!pip install nltk

!pip install tokenizers

!pip install punkt

import os
os.environ["NLTK_DATA"] = "/path/to/nltk_data"

!pip install --upgrade nltk

import nltk


nltk.download('all')

!pip install transformers

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import random

# Set the NLTK data directory
nltk.data.path.append("path/to/nltk_data_directory")

# Load the training data from a text file
def load_training_data(dialog_stu_teacher):
    with open(dialog_stu_teacher, 'r') as file:
        training_data = file.readlines()
    return training_data

# Preprocess the training data
def preprocess_data(data):
    preprocessed_data = []
    for sentence in data:
        preprocessed_sentence = preprocess_sentence(sentence)
        preprocessed_data.append(preprocessed_sentence)
    return preprocessed_data

# Preprocess a single sentence
def preprocess_sentence(sentence):
    tagged_sentence = pos_tag(word_tokenize(sentence))
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    processed_tokens = [lemmatizer.lemmatize(token.lower(), get_wordnet_pos(tag)) for token, tag in tagged_sentence if token.lower() not in stop_words and tag.startswith('NN')]
    preprocessed_sentence = ' '.join(processed_tokens)
    preprocessed_sentence = remove_phrases(preprocessed_sentence)
    return preprocessed_sentence

# Remove specific phrases from the sentence
def remove_phrases(sentence):
    phrases_to_remove = ["what is", "i mean"]
    for phrase in phrases_to_remove:
        sentence = sentence.replace(phrase, "")
    return sentence

# Extract keywords from the preprocessed sentence
def extract_keywords(sentence):
    keywords = []
    tagged_sentence = pos_tag(word_tokenize(sentence))
    for token, tag in tagged_sentence:
        if tag.startswith('NN') or tag.startswith('VB'):
            keywords.append(token.lower())
    return keywords

# Get WordNet POS tag
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # default to noun if not recognized

# Train the chatbot on the preprocessed data
def train_chatbot(training_data):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(training_data)
    return vectorizer, tfidf_matrix

# Generate a response based on the user input and keywords
def generate_response(vectorizer, tfidf_matrix, training_data, query, keywords, conversation_history):
    preprocessed_query = preprocess_sentence(query)
    query_vector = vectorizer.transform([preprocessed_query])
    similarities = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_index = similarities.argmax()
    response = training_data[most_similar_index]

    # Process the response based on the keywords and conversation history
    processed_response = process_response(response, keywords, conversation_history)

    return processed_response

# Process the response based on the keywords and conversation history
def process_response(response, keywords, conversation_history):
    # Example modifications based on suggested techniques
    if keywords and conversation_history:
        previous_query, previous_response = conversation_history[-1]

        # Check if the previous query is related to the current response
        previous_keywords = extract_keywords(previous_query)
        if set(previous_keywords).intersection(keywords):
            response = modify_response(response, previous_response)

    return response

# Modify the response based on the previous response
def modify_response(response, previous_response):
    # Example modifications based on suggested techniques
    if previous_response.startswith("I don't know"):
        response = "Sorry, I still don't know the answer to that."

    return response

# Example conversation loop
def chat():
    dialog_stu_teacher = "/content/dialog_stu_teacher.txt"
    training_data = load_training_data(dialog_stu_teacher)
    preprocessed_data = preprocess_data(training_data)
    vectorizer, tfidf_matrix = train_chatbot(preprocessed_data)

    print("Welcome to the Chatbot!")
    print("You can start chatting with the bot. Enter 'exit' to quit.")

    conversation_history = []

    while True:
        query = input("User: ")
        if query.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        keywords = extract_keywords(query)
        response = generate_response(vectorizer, tfidf_matrix, training_data, query, keywords, conversation_history)
        conversation_history.append((query, response))

        print("Chatbot:", response)

# Run the chat function
chat()
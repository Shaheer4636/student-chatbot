# Student-Teacher Interaction Chatbot

## Overview

This project implements a student-teacher interaction chatbot using Python, NLTK (Natural Language Toolkit), and scikit-learn. The chatbot is trained on a dataset containing dialogues between students and teachers, aiming to generate context-aware responses based on user input and extracted keywords.

## Technologies Used

- **Python**: The primary programming language for chatbot development.
- **NLTK**: Utilized for natural language processing tasks such as tokenization, part-of-speech tagging, and sentiment analysis.
- **scikit-learn**: Implemented for TF-IDF vectorization, transforming text data into numerical vectors.
- **Cosine Similarity**: Employed to measure the similarity between user queries and training data.
- **Random Responses**: Added randomness to responses for a more natural conversation.

## Project Structure

- **chatbot.py**: The main Python script containing the chatbot implementation.
- **dialog_stu_teacher.txt**: A text file containing training data extracted from student-teacher dialogues.

### Install Dependencies:
```pip install nltk scikit-learn```

### Run the Chatbot:
```python chatbot.py```

### Example use 

#### User
```How can I register for a course?```

#### Bot 
``` To register for a course, please visit the course registration page on our student portal. ```








# Tkinter GUI Quiz App

This is a simple quiz application built with Python using the Tkinter library for the graphical user interface. The app fetches trivia questions from the Open Trivia Database API (https://opentdb.com) and presents them to the user in a true/false format.

## Features

- Fetches trivia questions from the Open Trivia Database API
- Presents questions in a true/false format
- Displays questions on a card
- Uses tick and cross buttons for answering questions
- Tracks and displays the user's score on top
- Provides immediate feedback on whether the selected answer is correct or incorrect

## Usage
Run the **main.py** script to start the application

## Project Structure
- main.py: The logic for fetching and displaying quiz questions.
- ui.py: Contains the Tkinter GUI.
- data.py: A helper module for making API calls to the Open Trivia Database.
- quiz_brain.py: A module for handling the quiz questions and user's answers.
- question_model.py: Contains the question model for the current question and the corresponding answer.
- README.md: This file.

## API Integration
The application uses the Open Trivia Database API to fetch quiz questions. You can modify the API call parameters in data.py to customize the number of questions, type, category, etc.

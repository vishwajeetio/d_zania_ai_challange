# RAG CLI Application

## Description
This CLI application processes a PDF document, extracts relevant information to answer given questions, and posts the results on Slack.

## Features
- Extract text from PDF
- Generate embeddings using OpenAI API
- Store embeddings in local ChromaDB
- Retrieve relevant chunks for a given question
- Generate answers using OpenAI API
- Save answers to results.json file and print them to the console

## Prerequisites
- Python 3.12 with pip
- OpenAI API key

## Installation
1. Clone the repository
2. Copy the `.env.example` file to `.env` and fill in the required values
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```



## Usage

python main.py <pdf_path> <question1> <question2> ...

## Example
python main.py handbook.pdf "What is the main topic?"


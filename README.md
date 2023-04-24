# OpenAI API Novel Writing Helper

This web application helps novel writers generate conversations between their characters using the OpenAI GPT-3.5 API. The app is built using Flask for the server-side and HTML, CSS, and JavaScript for the client-side.

## Features

- Add multiple characters with names, personalities, and background information.
- Specify the novel's synopsis and length.
- Generate a conversation between the characters based on the provided information.

## Prerequisites

- Python 3.6 or later
- Poetry
- An OpenAI API key (You can get one by signing up at OpenAI)

## Installation

Clone the repository:

```bash
git clone <https://github.com/yourusername/openai-novel-writing-helper.git>
```

Change to the project directory:

```bash
cd openai-novel-writing-helper/server
```

Install the required Python packages using Poetry:

```bash
poetry install
```

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key"
# Replace your-api-key with your actual API key.
```

## Running the Application

1. Activate the Poetry virtual environment:

```bash
poetry shell
```

1. Inside the server directory, run the Flask application:

```bash
python app.py
```

Open your browser and go to <http://127.0.0.1:5000/> to see the web application.

## Usage

1. Add character details by clicking the "Add Character" button. You can add as many characters as you want.
1. Fill in the character information (name, personalities, and background) for each character.
1. Provide the novel's synopsis and length (in pages).
1. Click the "Generate Conversation" button to generate a conversation between the characters based on the provided information. The generated conversation will be displayed below the button.

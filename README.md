# Jarvis 2.0

Jarvis is an extensive, modular, AI driven assistant. It's helpful, user friendly, and easily accessible via voice or text. It's also open source, so you can customize it to your liking.

## Installation

To begin, install the required packages:

```bash
pip install -r requirements.txt
```

You will then need to generate an OpenAI API key, which you can do [here](https://beta.openai.com/). Once you have your API key, add it to a file called `.env` with the following statement:

```
OPENAI_API_KEY=key_here
```

## Usage

To run Jarvis, simply run the following command:

```bash
python main.py
```

## Configuration

The config is located in the `config.json` file, which contains all of the options for Jarvis.

## Plugins - How it works

Plugins are split into two different methods, functions and modules. Both functions and modules are used for commands, but they are used in different ways.

### Modules

Modules are user defined commands that are pre-built into the system. These are intext commands that are used to replace a command in text. For example, if the user asks for the current time, Jarvis will use the time module to get the current time and add it to the response.

### Functions

Functions are commands that are created on the fly. Functions can modify your system and run anything as code. For example, if the user asks to open a file, Jarvis will create a function that opens the file and then run it.

## Memory - How it works

Jarvis uses two different types of memory methods. Short term and long term.

### Short Term

Short term memory is used to store information currently relevent to the conversation. It stores as much information as it can, and is easily accessible to the AI. However, there is a limit to how much information can be stored in short term memory, and old information is pruned.

### Long Term

Long term memory is used to store information in the long term, and can store an unlimited amount of information. When you talk to the AI, it will see if it can recall information from long term memory, and if it can, it will use that information to answer your question.

## AI

Jarvis uses multiple different AI models in the background. All of the models use OpenAI's GPT models, such as GPT-4 and GPT-3.5. The models are used to generate responses to the user, generate code for functions, and search long term memory for relevant information.

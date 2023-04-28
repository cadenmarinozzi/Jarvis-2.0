from openai.embeddings_utils import cosine_similarity
from dotenv import load_dotenv
import openai, os

load_dotenv();

openai.api_key = os.getenv('OPENAI_API_KEY');

def createCompletion(messages, model='gpt-4', state=None):
    if (state and not state.config['has_gpt4']):
        model = 'gpt-3.5-turbo';

    completion = openai.ChatCompletion.create(model=model, messages=messages)

    return completion.choices[0].message.content;

def createEmbedding(text):
    embedding = openai.Embedding.create(input=text, model='text-embedding-ada-002');

    return embedding['data'][0]['embedding'];

def getSimilarity(x, inputEmbedding):
    return cosine_similarity(x, inputEmbedding);
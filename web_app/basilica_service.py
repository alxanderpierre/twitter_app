
import basilica
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(API_KEY)

if __name__ =="__main__": # only if this is running from the command name
    sentences = ["Hello world?", "how are you today"]
    embeddings = connection.embed_sentences(sentences)
    print(type(embeddings))

    for embedding in embeddings:
        print(len(embedding)) #> 768
        print(list(embedding))
        print("-----------")
    #[[0.8556405305862427, ...], ...]

from langchain.document_loaders import TextLoader, WebBaseLoader
from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.indexes import VectorstoreIndexCreator
from dotenv import dotenv_values
import os
import sys
# Document loader
config = dotenv_values(".env")
os.environ["OPENAI_API_KEY"]  = config["OPENAI_API_KEY"]

# print(sys.argv[1])
# loader = TextLoader('text.txt')
loader = RecursiveUrlLoader("https://github.com/SagarDollin/QuantumComputerSimulator")

# loader = RecursiveUrlLoader(url=url)
# Lazy load each
docs = [print(doc) or doc for doc in loader.lazy_load()]



# https://python.langchain.com/docs/modules/data_connection/document_loaders/integrations/recursive_url_loader


# index = VectorstoreIndexCreator().from_loaders([loader])

# # Question-answering
# question = "Who has written qosf-simulator-task.ipynb"
# response = index.query(question, llm=None)
# print(response)
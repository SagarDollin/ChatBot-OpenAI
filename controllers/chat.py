from fastapi import HTTPException, status, Request

from models.chat import Query

from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.indexes import VectorstoreIndexCreator

def query_document_controller(request: Request, query: Query):
    """
    Controller function to query a document based on the provided query.

    Parameters:
        request (Request): The FastAPI Request object.
        query (Query): An instance of the Query model representing the search query.

    Returns:
        dict: The response containing the results of the query.

    Raises:
        HTTPException: If there are any errors during the query or document loading process.
    """
    try:
        # Create a RecursiveUrlLoader to load the document from the specified URL
        loader = RecursiveUrlLoader(url=query.url)
        # docs = loader.load()
        # print("len of docs:",len(docs))
        # Create an index using VectorstoreIndexCreator and load the document using the loader
        index = VectorstoreIndexCreator().from_loaders([loader])
        
        # Perform question-answering using the index and the provided query string
        response = index.query(query.query)
        
        return response
    
    except Exception as e:
        # If any errors occur during the process, raise an HTTPException with a 500 status code
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred during the query process.") from e

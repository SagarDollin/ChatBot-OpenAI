from fastapi import APIRouter, status, Request, HTTPException

from models.chat import Query
from controllers.chat import query_document_controller

router = APIRouter()

@router.post('/query_document', response_model=str, status_code=status.HTTP_200_OK, description='Send a query along with a document that will be used as context by the OpenAI model.')
async def query_document(request: Request, query: Query):
    """
    API route to handle POST requests for querying a document.

    Parameters:
        request (Request): The FastAPI Request object containing the HTTP request information.
        query (Query): An instance of the Query model representing the search query.

    Returns:
        str: The response containing the results of the query.

    Raises:
        HTTPException: If there are any errors during the query or document loading process.
    """
    try:
        # Call the query_document_controller function to handle the query and document loading process
        response = query_document_controller(request, query)
        
        return response
    
    except Exception as e:
        # If any errors occur during the process, raise an HTTPException with a 500 status code
        # indicating an internal server error. The error details will be included in the response.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred during the query process.") from e

from pydantic import BaseModel, AnyHttpUrl

class Query(BaseModel):
    """
    Represents a query model with two fields: 'query' and 'url'.
    
    Attributes:
        query (str): The query string for the search.
            Default: 'Who is the author of this repository?'
        
        url (AnyHttpUrl): The URL for the search. 
            Default: 'https://github.com/SagarDollin/QuantumComputerSimulator'
    """
    query: str = 'Who is the author of this repository?'
    url: AnyHttpUrl = 'https://github.com/SagarDollin/QuantumComputerSimulator'

from fastapi import FastAPI
from dotenv import dotenv_values
import os

# Load environment variables from the .env file
config = dotenv_values(".env")

# Create a FastAPI application
app = FastAPI()

# Set environment variables during application startup
@app.on_event("startup")
def startup():
    """
    Function executed during application startup.

    This function sets environment variables, specifically the 'OPENAI_API_KEY',
    by loading their values from the .env file.
    """
    os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
    print("OpenAPI key has been set, the server has been started!")

# Perform cleanup during application shutdown
@app.on_event("shutdown")
def shutdown():
    """
    Function executed during application shutdown.

    This function is called when the FastAPI application is shutting down.
    It can be used to perform cleanup tasks or notify other services about the shutdown.
    """
    print("Shutting down the server")

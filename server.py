import uvicorn
from routes.chat import router as chat_router
from app import app, config, startup

# Define a route for the root endpoint
@app.get("/")
async def root():
    """
    Root endpoint that returns a JSON response with a message.

    This endpoint will return a message specified in the 'server_on_message' key
    from the configuration loaded earlier.
    """
    return {"message": config["server_on_message"]}

# Include the chat_router for chat-related endpoints
app.include_router(chat_router, tags=["Chat"], prefix="/chat")

# If this script is executed directly (not imported as a module), start the server
if __name__ == "__main__":
    # Run the FastAPI server using uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8001, log_level="info", reload=True)

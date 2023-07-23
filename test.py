import unittest
from fastapi.testclient import TestClient
from server import app, config, startup

# Call the startup function to set up the environment variables before running the tests
app.on_event("startup")(startup())

class TestChatAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root_endpoint(self):
        """
        Test case for the root endpoint ("/").

        This test sends a GET request to the root endpoint and checks if the response
        status code is 200 and the JSON response matches the expected message from the config.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": config['server_on_message']})

    def test_query_document_endpoint(self):
        """
        Test case for the "/chat/query_document" endpoint.

        This test sends a POST request to the "/chat/query_document" endpoint with some
        example query data and checks if the response status code is 200.
        You should add more assertions to validate the response data based on the expected
        behavior of the endpoint.
        """
        # Example Test Case:
        query_data = {
            "query": "Who is the author of this repository?",
            "url": "https://github.com/SagarDollin/QuantumComputerSimulator"
        }
        response = self.client.post("/chat/query_document", json=query_data)
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response data.

if __name__ == "__main__":
    unittest.main()

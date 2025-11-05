from unittest.mock import patch, MagicMock
# Assume APIClient class from previous slide is in a file named `api_client`
from pipeline.api_client import APIClient

@patch('requests.get')
def test_get_user_success(mock_get):
     """Tests a successful API call for a user."""
     # Arrange: Configure the mock to simulate a successful response
     mock_response = MagicMock()
     mock_response.status_code = 200
     mock_response.json.return_value = {"id": 1, "name": "Test User"}
     mock_get.return_value = mock_response
     # Act: Call the method we are testing
     client = APIClient()
     user_data = client.get_user(1)
     # Assert: Check that the method returned the expected data
     assert user_data["name"] == "Test User"
     # Assert that our mock was called correctly
     mock_get.assert_called_once_with("https://fakestoreapi.com/users/1")

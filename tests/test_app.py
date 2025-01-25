import warnings
import pytest
from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app

# Create a TestClient instance for testing
client = TestClient(app)


def test_health_check():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", PendingDeprecationWarning)
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"health_check": "OK", "model_version": 1}
        print(f"Health Check Response: {response.json()}")  # Display response in the report


@pytest.mark.parametrize("input_data,expected_status", [
    ({"Gender": "Male", "Age": 35, "HasDrivingLicense": 1, "RegionID": 5.0, "Switch": 0, "PastAccident": "Yes", "AnnualPremium": 12000.0}, 200),
    ({"Gender": "Male", "Age": "InvalidAge", "HasDrivingLicense": 1, "RegionID": 5.0, "Switch": 0, "PastAccident": "Yes", "AnnualPremium": 12000.0}, 422),
])
def test_prediction(input_data, expected_status):
    """Test the prediction endpoint with valid and invalid input."""
    response = client.post("/predict", json=input_data)
    print(f"Request Input: {input_data}")  # Log input data
    print(f"Response: {response.json()}")  # Log response in the pytest report

    assert response.status_code == expected_status

    if response.status_code == 200:
        result = response.json()
        assert "predicted_class" in result
        assert isinstance(result["predicted_class"], int)
    elif response.status_code == 422:
        error = response.json()
        assert "detail" in error  # Ensure validation error message is present

import json
import pytest

@pytest.fixture
def fig():
    """
    Read and parse the config JSON file.
    
    Returns:
        dict: Parsed JSON data as a dictionary
    """
    with open('test-suite/nonprod_config.json') as file:
        return json.load(file)
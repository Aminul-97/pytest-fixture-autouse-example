# Pytest Fixture Autouse Example
This repo contains the sample code for the article - [How to Auto-Request Pytest Fixtures Using "Autouse"](https://pytest-with-eric.com/pytest-advanced/pytest-fixture-autouse/).

The article explains how to use the `autouse` parameter of the `@pytest.fixture` decorator to automatically request a fixture for all tests in a module.

# Requirements
* Python (3.11+)

Please install the dependencies via the `requirements.txt` file using 
```bash
pip install -r requirements.txt
```
If you don't have Pip installed, please follow instructions online on how to do it.

# How To Run the Unit Tests
To run the Unit Tests from the root of the repo, run
```bash
pytest -v
```

If you have any questions about the project, please raise an Issue on GitHub. 

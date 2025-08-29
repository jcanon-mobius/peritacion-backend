import json
from lambda_functions.hello_world.app import lambda_handler

def test_hello_world():
    event = {"test": True}
    result = lambda_handler(event, None)
    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert body["message"].startswith("Hello from peritacion-backend")
    assert body["input"]["test"] is True
    print("Test 'test_hello_world' passed.")
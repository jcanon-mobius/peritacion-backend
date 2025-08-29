import json
from lambda_functions.uploads_presigns.app import lambda_handler

def test_post_upload_presign():
    event = {"body": json.dumps({"filename": "video.mp4"})}
    resp = lambda_handler(event, None)

    assert isinstance(resp, dict)
    assert resp.get("statusCode") == 200
    assert "body" in resp

    body = json.loads(resp["body"])
    assert isinstance(body, dict)
    assert "url" in body
    assert body["url"].startswith("https://s3-pre-signed-url-example.com/")
    assert body["url"].endswith("/video.mp4")
    print("Test 'test_presign_returns_200_and_url' passed.")
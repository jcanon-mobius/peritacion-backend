import json
from typing import Any, Dict, Optional

PREFIX = "https://s3-pre-signed-url-example.com"

def _extract_filename(event: Dict[str, Any]) -> str:
    body = event.get("body")
    if isinstance(body, str):
        try:
            data = json.loads(body)
            if isinstance(data, dict) and "filename" in data:
                return str(data["filename"])
        except json.JSONDecodeError:
            pass
    elif isinstance(body, dict) and "filename" in body:
        return str(body["filename"])
    if "filename" in event:
        return str(event["filename"])
    return "video.mp4"

def lambda_handler(event: Dict[str, Any], context: Optional[Any]) -> Dict[str, Any]:
    filename = _extract_filename(event)
    body = {"url": f"{PREFIX}/{filename}"}
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
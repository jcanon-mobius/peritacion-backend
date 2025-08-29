import json
from typing import Any, Dict

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    body = {
        "message": "Hello from peritacion-backend",
        "input": event or {},
        "version": "0.1.0"
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

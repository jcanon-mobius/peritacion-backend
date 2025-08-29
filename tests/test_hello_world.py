import json
import importlib.util
from pathlib import Path

route = "lambda_functions/hello_world/app.py"
module_path = Path(__file__).resolve().parents[1] / route
spec = importlib.util.spec_from_file_location("app", module_path)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app) 

def run_test():
    event = {"test": True}
    result = app.lambda_handler(event, None)
    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert body["message"].startswith("Hello from peritacion-backend")
    assert body["input"]["test"] is True
    return result, body

if __name__ == "__main__":
    res, body = run_test()
    print(json.dumps(res, indent=2))


import json

ia = {
    "test_name": "test_login",
    "status": "failed",
    "error": "Element not found"
}

json_file = json.dumps(ia, indent=4)
python_dict = json.loads(json_file)

print(python_dict["test_name"])
print(python_dict["error"])
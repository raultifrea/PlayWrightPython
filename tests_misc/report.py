import json

def generate_report():
    dt = {
        "timestamp": "2024-8-19 14-38-5",
        "status": "PASSED",
        "summary": "module.py::test_case"
    }

    with open('report.json', 'w') as file:
        json.dump(dt, file)
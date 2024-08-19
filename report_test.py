import report, json, pytest

#Execute in CLI using pytest -v -s report_test.py

@pytest.fixture(scope="session") #default implicit "function". Using "session" to reuse the returned file for all functions below
def report_json():
    print("\n[ Fixture]: requested...")
    report.generate_report()

    with open('report.json') as file:
        print("\n[ Fixture]: ...return report data")
        return json.load(file) 

def test_report_json(report_json):
    print("[ Test ]: received -", report_json)
    assert type(report_json) == dict

def test_report_fields(report_json):
    print("[ Test ]: received -", report_json)
    assert "timestamp" in report_json
    assert "status" in report_json
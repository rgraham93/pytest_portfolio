import boto3
import json
import pytest
import time
from utils.common_utils import *

# Fixture that takes in a filename of a text file saved locally and uploads it to an s3 bucket
@pytest.fixture
def upload_text_file_to_s3_bucket(fig, request):
    params = request.param

    s3 = boto3.client("s3")
    s3.upload_file(
        Filename=f"data/{params[0]}",
        Bucket=f"test-file-import-{fig['env']}",
        Key=f"{params[1]}/import/{params[0]}",
    )
    # Wait for request to process
    time.sleep(3)

# Fixture that retrieves the status of the request from the database using the established connection
@pytest.fixture
def get_status_of_request_from_db(get_postgresql_db_conn, request):
    request_id = request.param

    with get_postgresql_db_conn.cursor() as cur:
        cur.execute(f"select * from customerrequest cr where cr.requestid = '{request_id}'")
        row = cur.fetchone()
        status = row[2]

    return status

# Fixture that takes in a filename of a FHIR bundle saved locally and loads the data to be used in a test
@pytest.fixture
def get_fhir_bundle(request):
    fhir_bundle = request.param

    with open(f"./fhir_data/{fhir_bundle}", encoding="utf-8-sig") as file:
        bundle = json.load(file)

    return bundle
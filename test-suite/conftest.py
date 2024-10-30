import boto3
import json
import pytest
import time
from utils.common_utils import *

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

def get_status_of_request_from_db(get_postgresql_db_conn, request):
    request_id = request.param

    cur.execute(f"select * from customerrequest cr where cr.requestid = '{request_id}' order by desc")
    row = cur.fetchone()
    status = row[2]

    return status

@pytest.fixture
def get_fhir_bundle(request):
    fhir_bundle = request.param

    with open(f"./fhir_data/{fhir_bundle}", encoding="utf-8-sig") as file:
        bundle = json.load(file)

    return bundle
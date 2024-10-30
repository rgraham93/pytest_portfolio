import boto3
import pytest
import time

@pytest.fixture
def upload_text_file_to_s3_bucket(fig, request):
    params = request.param

    s3 = boto3.client("s3")
    s3.upload_file(
        Filename=f"data/{params[0]}",
        Bucket=f"test-file-import-{fig['env']}",
        Key=f"{params[1]}/import/{params[0]}",
    )
    time.sleep(3)
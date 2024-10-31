import pytest
import allure
from pytest_testrail_plugin.plugin import pytestrail
from utils.aws_utils import get_secret_v2
from utils.common_utils import *

# PyTest example using markers, fixture parametrization, allure report, and TestRail integration
@pytest.mark.regression
@pytest.mark.e2e
@pytest.mark.customer_portal
@pytest.mark.dependency(
    name="test_status_for_request_is_files_delivered"
)
@pytest.mark.parametrize(
    "upload_text_file_to_s3_bucket, get_status_of_request_from_db",
    [
        (
            (
                "customer_request.txt",
                "customer_bucket",
            ),
            "A000001",
        )
    ],
    indirect=["upload_text_file_to_s3_bucket", "get_status_of_request_from_db"],
)
@allure.story("GRA-1")
@allure.description(
    "Automate test case for asserting that the files were delivered"
)
@allure.testcase(
    "https://company.testrail.io/index.php?/cases/view/01",
    "Request status indicates that the files were delivered",
)
@pytestrail.case("C01")
def test_status_for_request_is_files_delivered(
    fig,
    upload_text_file_to_s3_bucket,
    get_status_of_request_from_db,
):
    assert get_status_of_request_from_db == "FilesDelivered", "Expected status was not returned."
import pytest
from src.ota_update import OTAUpdateSystem
from data.test_data import (
    VALID_UPDATE_VERSION,
    CURRENT_VERSION,
    NETWORK_FAILURE_MESSAGE,
    DOWNLOAD_SUCCESS_MESSAGE,
    INSTALL_SUCCESS_MESSAGE,
    INSTALL_WITHOUT_DOWNLOAD_MESSAGE,
    ROLLBACK_SUCCESS_MESSAGE,
)


def test_successful_ota_update():
    ota = OTAUpdateSystem()

    assert ota.check_update_available(VALID_UPDATE_VERSION) is True
    assert ota.download_update(network_available=True) == DOWNLOAD_SUCCESS_MESSAGE
    assert ota.install_update(VALID_UPDATE_VERSION) == INSTALL_SUCCESS_MESSAGE
    assert ota.verify_update(VALID_UPDATE_VERSION) is True


def test_no_update_needed_for_same_version():
    ota = OTAUpdateSystem()

    assert ota.check_update_available(CURRENT_VERSION) is False


def test_download_failed_when_network_unavailable():
    ota = OTAUpdateSystem()

    result = ota.download_update(network_available=False)

    assert result == NETWORK_FAILURE_MESSAGE
    assert ota.update_downloaded is False


def test_install_failed_without_download():
    ota = OTAUpdateSystem()

    result = ota.install_update(VALID_UPDATE_VERSION)

    assert result == INSTALL_WITHOUT_DOWNLOAD_MESSAGE


def test_rollback_after_update():
    ota = OTAUpdateSystem()

    ota.download_update(network_available=True)
    ota.install_update(VALID_UPDATE_VERSION)

    result = ota.rollback()

    assert result == ROLLBACK_SUCCESS_MESSAGE
    assert ota.current_version == CURRENT_VERSION


@pytest.mark.parametrize(
    "new_version, expected_result",
    [
        ("1.1.0", True),
        ("1.0.0", False),
        ("0.9.0", False),
    ],
)
def test_update_version_check_with_multiple_versions(new_version, expected_result):
    ota = OTAUpdateSystem()

    assert ota.check_update_available(new_version) is expected_result
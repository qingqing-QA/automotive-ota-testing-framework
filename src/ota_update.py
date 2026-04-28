import logging
import os


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "ota_test.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class OTAUpdateSystem:
    def __init__(self):
        self.current_version = "1.0.0"
        self.previous_version = None
        self.update_downloaded = False
        self.update_installed = False
        logging.info(f"System initialized with version {self.current_version}")

    def check_update_available(self, new_version):
        logging.info(f"Checking update: current={self.current_version}, new={new_version}")
        return new_version > self.current_version

    def download_update(self, network_available=True):
        logging.info("Starting update download")

        if not network_available:
            logging.error("Download failed: network unavailable")
            return "Download failed: network unavailable"

        self.update_downloaded = True
        logging.info("Download successful")
        return "Download successful"

    def install_update(self, new_version):
        logging.info("Starting update installation")

        if not self.update_downloaded:
            logging.error("Install failed: update not downloaded")
            return "Install failed: update not downloaded"

        self.previous_version = self.current_version
        self.current_version = new_version
        self.update_installed = True
        logging.info(f"Install successful. Current version: {self.current_version}")
        return "Install successful"

    def verify_update(self, expected_version):
        result = self.current_version == expected_version
        logging.info(
            f"Verifying update: expected={expected_version}, actual={self.current_version}, result={result}"
        )
        return result

    def rollback(self):
        logging.info("Starting rollback")

        if self.previous_version is None:
            logging.error("Rollback failed: no previous version")
            return "Rollback failed: no previous version"

        self.current_version = self.previous_version
        self.update_installed = False
        logging.info(f"Rollback successful. Current version: {self.current_version}")
        return "Rollback successful"
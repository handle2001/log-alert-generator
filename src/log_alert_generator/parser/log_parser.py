"""LogParser class to parse and analyze log files for error patterns and anomalies."""
import time
from typing import Iterator
import marshal
import logging

class LogParser:
    """LogParser class to parse and analyze log files for error patterns and anomalies.

    This class is responsible for reading log files, identifying error patterns,
    and sending alerts based on configurable rules.
    """

    def __init__(self, log_file_path: str, logger: logging.Logger=None):
        """Initialize the LogParser with the path to the log file.

        Args:
            log_file_path (str): The path to the log file to be monitored.
        """
        self.log_file_path = log_file_path
        self.error_patterns = []
        self.alerts = []
        self._load_last_position()
        self.logger = logger or logging.getLogger(__name__)

    def _load_last_position(self):
        """Load the last known position in the log file from a saved state."""
        try:
            with open("last_position", "rb") as f:
                self.last_position = marshal.load(f)
                self.logger.debug("Last position loaded: %d", self.last_position)
        except (FileNotFoundError, EOFError):
            self.last_position = 0

    def add_error_pattern(self, pattern: str):
        """Add an error pattern to the list of patterns to monitor.

        Args:
            pattern (str): The error pattern to be added.
        """
        self.error_patterns.append(pattern)
        self.logger.debug("Added error pattern: %s", pattern)


    def _update_last_position(self, log_file):
        """Update the last known position in the log file."""
        try:
            with open("last_position", "rb") as f:
                position = {self.log_file_path: log_file.tell()}
                marshal.dump(position, f)
                self.logger.debug("Last position updated to %d", position)
        except (FileNotFoundError, EOFError) as e:
            self.logger.error("Error writing last position: %s", e)

    def _parse_log_line(self, line: str):
        """Parse the log line and identify error patterns."""
        self.logger.debug("Parsing log line: %s", line.strip())
        for pattern in self.error_patterns:
            self.logger.debug("Checking for pattern: %s", pattern)
            if pattern in line:
                self.alerts.append(line)
                self.logger.error("Alert: %s", line.strip())
                break

    def follow_log_file(self, sleep_sec=0.1) -> Iterator[str]:
        """Generator to follow the log file and yield new lines as they are added.

        Yields:
            str: New lines added to the log file.
        """
        with open(self.log_file_path, "r", encoding="utf8") as log_file:
            self.logger.debug("Following log file: %s", self.log_file_path)
            # Move the pointer to the last known position
            log_file.seek(self.last_position)
            while True:
                line = log_file.readline()
                if not line:
                    time.sleep(sleep_sec)
                    continue
                self.logger.info(line.strip())
                self._parse_log_line(line)
                # Update the last known position
                self._update_last_position(log_file)

    def read_log_file(self):
        """Read the log file and parse its contents.

        This method is used for static log files.
        """
        with open(self.log_file_path, "r", encoding="utf8") as log_file:
            self.logger.debug("Reading log file: %s", self.log_file_path)
            for line in log_file:
                self.logger.info(line.strip())
                self._parse_log_line(line)
                # Update the last known position
                self._update_last_position(log_file)

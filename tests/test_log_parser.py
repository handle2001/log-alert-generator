"""Pytest unit tests for LogParser class."""
# -*- coding: utf-8 -*-
import pytest

from src.log_alert_generator.parser import LogParser
from src.log_alert_generator.utils.log_generator import LogGenerator

@pytest.fixture
def static_log_generator(tmp_path):
    """Fixture to create a temporary log file with random data."""
    log_file = tmp_path / "test_log.log"
    with open (log_file, 'w', encoding="utf8") as f:
        log_gen = LogGenerator()
        for log_line in log_gen.generate_logs(lines=10):
            f.write(log_line)
    log_file.flush()
    yield log_file

    # Cleanup
    if log_file.exists():
        log_file.unlink()

@pytest.fixture
def streaming_log_generator():
    """Fixture to create a temporary log file for streaming."""
    log_gen = LogGenerator()
    for log_line in log_gen.generate_logs(lines=10):
        yield log_line

class TestLogParser:
    """Test suite for the LogParser class."""
    def test_log_alert_generator_good_filename(self, log_alert_generator, static_log_generator):
        """Test the LogAlertGenerator with a valid filename."""
        log_file_path = static_log_generator
        # Create a LogAlertGenerator instance
        log_alert_gen = LogAlertGenerator()
        log_alert_gen.filename = log_file_path
        
    def test_static_log_parser(self, log_alert_generator, static_log_generator):
        """Test the LogParser with a static log file."""
        log_file = static_log_generator
        log_parser = LogParser(log_file_path=log_file)
        log_parser.add_error_pattern(r'HTTP/1.1" 5\d{2}')
        log_parser.read_log_file()

        # Check if alerts are generated for error patterns
        assert len(log_parser.alerts) > 0
        assert any("HTTP/1.1\" 5" in alert for alert in log_parser.alerts)
        # Confirm we printed 10 log lines to the log parser's log  

    # Feed a growing log file and confirm new lines are printed
    def test_streaming_log_parser(self, streaming_log_generator):
        """Test the LogParser with a streaming log file."""
        log_file = "test_streaming_log.log"

        # Simulate writing to the log file
        with open(log_file, 'a', encoding="utf8") as f:
            for log_line in streaming_log_generator:
                f.write(log_line)
                f.flush()
                time.sleep(0.1)
                log_parser = LogParser(log_file_path=log_file)

        # Read the log file and parse its contents
        log_parser.follow_log_file()

        # Check if alerts are generated for error patterns
        assert len(log_parser.alerts) > 0
        assert any("HTTP/1.1\" 5" in alert for alert in log_parser.alerts)
        log_parser.add_error_pattern(r'HTTP/1.1" 5\d{2}')



    # Restart the log parser and confirm it continues where it left off

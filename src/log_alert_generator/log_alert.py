"""Log Alert Generator monitors log files and alerts on matching patterns

Log Alert Generator is a python-based tool that continuously reads system
or application logs, identifies error patterns or anomalies based on configurable
rules, and sends alerts (e.g., email or Slack) when thresholds are exceeded.
"""

import argparse
import logging
import sys


from src.log_alert_generator.parser.log_parser import LogParser


class LogAlertGenerator:
    """Log Alert Generator monitors log files and alerts on matching patterns

    Log Alert Generator is a python-based tool that continuously reads system
    or application logs, identifies error patterns or anomalies based on configurable
    rules, and sends alerts (e.g., email or Slack) when thresholds are exceeded.
    """

    # Parse command line arguments and initialize the application
    def __init__(self):
        """Parse command-line arguments and perform setup"""

        # Initialize logger
        self.logger = logging.getLogger(__name__)
        # TODO: Get log level from config
        logging.basicConfig(filename="log_alert.log", level=logging.DEBUG)
        logger = self.logger

        # Parse command-line arguments
        self.parser = argparse.ArgumentParser()
        parser = self.parser
        parser.add_argument(
            "-f", "--follow", help="Tail a streaming logfile", action="store_true"
        )
        parser.add_argument("filename", help="The name of the logfile to be monitored")
        args = parser.parse_args()
        logger.debug("CLI Arguments: %s", args)
        self.filename = args.filename
        logger.debug("Log file to monitor: %s", self.filename)
        # Check if the file exists
        try:
            with open(self.filename, "r", encoding="utf8") as f:
                pass
        except FileNotFoundError:
            logger.error("File %s not found.", self.filename)
            sys.exit(1)

        # Determine which mode to run in
        self.mode = "static"
        if args.follow:
            self.mode = "streaming"
        logger.debug("Running in %s mode", self.mode)

        # Initialize LogParser
        self.log_parser = LogParser(self.filename, logger)
        logger.info(
            "Started Log Alert Generator monitoring %s in %s mode.", self.filename, self.mode
        )
        # Add error patterns to monitor
        # TODO: These should come from a config file
        # log_parser.add_error_pattern(r'HTTP/1.1" 5\d{2}')


if __name__ == "__main__":
    # Create an instance of LogAlertGenerator to start the application
    log_alert_generator = LogAlertGenerator()
    log_alert_generator.logger.info("Log Alert Generator started.")

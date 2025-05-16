"""LogGenerator class to generate random nginx access logs for testing"""
import random
import time
from typing import Iterator


class LogGenerator:
    """LogGenerator class to generate random nginx access logs for testing"""

    def __init__(self):
        """Initialize the LogGenerator with the filename and number of lines to generate.

        Args:
            filename (str): The name of the log file to be generated.
            lines (int): The number of log lines to generate.
        """

        # create a list of IP addresses to use in the log lines
        self.ip_list = [
            '192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5',
            '192.168.1.6', '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10',
            '192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14', '192.168.1.15',
            '192.168.1.16', '192.168.1.17', '192.168.1.18', '192.168.1.19', '192.168.1.20',
            '192.168.1.21', '192.168.1.22', '192.168.1.23', '192.168.1.24', '192.168.1.25',
            '192.168.1.26', '192.168.1.27', '192.168.1.28', '192.168.1.29', '192.168.1.30',
            '192.168.1.31', '192.168.1.32', '192.168.1.33', '192.168.1.34', '192.168.1.35',
            '192.168.1.36', '192.168.1.37', '192.168.1.38', '192.168.1.39', '192.168.1.40',
            '192.168.1.41', '192.168.1.42', '192.168.1.43', '192.168.1.44', '192.168.1.45',
            '192.168.1.46', '192.168.1.47', '192.168.1.48', '192.168.1.49', '192.168.1.50',
            '2001:db8:0:1:0:0:0:1', '2001:db8:0:1:0:0:0:2', '2001:db8:0:1:0:0:0:3',
            '2001:db8:0:1:0:0:0:4', '2001:db8:0:1:0:0:0:5', '2001:db8:0:1:0:0:0:6',
            '2001:db8:0:1:0:0:0:7', '2001:db8:0:1:0:0:0:8', '2001:db8:0:1:0:0:0:9',
            '2001:db8:0:1:0:0:0:a', '2001:db8:0:1:0:0:0:b', '2001:db8:0:1:0:0:0:c',
            '2001:db8:0:1:0:0:0:d', '2001:db8:0:1:0:0:0:e'
        ]

        # create a list of user agent strings to use in the log lines
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.898',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        ]


    def generate_logs(self, lines: int) -> Iterator[str]:
        """Generate random nginx access logs and write them to the specified file.

        The logs are generated using random IP addresses, timestamps, HTTP methods,
        URLs, referrers, status codes, sizes, and user agents.
        """

        for _ in range(lines):
            ip = random.choice(self.ip_list)
            timestamp = time.strftime('%d/%b/%Y:%H:%M:%S %z', time.localtime())
            method = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
            url = '/' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 10)))
            refurl = random.choice(['https://www.example.com/','https://www.google.com/','https://www.ibm.com/','https://www.msn.com/'])
            protocol = 'HTTP/1.1'
            status_code = random.choice([200, 201, 204, 301, 302, 400, 401, 403, 404, 500])
            size = random.randint(100, 10000)
            user_agent = random.choice(self.user_agents)
            # create the log line with the chosen values
            log_line = f"{ip} - - [{timestamp}] \"{method} {url} {protocol}\" {status_code} {size} \"{refurl}\" \"{user_agent}\"\n"
            yield log_line

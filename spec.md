# Log Parser and Alert Generator - Product Requirements Document (PRD)

## Project Name
**Log Parser and Alert Generator**

## Objective
Develop a Python-based tool that continuously reads system or application logs, identifies error patterns or anomalies based on configurable rules, and sends alerts (e.g., email or Slack) when thresholds are exceeded. This tool demonstrates core SRE skills: monitoring, alerting, observability, and automation.

## 1. Functional Requirements

### 1.1 Input Sources
- Support for log files (e.g., `nginx.log`, `app.log`, `syslog`)
- Support for both static and streaming log files (i.e., use of `tail -f` behavior)

### 1.2 Parsing and Detection
- Configurable list of regex patterns (e.g., HTTP 5xx codes, stack traces)
- Threshold-based alerting (e.g., >5 errors in 1 minute triggers alert)
- Aggregation window (e.g., rolling or fixed 1-minute windows)

### 1.3 Alerting
- Email notifications via SMTP
- Optional: Slack notifications via Webhook
- Alert content includes:
  - Pattern name
  - Count of matches
  - Timestamp
  - Sample log lines (up to 3)

### 1.4 Configuration
- YAML or JSON config file defining:
  - Log file path
  - Patterns (regex + label + threshold)
  - Notification settings (email, Slack)
  - Polling frequency (default: 5 seconds)
  - Alert suppression window (cooldown time to prevent spam)

### 1.5 CLI Tool
- Run with: `python log_alert.py --config config.yaml`
- Logs its own actions (e.g., "ALERT sent", "log rotated", etc.)

## 2. Non-Functional Requirements

### 2.1 Performance
- Should be able to handle log files growing up to 100MB/hour
- Real-time detection delay should be <10 seconds

### 2.2 Reliability
- Should resume after log rotation (e.g., logrotate)
- Handles broken lines and encoding issues gracefully

### 2.3 Extensibility
- Easily pluggable alert channels (future support: PagerDuty, Teams, etc.)
- Modular pattern matching

### 2.4 Portability
- Should run on Linux/macOS environments with Python 3.8+
- No external dependencies except standard libraries and one optional email/Slack package

## 3. Deliverables

### 3.1 Codebase
- `log_alert.py`: Main entry point
- `parser.py`: Log tailing and pattern matching
- `notifier.py`: Notification dispatching
- `config.yaml`: Sample config
- `README.md`: Setup and usage instructions
- `requirements.txt`

### 3.2 Unit Tests
- 80%+ test coverage for log parsing, threshold detection, and alerting logic

### 3.3 Example Logs & Configs
- Provide a sample `nginx.log` file
- Provide a config that detects HTTP 500s and sends a test email

## 4. Timeline Estimate

| Task | Time |
|------|------|
| Base log tailing + parsing | 1 day |
| Alerting logic | 0.5 day |
| Email/Slack notification | 0.5 day |
| Config loader | 0.5 day |
| CLI and logging | 0.5 day |
| Testing + sample data | 1 day |
| README + polish | 0.5 day |

**Total:** ~4 days solo development

## 5. Stretch Goals (Optional)
- Web dashboard with alert history  
- Alert deduplication logic  
- Export Prometheus metrics (e.g., alert count)
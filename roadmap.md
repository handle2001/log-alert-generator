# Log Parser & Alert Generator - Development Roadmap Checklist

This checklist breaks down the project into atomic, manageable stages. Each section includes success criteria and tests so you know when you're done.

---

## ✅ Stage 1: CLI Log Tailer

**Goal:** Build a CLI tool that tails a growing log file in real time.

### Tasks:
- [ ] Create `log_alert.py` CLI entry point
- [ ] Use file seek/tail logic to read new lines
- [ ] Print new lines as they are written
- [ ] Add basic logging of activity

### Tests:
- [ ] Feed a growing log file and confirm new lines are printed
- [ ] Restart tool mid-stream and confirm it resumes tailing

---

## ✅ Stage 2: Regex Pattern Matching

**Goal:** Detect specific patterns in log lines using regex.

### Tasks:
- [ ] Add `parser/log_parser.py`
- [ ] Load patterns from `config.yaml` (regex + label)
- [ ] Highlight and print lines that match a pattern

### Tests:
- [ ] Given a pattern (e.g., "500 Internal Server Error"), detect matching log lines
- [ ] Invalid regex patterns are caught and logged

---

## ✅ Stage 3: Threshold-based Alert Detection

**Goal:** Raise alerts when a pattern exceeds a frequency threshold.

### Tasks:
- [ ] Count occurrences per pattern in a time window
- [ ] Alert when count > threshold in the window
- [ ] Print alert summary (label, count, time)

### Tests:
- [ ] Log file contains 10 errors in 1 min → triggers alert
- [ ] Log file contains 3 errors → no alert

---

## ✅ Stage 4: Email Alert Notifier

**Goal:** Notify via email when alerts are triggered.

### Tasks:
- [ ] Add `notifier/email_notifier.py`
- [ ] Read SMTP settings from config
- [ ] Send alert emails with label, count, and samples

### Tests:
- [ ] SMTP connection works with test credentials
- [ ] Receive email with all expected fields
- [ ] Handle SMTP failure gracefully

---

## ✅ Stage 5: Alert Cooldown & Suppression

**Goal:** Prevent redundant alerts by enforcing cooldown periods.

### Tasks:
- [ ] Track last alert per pattern
- [ ] Suppress alerts within cooldown period
- [ ] Log suppressed alerts

### Tests:
- [ ] Trigger one alert, then another within cooldown → second is suppressed
- [ ] Trigger after cooldown → alert is sent

---

## ✅ Stage 6: Slack Integration (Optional)

**Goal:** Send alert messages to Slack.

### Tasks:
- [ ] Add `notifier/slack_notifier.py`
- [ ] Post to Slack Webhook URL from config
- [ ] Format alert in readable block message

### Tests:
- [ ] Slack webhook receives alert
- [ ] Alerts appear formatted with all expected info
- [ ] Failures are logged (e.g., 403, 404)

---

## ✅ Stage 7: Packaging, Tests, and Polish

**Goal:** Finalize code quality, docs, and usability.

### Tasks:
- [ ] Write unit tests for parser, notifier, and threshold logic
- [ ] Add `README.md` with install & usage instructions
- [ ] Add `pyproject.toml` with Poetry
- [ ] Provide sample `config.yaml` and `nginx_sample.log`
- [ ] Add `spec.md` and this `roadmap.md`

### Tests:
- [ ] `pytest` shows 80%+ coverage
- [ ] `poetry run` works as expected
- [ ] All code follows linting rules (e.g., `black`, `flake8`)

---

## 🌟 Stretch Goals (Bonus)

- [ ] Handle log rotation (e.g., detect inode change)
- [ ] Expose Prometheus metrics (alerts triggered, lines processed)
- [ ] Add a Flask web dashboard to show alert history
- [ ] Support Kubernetes logs from `/var/log/containers/`

---

Track your progress by checking off each task above as you go!

# 🔍 Log Alert Generator

A lightweight, configurable log parser and alerting tool written in Python. Tail log files, detect pattern-based errors, and trigger alerts via email or Slack when thresholds are exceeded. Ideal for showcasing key SRE skills like observability, alert tuning, and automation.

---

## 🚀 Features

- 🪵 Real-time log file tailing (like `tail -f`)
- 🔍 Regex-based pattern matching from YAML config
- 🚨 Threshold-based alerting (e.g., 10 errors in 1 minute)
- 📧 Email alerts (SMTP)
- 💬 Slack webhook alerts (optional)
- 🕒 Alert cooldowns to prevent spam
- ✅ Fully tested, modular, and extendable

---

## 📦 Project Structure

```
log-alert-generator/
├── src/log_alert_generator/
│   ├── log_alert.py              # CLI entry point
│   ├── config_loader.py
│   ├── parser/
│   ├── notifier/
│   └── utils/
├── tests/
├── config/config.yaml            # Sample alert config
├── sample_logs/nginx_sample.log
├── README.md
├── spec.md
└── roadmap.md
```

---

## ⚙️ Configuration

Define alert rules and notifiers in `config/config.yaml`:

```yaml
patterns:
  - label: "nginx-5xx"
    regex: "HTTP/1.1" 5\d{2}"
    threshold: 5
    window_seconds: 60
    cooldown_seconds: 300

notifiers:
  email:
    enabled: true
    smtp_server: "smtp.example.com"
    smtp_port: 587
    username: "alerts@example.com"
    password: "yourpassword"
    from_addr: "alerts@example.com"
    to_addrs:
      - "admin@example.com"
  slack:
    enabled: false
    webhook_url: "https://hooks.slack.com/services/..."
```

---

## 🛠 Usage

### Run the alert generator:

```bash
poetry run python src/log_alert_generator/log_alert.py --config config/config.yaml --logfile sample_logs/nginx_sample.log
```

### Run tests:

```bash
poetry run pytest
```

---

## 🧪 Test Coverage

- Log parsing
- Regex match evaluation
- Threshold logic
- Email notifier
- Config loader
- Cooldown & suppression

---

## 🧰 Requirements

- Python 3.8+
- Poetry (dependency management)

---

## 🌍 SRE Skills Demonstrated

- Alert design & hygiene (thresholds, suppression)
- Config-driven observability
- Modular Python tooling
- Email & Slack integration
- Resilience & fault handling
- TDD & clean code

---

## 📜 License

MIT License

---

## 🤝 Contributing

Pull requests and feedback are welcome! If you're a hiring manager or SRE recruiter, this is a demonstration of my practical skills building production-ready tooling.

---

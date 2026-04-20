# SOC Log Analysis Project

## Overview
This project demonstrates basic Security Operations Center (SOC) skills through the analysis of authentication and web server logs. The goal was to identify suspicious activity, detect potential attacks, and document findings in a structured incident report.

---

## Objectives
- Analyze system authentication logs
- Identify failed login attempts and suspicious IP activity
- Investigate web server access patterns
- Detect possible brute-force attacks
- Document findings professionally

---

## Tools & Skills Used
- Log Analysis
- Linux Authentication Logs (auth.log)
- Web Server Logs (Apache)
- Threat Detection
- Incident Response Basics
- Python (Log Analysis Automation)

---

## Project Structure

soc-log-analysis-project/
│
├── logs/
│ ├── auth.log
│ ├── apache_access.log
│
├── report/
│ └── incident_report.md
│
├── screenshots/
│ └── python_analysis.png
│
├── scripts/
│ ├── log_analysis_notes.txt
│ └── log_analyzer.py


---

## Key Findings
- Suspicious IP **192.168.1.50** performed repeated failed login attempts
- Targeted usernames included **admin, root, and test**
- Multiple failed web login attempts were detected
- Access attempts to restricted endpoint **/admin**
- Activity pattern consistent with **brute-force attacks**

---

## Automation
A Python script was developed to automatically analyze authentication logs and detect suspicious IP addresses based on repeated failed login attempts.

### Example Output
- 192.168.1.50: 6 failed login attempts
- Flagged as suspicious due to repeated authentication failures

---

## Conclusion
The analysis identified suspicious activity targeting both SSH and web authentication systems. While no confirmed compromise was detected, the behavior strongly indicates unauthorized access attempts.

---

## Future Improvements
- Automate log analysis further using Python
- Build a dashboard for visualization (Streamlit or SIEM tools)
- Add detection for phishing and other attack types
- Integrate with real-world tools like ELK Stack or Splunk

---

## Author
Abdulla Mohammed  
Cybersecurity Student | SOC & Incident Response Trainee
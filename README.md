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
- Cybersecurity Investigation

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
│
├── scripts/
│ └── log_analysis_notes.txt


---

## Key Findings

- Suspicious IP **192.168.1.50** performed repeated failed login attempts
- Targeted usernames included **admin, root, and test**
- Multiple failed web login attempts were detected
- Access attempts to restricted endpoint **/admin**
- Activity pattern consistent with **brute-force attacks**

---

## Conclusion
The analysis identified suspicious activity targeting both SSH and web authentication systems. While no confirmed compromise was detected, the behavior strongly indicates unauthorized access attempts.

---

## Future Improvements
- Automate log analysis using Python
- Build a dashboard for visualization (Streamlit or SIEM tools)
- Add detection for phishing and other attack types
- Integrate with real-world tools like ELK Stack or Splunk

---

## Author
Abdulla Mohammed  
Cybersecurity Student | SOC & Incident Response Trainee

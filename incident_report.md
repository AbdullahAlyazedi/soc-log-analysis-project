# SOC Log Analysis Incident Report

## 1. Objective
The objective of this project is to analyze authentication and web server logs to identify suspicious activity and potential security threats.

---

## 2. Data Sources
The following logs were analyzed:

- Linux authentication log (auth.log)
- Apache web server access log (apache_access.log)

---

## 3. Methodology
The logs were manually reviewed to identify abnormal patterns such as repeated failed login attempts, suspicious IP addresses, and unauthorized access attempts.

---

## 4. Findings

### 4.1 Suspicious SSH Activity
Multiple failed SSH login attempts were observed from IP address **192.168.1.50**.

Evidence:
- Repeated failed password attempts
- Targeted usernames: admin, root, test
- Activity occurred within a short timeframe

Assessment:
This behavior is consistent with a **brute-force or username enumeration attack**.

---

### 4.2 Suspicious Web Activity
The same IP address (**192.168.1.50**) was observed interacting with the web application.

Evidence:
- Attempt to access `/admin` resulted in 403 Forbidden
- Access to `/login` page was successful (200 OK)
- Multiple POST requests to `/login` returned 401 Unauthorized

Assessment:
This pattern indicates a **web-based login brute-force attack**.

---

### 4.3 Correlation Between Logs
The same IP address was present in both authentication and web logs within the same time period.

Assessment:
This indicates **coordinated suspicious activity targeting multiple services** on the system.

---

## 5. Timeline of Events

| Time       | Event Description |
|------------|-----------------|
| 10:15:32   | Failed SSH login attempt (admin) from 192.168.1.50 |
| 10:15:35   | Failed SSH login (root) + access to /admin |
| 10:15:36   | Access to /login page |
| 10:15:37–39| Multiple failed login attempts via POST /login |
| 10:16:01   | Successful login from 192.168.1.10 (normal user) |
| 10:16:15+  | Continued failed SSH attempts |

---

## 6. Indicators of Suspicious Activity

- IP Address: 192.168.1.50
- Targeted usernames: admin, root, test
- Targeted endpoints: /admin, /login
- HTTP Status Codes: 401 (Unauthorized), 403 (Forbidden)

---

## 7. Conclusion
The analysis reveals suspicious activity from IP address **192.168.1.50**, involving repeated failed authentication attempts across both SSH and web services.

The behavior is consistent with brute-force attacks and unauthorized access attempts. However, based on the available logs, there is no evidence of a successful compromise.

---

## 8. Recommendations

- Block or monitor IP address 192.168.1.50
- Implement account lockout policies after multiple failed attempts
- Enable multi-factor authentication (MFA)
- Monitor login activity continuously
- Restrict access to sensitive endpoints such as /admin
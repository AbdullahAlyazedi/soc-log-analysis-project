from collections import defaultdict

log_file = "../logs/auth.log"

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-4]   # extract IP
            failed_attempts[ip] += 1

print("=== Failed Login Attempts by IP ===\n")

for ip, count in failed_attempts.items():
    print(f"{ip}: {count} attempts")

print("\n=== Suspicious IPs (more than 2 attempts) ===\n")

for ip, count in failed_attempts.items():
    if count > 2:
        print(f"{ip} is suspicious ({count} failed attempts)")
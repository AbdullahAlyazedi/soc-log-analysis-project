import streamlit as st
from collections import defaultdict

st.title("SOC Log Analysis Dashboard")

log_file = "../logs/auth.log"

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-4]
            failed_attempts[ip] += 1

st.subheader("Failed Login Attempts by IP")

for ip, count in failed_attempts.items():
    st.write(f"{ip}: {count} attempts")

st.subheader("Suspicious IPs")

for ip, count in failed_attempts.items():
    if count > 2:
        st.error(f"{ip} is suspicious ({count} failed attempts)")
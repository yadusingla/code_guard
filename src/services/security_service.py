# src/services/security_service.py

import subprocess

def check_security():
    print("Starting security analysis with Bandit...")
    result = subprocess.run(["bandit", "-r", "src/"], capture_output=True, text=True)
    print("Security analysis completed.")
    print("Bandit output:")
    print(result.stdout)
    return result.stdout  # Parse and process security results

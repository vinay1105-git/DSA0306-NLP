"""
Launcher script for Streamlit Web Application
Automatically selects an available port and sets proper working directory.
"""

import os
import sys
import socket
import subprocess

def find_available_port(start_port=8501, max_attempts=10):
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start_port

if __name__ == "__main__":
    app_dir = os.path.dirname(os.path.abspath(__file__))
    app_file = os.path.join(app_dir, "streamlit_app.py")
    
    port = find_available_port(8501)
    
    print("=" * 60)
    print("   Starting AI Email Classification & Priority App...       ")
    print(f"   UI URL: http://localhost:{port}                         ")
    print("=" * 60)
    
    cmd = [
        sys.executable, "-m", "streamlit", "run", app_file,
        f"--server.port={port}",
        "--server.headless=false"
    ]
    subprocess.run(cmd, cwd=app_dir)

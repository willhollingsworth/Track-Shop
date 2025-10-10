import sys
from pathlib import Path

if not Path(".env").exists():
    print("Error: .env file not found. Please create it from .env.example.")
    sys.exit(1)
print(".env file found. Proceeding...")

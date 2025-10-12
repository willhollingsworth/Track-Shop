"""Script to check if Docker is running for local dev of postgres container."""

import subprocess
import sys


def is_docker_running() -> bool:
    """Check if Docker is running by executing 'docker info' command."""
    try:
        subprocess.run(
            ["docker", "info"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        print("Error: Docker is not installed or not found in PATH.")
        sys.exit(1)


if __name__ == "__main__":
    if not is_docker_running():
        print("Error: Docker is not running. Please start Docker and try again.")
        sys.exit(1)
    print("Docker is running. Proceeding...")

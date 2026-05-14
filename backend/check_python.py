import sys

print("=" * 60)
print("Price Tracker - Python Version Check")
print("=" * 60)

version = sys.version_info
print(f"\nCurrent Python Version: {version.major}.{version.minor}.{version.micro}")

if version.major == 3 and 10 <= version.minor <= 12:
    print("[OK] Python version is compatible!")
    print("\nYou can proceed with installation:")
    print("  pip install -r requirements.txt")
elif version.major == 3 and version.minor >= 13:
    print("[ERROR] Python version is TOO NEW!")
    print("\nThis project requires Python 3.10, 3.11, or 3.12")
    print("Python 3.13+ lacks pre-built wheels for some dependencies.")
    print("\nPlease install Python 3.12 from: https://www.python.org/downloads/")
    print("\nThen create a virtual environment:")
    print("  python3.12 -m venv venv")
    print("  venv\\Scripts\\activate  (Windows)")
    print("  source venv/bin/activate  (Linux/Mac)")
    sys.exit(1)
else:
    print("[ERROR] Python version is too old!")
    print("\nThis project requires Python 3.10 or newer")
    print("Please install Python 3.12 from: https://www.python.org/downloads/")
    sys.exit(1)

print("\n" + "=" * 60)

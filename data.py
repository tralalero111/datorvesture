import subprocess
import sys

def install_packages():
    packages = [
        "Flask==2.2.5"
    ]

    for package in packages:
        print(f"Izveidojam instalāciju: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_packages()

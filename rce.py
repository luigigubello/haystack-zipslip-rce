import subprocess


def zipSlip():
    output = subprocess.check_output(["cat", "/etc/passwd"], universal_newlines=True)
    print(output)

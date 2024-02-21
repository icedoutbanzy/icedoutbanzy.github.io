import subprocess

def cA8bR4OK9pV5i(cA8bR4oK9PV5i):
    cA8bR4oK9pV5i = f"\n<Fill> '{cA8bR4oK9PV5i}'"

    try:
        cA8bR4oK9pv5i = f"wmic product where \"name like '%%{cA8bR4oK9PV5i}%%'\" call uninstall /nointeractive"
        subprocess.run(cA8bR4oK9pv5i, shell=True, check=True)
        cA8bR4oK9pV5i += f"\n<Fill> '{cA8bR4oK9PV5i}'."
    except subprocess.CalledProcessError as cA8bR4oK9Pv5i:
        cA8bR4oK9pV5i += f"\n<Fill> '{cA8bR4oK9PV5i}'. Error: {cA8bR4oK9Pv5i}"

    return cA8bR4oK9pV5i
import os
import platform
import subprocess
import sys


def get_tailwind_binary():
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "darwin":
        os_name = "macos"
    elif system == "linux":
        os_name = "linux"
    elif system == "windows":
        os_name = "windows"
    else:
        raise ValueError(f"Unsupported operating system: {system}")

    if "arm" in machine or "aarch64" in machine:
        arch = "arm64"
    elif machine == "x86_64" or machine == "amd64":
        arch = "x64"
    elif machine == "armv7l":
        arch = "armv7"
    else:
        raise ValueError(f"Unsupported architecture: {machine}")

    extension = ".exe" if system == "windows" else ""
    return f"tailwindcss-{os_name}-{arch}{extension}"


def setup():
    binary_name = get_tailwind_binary()
    url = f"https://github.com/tailwindlabs/tailwindcss/releases/latest/download/{binary_name}"

    subprocess.run(["curl", "-sLO", url], check=True)
    if platform.system().lower() != "windows":
        subprocess.run(["chmod", "+x", binary_name], check=True)
    os.rename(binary_name, "tailwindcss")
    subprocess.run(["./tailwindcss", "init"], check=True)


def watch():
    subprocess.run(
        [
            "./tailwindcss",
            "-i",
            "shad4fast/globals.css",
            "-o",
            "./output.css",
            "--watch",
        ],
        check=True,
    )


def build():
    subprocess.run(
        [
            "./tailwindcss",
            "-i",
            "shad4fast/globals.css",
            "-o",
            "output.css",
            "--minify",
        ],
        check=True,
    )


def main():
    if len(sys.argv) < 2:
        print("Usage: shad4fast <command>")
        print("Available commands: setup, watch, build")
        sys.exit(1)

    command = sys.argv[1]
    if command == "setup":
        setup()
    elif command == "watch":
        watch()
    elif command == "build":
        build()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()

"""Capture the running Flask application's blank-input error interface."""

import os
import subprocess
import sys
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "7c_error_handling_interface.png"


def main():
    """Start the actual server, submit blank input and capture its response."""
    server = subprocess.Popen(
        [sys.executable, "server.py"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    browser = None
    try:
        time.sleep(3)
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1200,850")
        browser = webdriver.Chrome(options=options)
        browser.get("http://127.0.0.1:5000/")
        browser.find_element(By.ID, "textToAnalyze").clear()
        browser.find_element(By.CSS_SELECTOR, "button").click()
        for _ in range(30):
            if "Invalid text! Please try again!" in browser.find_element(
                By.ID, "system_response"
            ).text:
                break
            time.sleep(0.3)
        else:
            raise RuntimeError("Blank input error not displayed")
        browser.save_screenshot(str(OUT))
        print(f"Captured genuine Flask error response screenshot: {OUT.name}")
    finally:
        if browser is not None:
            browser.quit()
        server.terminate()
        try:
            server.wait(timeout=10)
        except subprocess.TimeoutExpired:
            server.kill()


if __name__ == "__main__":
    main()

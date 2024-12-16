# Keylogger

This repository contains a keylogger implementation and a decoder script for handling captured keystroke data. This was my first project involving cybersecurity, and I'm re-uploading it to GitHub for reference and sharing purposes.

## Repository Overview

- **`keylogger.py`**: This script captures keystrokes on the host machine and either sends the logs to a remote server or stores them locally based on the specified configuration.
- **`key_decoder.py`**: A script to decode the keylogs captured by the keylogger. It uses a scan-code-to-key mapping for conversion and outputs readable data.

## Features

### Keylogger (`keylogger.py`)
- Captures all keystrokes using the `keyboard` module.
- Sends data to a remote server or saves it locally based on user settings.
- Reports keystrokes at regular intervals (default: 10 seconds).
- Configurable server URL and logging interval.

### Key Decoder (`key_decoder.py`)
- Converts scan codes into readable keystrokes.
- Fetches log data from a remote server or a local file.
- Outputs the decoded keystrokes in a human-readable format.

## Usage

### Prerequisites
- Python 3.x
- Modules: `keyboard`, `urllib`

### Running the Keylogger
1. Ensure Python is installed on the target machine.
2. Set the `SERVER_URL` environment variable for remote logging or configure the script to use local file storage.
3. Run the script:
   ```bash
   python keylogger.py
   ```

### Decoding the Key Logs
1. Update the `SERVER_URL` in `key_decoder.py` to the appropriate endpoint where the logs are hosted.
2. Run the decoder:
   ```bash
   python key_decoder.py
   ```

## Warning

This project is for **educational purposes only**. Unauthorized use of this software to capture or monitor someone's activity without consent is illegal and unethical. Always ensure you have permission before using this tool on any device.

## Contributions

If you have ideas to improve the project or fix issues, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

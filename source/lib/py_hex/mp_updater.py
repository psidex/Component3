"""
Update micropython.hex
The hex is scraped from $urlwhich should be the 
latest version at all times
"""

import requests
url = "http://microbit.pythonanywhere.com/editor.html"

def update_micropython_fw():
    # Get the URL
    r = requests.get(url)
    # Get everything after the firmware tag
    firmware = r.text.split('<div id="firmware" style="display: none;">')[1]
    # Remove everything after & including the ending tags
    firmware = firmware.split("</div>")[0]

    # Save to micropython.hex
    with open("micropython.hex", "w") as f:
        f.write(firmware)

if __name__ == "__main__":
    print("Updating micropython...")
    update_micropython_fw()
    print("Done!")

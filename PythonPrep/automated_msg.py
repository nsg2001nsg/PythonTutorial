import pandas as pd
import webbrowser
import time
import urllib.parse

# === SETTINGS ===
EXCEL_PATH = "contacts.xlsx"
PHONE_COLUMN = "Phone"

# === MESSAGE TO SEND ===
COMMON_MESSAGE = """
Hello. Khushi here from nysh.in,
It was a pleasure meeting you at the CMPL exhibition!
As discussed, here's our catalog featuring our range of Natural Heat Pain Patches, Cramp Patches, Hair Spa Cap ,Eye Spa ,Ayurvedic Patches, and Travel Warmers

To help me send you more specific details , do let me know whether your interested for white labeling/OEM solutions or for distributor pricing.
"""

# === STEP 1: Read Excel File ===
df = pd.read_excel(EXCEL_PATH)

# Drop rows without phone numbers
df = df.dropna(subset=[PHONE_COLUMN])
df[PHONE_COLUMN] = df[PHONE_COLUMN].astype(str).str.replace(r'\D', '', regex=True)

# === STEP 2: Send WhatsApp Messages ===
for number in df[PHONE_COLUMN]:
    encoded_message = urllib.parse.quote(COMMON_MESSAGE.strip())
    full_url = f"https://wa.me/{number}?text={encoded_message}"
    print(f"Opening: {full_url}")
    webbrowser.open(full_url)
    time.sleep(10)  # Wait a bit before opening next message

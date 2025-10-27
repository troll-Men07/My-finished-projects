# ================================================================
# ✈️ Airplane Boarding Simulation
# Created entirely with the help of ChatGPT (OpenAI)
# Shared reference: https://chatgpt.com/share/68ff64a5-4968-8001-a397-3d1cf2a49cd1
# ================================================================

import random
import time

print("=== ✈️ Airplane Boarding Simulation ===")

# ---------- Safe Input with Retry or Default ----------
def safe_input(prompt, default, type_func):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "":
            print(f"⚙️ Using default value: {default}")
            return default
        try:
            value = type_func(user_input)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print(f"❌ Invalid input '{user_input}'")
            choice = inpu

import subprocess

# wmic csproduct
def get_thinkpad_serial_number():
    try:
        output = subprocess.check_output(['wmic', 'csproduct', 'get', 'IdentifyingNumber'])
        print(output)
        serial_number = output.decode().split('\n')[1].strip()
        return serial_number
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
serial_number = get_thinkpad_serial_number()
if serial_number:
    print(f"ThinkPad Serial Number: {serial_number}")
else:
    print("Failed to retrieve ThinkPad Serial Number.")
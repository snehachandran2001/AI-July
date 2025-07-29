import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# ✅ Extended prefix mapping for Kerala (sample list; add more for full coverage)
prefix_mapping = {
    # Kollam
    "9744": {"state": "Kerala", "district": "Kollam"},
    "9072": {"state": "Kerala", "district": "Kollam"},
    
    # Thiruvananthapuram
    "9847": {"state": "Kerala", "district": "Thiruvananthapuram"},
    "9447": {"state": "Kerala", "district": "Thiruvananthapuram"},
    
    # Ernakulam
    "8089": {"state": "Kerala", "district": "Ernakulam"},
    "9074": {"state": "Kerala", "district": "Ernakulam"},
    
    # Kozhikode
    "9061": {"state": "Kerala", "district": "Kozhikode"},
    "8301": {"state": "Kerala", "district": "Kozhikode"},
    
    # Thrissur
    "9846": {"state": "Kerala", "district": "Thrissur"},
    "9446": {"state": "Kerala", "district": "Thrissur"},
    
    # Malappuram
    "9746": {"state": "Kerala", "district": "Malappuram"},
    "9539": {"state": "Kerala", "district": "Malappuram"},
    
    # Alappuzha
    "9496": {"state": "Kerala", "district": "Alappuzha"},
    "8547": {"state": "Kerala", "district": "Alappuzha"},
    
    # Palakkad
    "8078": {"state": "Kerala", "district": "Palakkad"},
    "8590": {"state": "Kerala", "district": "Palakkad"},
    
    # Kannur
    "8281": {"state": "Kerala", "district": "Kannur"},
    "8086": {"state": "Kerala", "district": "Kannur"},
}

# ✅ Get phone number input
number = input("Enter phone number with country code: ")  # Example: +919744123456

# ✅ Parse phone number
phone_number = phonenumbers.parse(number)

# ✅ Extract details using phonenumbers
location = geocoder.description_for_number(phone_number, 'en')  # Country/Region
sim_carrier = carrier.name_for_number(phone_number, 'en')       # Operator
timezones = timezone.time_zones_for_number(phone_number)        # Timezone

# ✅ Check custom mapping for state & district
national_number = str(phone_number.national_number)  # Get 10-digit number
prefix = national_number[:4]  # First 4 digits for mapping

state = None
district = None
if prefix in prefix_mapping:
    state = prefix_mapping[prefix]["state"]
    district = prefix_mapping[prefix]["district"]

# ✅ Display results
print("\nPhone Details:")
print(f"Full Number: {number}")
print(f"Location (phonenumbers): {location}")
print(f"Carrier: {sim_carrier}")
print(f"Timezone: {timezones}")

if state:
    print(f"State: {state}")
    print(f"District: {district}")
else:
    print("State/District info not available for this prefix.")

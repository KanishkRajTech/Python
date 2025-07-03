import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = phonenumbers.parse("+918651199005")

# Region/Country
print("Region:", geocoder.description_for_number(phone_number, "en"))

# Carrier
print("Carrier:", carrier.name_for_number(phone_number, "en"))

# Timezone(s)
print("Timezone(s):", timezone.time_zones_for_number(phone_number))

# Note: phonenumbers provides only limited details:
# 1. Region/Country
# 2. Carrier (Network Provider)
# 3. Timezone(s)
# It does NOT provide personal information, address, or exact location.
# For more details (like latitude/longitude or owner info), you would need to use external APIs or databases, which may require proper authorization and may not be publicly available.
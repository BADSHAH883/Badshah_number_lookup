import phonenumbers
from phonenumbers import geocoder, carrier, timezone


def track_phone_number(number):
    parsed_number = phonenumbers.parse(number)
    
    location = geocoder.description_for_number(parsed_number, "en")
    service_provider = carrier.name_for_number(parsed_number, "en")
    time_zones = timezone.time_zones_for_number(parsed_number)
    
    
    print(f"Phone Number: {number}")
    print(f"Location (Country/Region): {location}")
    print(f"city: {geocoder.description_for_number(parsed_number, "en")}")
    print(f"Carrier: {service_provider}")
    print(f"Timezone(s): {time_zones}")
    print(f"zip code: {geocoder.description_for_number(parsed_number, "en")}")
    print(f"Valid phone number: {phonenumbers.is_valid_number(parsed_number)}")
    print(f"possible number: {phonenumbers.is_possible_number(parsed_number)}")


# Example usage:
phone_number = "+91**********"  # Replace with any number
track_phone_number(phone_number)

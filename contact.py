# Contact Page Script
from pyscript import display # pyright: ignore[reportMissingImports]

# Variables
# Contact Information
contact_us = "Contact Us"  # String
contact_description = "We'd love to hear from you!"  # String
location = "Our Location"  # String
location_description1 = "M. Paterno Street"  # String
location_description2 = "Brgy. Pasadena, San Juan City"  # String
location_description3 = "Metro Manila, Philippines"  # String
phone_number = "Phone Numbers"  # String
phone_number_description1 = "Main: (123) 456-7890"  # String
phone_number_description2 = "Mobile: (0912) 345-6789"  # String
email_address = "Email Addresses"  # String
email_address_description1 = "info@sweetchoi.com"  # String
email_address_description2 = "career@sweetchoi.com"  # String
email_address_description3 = "support@sweetchoi.com"  # String
business_hours = "Open: 12:00 PM - 9:00 PM" # String

# Contact Us: Information
display(f"{contact_us}", target = "contact_us")
display(f"{contact_description}", target = "contact_description")

display(f"{location}", target = "location")
display(f"{location_description1}", target = "location_description1")
display(f"{location_description2}", target = "location_description2")
display(f"{location_description3}", target = "location_description3")

display(f"{phone_number}", target = "phone_number")
display(f"{phone_number_description1}", target = "phone_number_description1")
display(f"{phone_number_description2}", target = "phone_number_description2")

display(f"{email_address}", target = "email_address")
display(f"{email_address_description1}", target = "email_address_description1")
display(f"{email_address_description2}", target = "email_address_description2")
display(f"{email_address_description3}", target = "email_address_description3")

display(f"{business_hours}", target = "business_hours")


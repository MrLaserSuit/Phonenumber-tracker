import phonenumbers
from test import number
from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

Key = "API_KEY"

ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))

geocoder = OpenCageGeocode(Key)

query = str(ch_nmber)

results = geocoder.geocode(query)
print(results)

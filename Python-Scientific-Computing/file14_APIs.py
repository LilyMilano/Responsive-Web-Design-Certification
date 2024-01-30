import urllib.request, urllib.parse, urllib.error
import json

# ? Services Oriented Approach ____________________________________________
# * Most non-trivial applications use services.
# * Services publish the "rules" applications must follow to make use of the service (API)

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode(
        {"address": address}
    )  # + "&key=YOUR_API_KEY"

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted_address"]
    print(location)

    """
Output:
    Enter location: Ann Arbor, MI
Retrieving http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
Retrieved 236 characters
==== Failure To Retrieve ====
{
    "error_message" : "You must use an API key to authenticate each request to Google Maps Platform APIs. For additional information, please refer to http://g.co/dev/maps-no-account",
    "results" : [],
    "status" : "REQUEST_DENIED"
}
Enter location:
"""

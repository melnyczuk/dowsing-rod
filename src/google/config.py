import os

PLACES_KEY = os.environ.get("GOOGLE_PLACES_KEY")

PLACES_NEARBY_URL = (
    "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
)

PLACES_DETAIL_URL = "https://maps.googleapis.com/maps/api/place/details/json?"

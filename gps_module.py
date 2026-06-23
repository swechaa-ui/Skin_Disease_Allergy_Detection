import requests
from geopy.distance import geodesic


def get_nearby_dermatologists(lat, lon):

    lat = float(lat)
    lon = float(lon)

    url = "https://overpass-api.de/api/interpreter"

    query = f"""
    [out:json];
    node
      ["healthcare"="doctor"]
      ["speciality"="dermatology"]
      (around:5000,{lat},{lon});
    out;
    """

    response = requests.get(url, params={"data": query})
    data = response.json()

    doctors = []

    for element in data["elements"]:

        doc_lat = element["lat"]
        doc_lon = element["lon"]

        distance = geodesic((lat, lon), (doc_lat, doc_lon)).km

        name = element["tags"].get("name", "Unknown Dermatologist")

        doctors.append({
            "name": name,
            "distance": round(distance, 2),
            "lat": doc_lat,
            "lon": doc_lon
        })

    doctors.sort(key=lambda x: x["distance"])

    return doctors[:5]
![](https://media.npr.org/assets/img/2017/11/21/gettyimages-517721024_wide-3f507851b736f80a0fc38098e93381c4f61dfa4d-s1400-c85.jpg)

# Dowsing Rod

A toolkit for web divination.

---
# Endpoints
## Google Places
### `GET /google/places/nearby`
params | type | default | description
--- | --- | --- | ---
`lat` | `float` | `required` | a latitude coordinate
`lng` | `float` | `required` | a longtitude coordinate
`rad` | `float` | `100.0` | a radius in meters for results around the coordinate
```python
[
  {
    place_id: string,
    location: {
      lat: float,
      lng: float,
    }
  }
]
```
### `GET /google/places/rating`
params | type | default | description
--- | --- | --- | ---
`place_ids` | `List[str]` | `[]` | a list of place_ids
```
[
  {
    place_id: string,
    rating: float,
  }
]
```
### `GET /google/places/reviews`
params | type | default | description
--- | --- | --- | ---
`place_ids` | `List[str]` | `[]` | a list of place_ids
```
[
  {
    place_id: string,
    reviews: {
      rating: float,
      text: string,
    }
  }
]
```
### `GET /google/places/:place_id`
params | type | default | description
--- | --- | --- | ---
`fields` | `List[str]` | `[]` | list of [google place detail fields](https://developers.google.com/places/web-service/details#PlaceDetailsResults) to return in response 
[Full response](https://developers.google.com/places/web-service/details#PlaceDetailsResponses)
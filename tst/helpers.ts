import { PlacesNearbyResponse } from "@googlemaps/google-maps-services-js";
import { PlacesNearbyResponseData } from "@googlemaps/google-maps-services-js/dist/places/placesnearby";

export const getPlacesNearbyResponse = (results: PlacesNearbyResponseData['results']): PlacesNearbyResponse => ({ 
  data: getPlacesNearbyResponseData(results), 
  status: 200, 
  statusText: 'ok', 
  headers: {}, 
  config: {}, 
});

export const getPlacesNearbyResponseData = (results: PlacesNearbyResponseData['results']): PlacesNearbyResponseData => ({
  results, 
  status: "OK", 
  error_message: 'none',
});

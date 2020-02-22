import {
  Client,
  PlacePhotoResponse,
  PlacesNearbyResponse,
} from '@googlemaps/google-maps-services-js';
import {
  PlacePhoto,
  LatLngLiteral,
} from '@googlemaps/google-maps-services-js/dist/common';

const key = process.env.GOOGLE_PLACES || '';
const maps = new Client({});

export type GoogleResponse = PlacePhotoResponse | PlacesNearbyResponse;

const parseResults = ({
  data: { error_message: error, results },
}: GoogleResponse['data']): GoogleResponse['data']['results'] => {
  if (error) console.log('Request error: ', error);
  return results;
};

export const fetchPlaces = async ({
  lat,
  lng,
  radius,
}: {
  lat: LatLngLiteral['lat'];
  lng: LatLngLiteral['lng'];
  radius: number;
}): Promise<PlacesNearbyResponse> =>
  parseResults(
    await maps.placesNearby({
      params: { location: { lat, lng }, radius, key },
    }),
  );

export const fetchPhotos = async ({
  photo: { photoreference },
  maxwidth = 1600,
  maxheight = 1600,
}: {
  photo: PlacePhoto;
  maxwidth: number;
  maxheight: number;
}): Promise<PlacePhotoResponse> =>
  parseResults(
    await maps.placePhoto({
      params: { photoreference, maxwidth, maxheight, key },
    }),
  );

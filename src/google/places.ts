import {
  Client,
  PlacePhotoResponse,
} from '@googlemaps/google-maps-services-js';
import {
  PlacePhoto,
  LatLng,
} from '@googlemaps/google-maps-services-js/dist/common';
import { PlacesNearbyResponse } from '@googlemaps/google-maps-services-js/dist/places/placesnearby';

const key = process.env.GOOGLE_KEY || '';
const maps = new Client({});

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const parseResults = ({ data: { results = [] } }: any): Promise<any> => results;

export const fetchPlaces = ({
  location = '',
  radius = 0,
}: {
  location: LatLng;
  radius: number;
}): Promise<PlacesNearbyResponse> =>
  maps.placesNearby({ params: { location, radius, key } }).then(parseResults);

export const fetchPhotos = ({
  photo: { photoreference },
  maxwidth = 1600,
  maxheight = 1600,
}: {
  photo: PlacePhoto;
  maxwidth: number;
  maxheight: number;
}): Promise<PlacePhotoResponse> =>
  maps
    .placePhoto({ params: { photoreference, maxwidth, maxheight, key } })
    .then(parseResults);

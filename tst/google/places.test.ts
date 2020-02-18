import * as places from '../../src/google/places';
import * as maps from '@googlemaps/google-maps-services-js';
import { PlacesNearbyResponseData } from '@googlemaps/google-maps-services-js/dist/places/placesnearby';
import { getPlacesNearbyResponse } from '../helpers';

describe('places', () => {
  describe('fetchPlaces', () => {
    const placesNearby = jest.spyOn(maps.Client.prototype, 'placesNearby');

    const args = {
      location: 'test',
      radius: 10,
    };

    beforeEach(() => {
      jest.clearAllMocks();
    });

    it('calls google maps client placesNearby function', async () => {
      const expected = {
        params: expect.objectContaining({ ...args }),
      };

      expect(placesNearby).not.toHaveBeenCalled();
      await places.fetchPlaces(args);
      expect(placesNearby).toHaveBeenCalledWith(expected);
    });

    it('returns a list of google places', async () => {
      const expected = ['lol'] as PlacesNearbyResponseData['results'];

      placesNearby.mockResolvedValue(getPlacesNearbyResponse(expected));

      const actual = await places.fetchPlaces(args);
      expect(actual).toStrictEqual(expected);
    });
  });
});

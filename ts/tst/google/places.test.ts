import * as places from '../../src/google/places';
import { Client } from '@googlemaps/google-maps-services-js';
import { PlacesNearbyResponseData } from '@googlemaps/google-maps-services-js/dist/places/placesnearby';
import { getGoogleResponse } from '../helpers';

jest.mock('@googlemaps/google-maps-services-js', () => ({
  Client: jest.fn().mockReturnValue({
    placesNearby: jest.fn(),
    placePhoto: jest.fn(),
  }),
}));

describe('places', () => {
  describe('fetchPlaces', () => {
    const { placesNearby } = (Client as jest.Mock)();

    const args = {
      lat: 50,
      lng: 12,
      radius: 42,
    };

    beforeEach(() => {
      jest.clearAllMocks();
    });

    it('calls google maps client placesNearby function', async () => {
      const expected = {
        params: expect.objectContaining({
          location: { lat: args.lat, lng: args.lng },
          radius: args.radius,
        }),
      };

      placesNearby.mockResolvedValueOnce({
        data: { results: [] },
      });

      expect(placesNearby).not.toHaveBeenCalled();
      await places.fetchPlaces(args);
      expect(placesNearby).toHaveBeenCalledWith(expected);
    });

    it('returns a list of google places', async () => {
      const expected = ['lol'] as PlacesNearbyResponseData['results'];

      placesNearby.mockResolvedValueOnce(getGoogleResponse(expected));

      const actual = await places.fetchPlaces(args);
      expect(actual).toStrictEqual(expected);
    });

    it('logs the error message if a request returns an error', async () => {
      const consoleSpy = jest.spyOn(console, 'log');
      const err = 'oooooooooooops';

      placesNearby.mockResolvedValueOnce(getGoogleResponse([], err));

      expect(consoleSpy).not.toHaveBeenCalled();
      await places.fetchPlaces(args);
      expect(consoleSpy).not.toHaveBeenCalledWith(err);
    });
  });
});

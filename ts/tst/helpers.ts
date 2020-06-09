import { GoogleResponse } from '../src/google/places';

export const getGoogleResponse = (
  results: GoogleResponse['data']['results'],
  err?: string,
): GoogleResponse => ({
  data: {
    // eslint-disable-next-line @typescript-eslint/camelcase
    error_message: err,
    results,
  } as GoogleResponse['data'],
  status: 200,
  statusText: 'ok',
  headers: {},
  config: {},
});

export const flushPromises = (): any => setImmediate(Promise.resolve);

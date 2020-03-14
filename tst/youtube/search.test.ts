import ytsr from 'ytsr';

import { search } from '../../src/youtube';

jest.mock('ytsr');

describe('YouTube', () => {
  describe('search', () => {
    it('calls ytsr with search query', () => {
      expect(ytsr).not.toHaveBeenCalled();
      search({ q: 'test' });
      expect(ytsr).toHaveBeenCalledWith('test');
    });
  });
});

import ytsr from 'ytsr';

import { search } from '../../src/youtube';

jest.mock('ytsr');

describe('YouTube', () => {
  describe('search', () => {
    it('calls ytsr with search query', async () => {
      const expected = 'test';

      ((ytsr as unknown) as jest.Mock).mockResolvedValueOnce(expected);

      expect(ytsr).not.toHaveBeenCalled();
      const data = await search({ q: 'test' });
      expect(ytsr).toHaveBeenCalledWith('test');
      expect(data).toBe(expected);
    });
  });
});

import ytdl from 'ytdl-core';
import ytsr from 'ytsr';

import { info, rip, search } from '../../src/youtube';

jest.mock('ytdl-core');
jest.mock('ytsr');

describe('YouTube', () => {
  describe('info', () => {
    it('calls ytdl.getInfo with the correct query string', () => {
      expect(ytdl.getInfo).not.toHaveBeenCalled();
      info({ q: 'test' });
      expect(ytdl.getInfo).toHaveBeenCalledWith(
        'http://www.youtube.com/watch?v=test',
      );
    });
  });

  describe('rip', () => {
    it('calls ytdl with the search query', () => {
      expect(ytdl).not.toHaveBeenCalled();
      rip({ q: 'test' });
      expect(ytdl).toHaveBeenCalledWith('http://www.youtube.com/watch?v=test');
    });
  });

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

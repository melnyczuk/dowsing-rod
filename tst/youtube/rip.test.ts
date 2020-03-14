import ytdl from 'ytdl-core';

import { rip } from '../../src/youtube';

jest.mock('ytdl-core');

describe('YouTube', () => {
  describe('rip', () => {
    it('calls ytdl with the search query', () => {
      expect(ytdl).not.toHaveBeenCalled();
      rip({ q: 'test' });
      expect(ytdl).toHaveBeenCalledWith('test');
    });
  });
});

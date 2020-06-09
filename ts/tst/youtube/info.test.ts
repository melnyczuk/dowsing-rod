import ytdl from 'ytdl-core';

import { info } from '../../src/youtube';

jest.mock('ytdl-core');

describe('YouTube', () => {
  describe('info', () => {
    it('calls ytdl.getInfo with the correct query string', () => {
      expect(ytdl.getInfo).not.toHaveBeenCalled();
      info({ q: 'test' });
      expect(ytdl.getInfo).toHaveBeenCalledWith('test');
    });
  });
});

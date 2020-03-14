import ytdl from 'ytdl-core';

import { info } from '../../src/youtube';

jest.mock('ytdl-core');

describe('YouTube', () => {
  describe('info', () => {
    it('uses ytdl', () => {
      expect(ytdl.getInfo).not.toHaveBeenCalled();
      info({ q: 'test' });
      expect(ytdl.getInfo).toHaveBeenCalledWith('test');
    });
  });
});

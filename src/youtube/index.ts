import ytdl, { videoInfo } from 'ytdl-core';
import ytsr from 'ytsr';

const YTURL = 'http://www.youtube.com/watch?v=';

interface Query {
  q: string;
}

export const rip = async ({ q }: Query): Promise<any> => ytdl(YTURL + q);

export const info = async ({ q }: Query): Promise<videoInfo> =>
  await ytdl.getInfo(YTURL + q);

export const search = async ({ q }: Query): Promise<any> => await ytsr(q);

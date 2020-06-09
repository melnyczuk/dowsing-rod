import ytdl from 'ytdl-core';

export default async ({ q }: { q: string }): Promise<any> =>
  await ytdl.getInfo(q);

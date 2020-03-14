import ytsr from 'ytsr';

export default async ({ q }: { q: string }): Promise<any> => await ytsr(q);

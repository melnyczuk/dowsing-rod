require('dotenv').config();
import express from 'express';
import * as pkgs from '../src';

const app = express();
const HOST = process.env.HOST || 'localhost';
const PORT = parseInt(process.env.PORT || '6666');

app.listen(PORT, HOST, () => console.log('dowsing...'));

app.get(
  '/:pkg/:subpkg/:func',
  async ({ params: { pkg, subpkg, func }, query, url }, res) => {
    try {
      console.log('url', url, 'query', query);
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      res.send(await (pkgs as any)[pkg][subpkg][func](query));
    } catch (e) {
      res.send({ type: '/:pkg/:func', url, query });
    }
  },
);

app.get('/:pkg/:func', async ({ params: { pkg, func }, query, url }, res) => {
  try {
    console.log('url', url, 'query', query);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    res.send(await (pkgs as any)[pkg][func](query));
  } catch (e) {
    console.log('query', query);
    res.send({ type: '/:pkg/:func', url, query });
  }
});

app.get('/:any', ({ url }, res) => {
  res.send(url);
});

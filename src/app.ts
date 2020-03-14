require('dotenv').config();
import express from 'express';
import * as pkgs from '.';

const app = express();
const HOST = process.env.HOST || 'localhost';
const PORT = parseInt(process.env.PORT || '6666');

app.listen(PORT, HOST, () => console.log('dowsing...'));

app.get(
  '/:pkg/:subpkg/:func',
  async ({ url, params: { pkg, subpkg, func }, query }, res) => {
    console.log('request: ', url);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    res.send(await (pkgs as any)[pkg][subpkg][func](query));
  },
);

app.get('/:pkg/:func', async ({ url, params: { pkg, func }, query }, res) => {
  console.log('request: ', url);
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  res.send(await (pkgs as any)[pkg][func](query));
});

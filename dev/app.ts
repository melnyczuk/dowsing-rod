require('dotenv').config();
import * as express from 'express';
import * as fs from 'fs';

const app = express();
const HOST = process.env.HOST || 'localhost';
const PORT = parseInt(process.env.PORT || '6666');

app.listen(PORT, HOST, () => console.log('dowsing...'));

app.get(
  '/:pkg/:subpkg/:func',
  async ({ params: { pkg, subpkg, func } }, res) => {
    const uri = `${__dirname}/data/${pkg}/${subpkg}/${func}.json`;
    console.log(`mocking request: ${uri}`);
    try {
      const data = await fs.readFileSync(uri);
      res.send(data);
    } catch (e) {
      if (e.code === 'ENOENT') {
        console.log('404', e.path, e.message);
        res.status(404).send(e);
      } else {
        console.log('500', e.message);
        res.status(500).send(e);
      }
    }
  },
);

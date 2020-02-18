import * as express from 'express';
import * as pkgs from '.';

require('dotenv').config();

const app = express();
const HOST = process.env.HOST || 'localhost';
const PORT = parseInt(process.env.PORT || '6666');

app.listen(PORT, HOST, () => console.log('dowsing...'));

app.get(
  '/:pkg/:subpkg/:func', 
  async ({ url, params: { pkg, subpkg, func }, query }, res) => {
    console.log('request: ', url);
    res.send(await (pkgs as any)[pkg][subpkg][func](query));
  });

require('dotenv').config();
import * as express from 'express';
import * as fs from 'fs';

const app = express();
const HOST = process.env.HOST || 'localhost';
const PORT = parseInt(process.env.PORT || '6666');

app.listen(PORT, HOST, () => console.log('dummy dowsing...'));

app.get('/:pkg/:subpkg/:func', async ({ path }, res) => {
  console.log(`mocking request: ${path}`);
  try {
    const data = await fs.readFileSync(`${__dirname}/data/${path}.json`);
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
});

require('dotenv').config();
import axios, { AxiosRequestConfig } from 'axios';
import express from 'express';
import * as config from './config';

const app = express();
const HOST = process.env.HOST || 'localhost';
const PORT = parseInt(process.env.PORT || '6666');

app.listen(PORT, HOST, () => console.log('dowsing...'));

const services = Object.keys(config);

function api<T = unknown>(
  cfg: AxiosRequestConfig,
  params: Record<string, unknown>,
): Promise<T> {
  return axios({ ...cfg, params }).then(resp => resp.data);
}

app.get('/:pkg/:func', async ({ url, params: { pkg }, query }, res) => {
  console.log('request: ', url);
  if (services.includes(pkg)) {
    res.send(await api((config as any)[pkg], query));
  }
  res.status(404).send('service is not present');
});

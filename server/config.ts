import { AxiosRequestConfig } from 'axios';

const google: AxiosRequestConfig = {
  method: 'get',
  baseURL: 'https://maps.googleapis.com',
  url: '/maps/api/place/nearbysearch/json?',
  responseType: 'json',
};

export default { google };

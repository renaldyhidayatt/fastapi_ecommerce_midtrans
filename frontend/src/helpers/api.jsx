import axios from 'axios';

export const myApi = axios.create({
  baseURL: 'https://weak-blue-katydid-kit.cyclic.app/api',
});

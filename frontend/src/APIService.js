import axios from 'axios';
const API_URL = 'http://127.0.0.1:7000';
export class APIService {

  constructor() {
  }


  getAllRecords() {
    const url = `${API_URL}/api/year/`;
    return axios.get(url).then(response => response.data);
  }
}


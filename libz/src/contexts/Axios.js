import axios from 'axios';

const axiosRequest = axios.create({
    withCredentials: true,
});

export default axiosRequest;

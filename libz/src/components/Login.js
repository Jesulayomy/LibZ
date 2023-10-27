import { useContext, useState } from 'react';
import axios from 'axios';
import { AuthContext } from '../contexts/AuthContext';

function Login({ close }) {
  const { login } = useContext(AuthContext);
  const [credentials, setCredentials] = useState({
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials((prevCredentials) => ({
      ...prevCredentials,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('email', credentials.email);
    formData.append('password', credentials.password);
    try {
      const res = await axios.post(
        'http://127.0.0.1:5000/auth/login',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        },
        { withCredentials: true }
      );
      const user = res.data;
      close();
      login(user);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type='email'
        name='email'
        value={credentials.email}
        placeholder='Enter Email'
        onChange={handleChange}
      />
      <br />
      <input
        type='password'
        name='password'
        value={credentials.password}
        placeholder='Enter Password'
        onChange={handleChange}
      />
      <br />
      <input type='submit' value='Login' />
    </form>
  );
}

export default Login;

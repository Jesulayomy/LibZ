import { useContext, useState } from 'react';
import axios from 'axios';
import { Navigate } from 'react-router';
import { AuthContext } from '../contexts/AuthContext';

function Login() {
  const { isLoggedIn, login } = useContext(AuthContext);
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
        'http://localhost:5000/auth/login',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        },
        { withCredentials: true }
      );
      const user = res.data;
      console.log(user);
      login(user);
    } catch (err) {
      console.log(err);
    }
  };

  return isLoggedIn ? (
    <Navigate replace to='/' />
  ) : (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type='email'
          name='email'
          value={credentials.email}
          placeholder='Email'
          onChange={handleChange}
        />
        <br />
        <input
          type='password'
          name='password'
          value={credentials.password}
          placeholder='Password'
          onChange={handleChange}
        />
        <br />
        <button type='submit'>Login</button>
      </form>
    </div>
  );
}

export default Login;

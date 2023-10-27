import { useContext, useState } from 'react';
import axios from 'axios';
import { AuthContext } from '../contexts/AuthContext';

function SignUp({ close }) {
  const { login } = useContext(AuthContext);
  const [userData, setUserData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    display_name: '',
    gender: '',
    date_of_birth: '',
    phone: '',
    password: '',
    confirmPassword: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUserData((prevUserData) => ({
      ...prevUserData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    for (const key in userData) {
      if (key !== 'confirmPassword') formData.append(key, userData[key]);
    }
    try {
      const res = await axios.post('http://127.0.0.1:5000/api/users', formData);
      const user = res.data;
      close();
      login(user);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type='text'
        name='first_name'
        placeholder='Enter First Name'
        value={userData.first_name}
        onChange={handleChange}
      />
      <br />
      <input
        type='text'
        name='last_name'
        placeholder='Enter Last Name'
        value={userData.last_name}
        onChange={handleChange}
      />
      <br />
      <input
        type='email'
        name='email'
        placeholder='Enter Email Address'
        value={userData.email}
        onChange={handleChange}
      />
      <br />
      <input
        type='text'
        name='display_name'
        placeholder='Choose a Display Name'
        value={userData.display_name}
        onChange={handleChange}
      />
      <br />
      <select name='gender' value={userData.gender} onChange={handleChange}>
        <option>Gender</option>
        <option>Male</option>
        <option>Female</option>
        <option>Other</option>
      </select>
      <input
        type='date'
        name='date_of_birth'
        placeholder='Date of Birth'
        value={userData.date_of_birth}
        onChange={handleChange}
      />
      <br />
      <input
        type='tel'
        name='phone'
        placeholder='Enter Phone Number'
        value={userData.phone}
        onChange={handleChange}
      />
      <br />
      <input
        type='password'
        name='password'
        placeholder='Enter Password'
        value={userData.password}
        onChange={handleChange}
      />
      <br />
      <input
        type='password'
        name='confirmPassword'
        placeholder='Confirm Password'
        value={userData.confirmPassword}
        onChange={handleChange}
      />
      <br />
      <input type='submit' value='Sign Up' />
    </form>
  );
}

export default SignUp;

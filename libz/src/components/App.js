/* eslint-disable react-hooks/exhaustive-deps */
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useEffect, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from '../contexts/AuthContext';
import Home from '../pages/Home';
import Login from '../pages/Login';
import Layout from '../pages/Layout';

function App() {
  const { login } = useContext(AuthContext);
  // const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getCurrentUser = async () => {
      try {
        const res = await axios.get('http://localhost:5000/auth/current_user', {
          withCredentials: true,
        });
        const user = res.data;
        console.log(user);
        if (Object.keys(user).length > 0) login(user);
      } catch (err) {
        console.log(err);
      }
    };
    getCurrentUser();
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route index element={<Home />} />
          <Route path='login' element={<Login />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

/* eslint-disable react-hooks/exhaustive-deps */
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from '../contexts/AuthContext';
import Home from '../pages/Home';
import Layout from '../pages/Layout';
import Profile from '../pages/Profile';

function App() {
  const { login, user } = useContext(AuthContext);
  const [showLogin, setShowLogin] = useState(false);
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
        <Route path='/' element={<Layout setShowLogin={setShowLogin} />}>
          <Route
            index
            element={<Home showLogin={showLogin} setShowLogin={setShowLogin} />}
          />
          <Route path='profile' element={<Profile user={user} />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

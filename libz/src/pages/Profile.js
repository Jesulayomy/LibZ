import { useContext } from 'react';
import { useNavigate } from 'react-router';
import axios from 'axios';
import { BiLogOut } from 'react-icons/bi';
import { AuthContext } from '../contexts/AuthContext';
import ProfileDetails from '../components/ProfileDetails';
import ProfileBooks from '../components/ProfileBooks';
import '../styles/Profile.css';

function Profile({ user }) {
  const navigate = useNavigate();
  const { isLoggedIn, logout } = useContext(AuthContext);

  const handleLogout = async () => {
    try {
      await axios.post('http://localhost:5000/auth/logout');
      logout();
    } catch (error) {
      console.log(error);
    }
  };

  if (!isLoggedIn) navigate('/');

  return (
    <div className='profile-page'>
      <div className='button logout' onClick={handleLogout}>
        Logout
        <BiLogOut color='white' />
      </div>
      <ProfileDetails user={user} />
      <ProfileBooks user={user} />
    </div>
  );
}

export default Profile;

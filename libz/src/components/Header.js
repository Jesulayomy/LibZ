import { useContext } from 'react';
import { useNavigate } from 'react-router';
import { AuthContext } from '../contexts/AuthContext';
import SearchBox from './SearchBox';
import '../styles/Header.css';

function Header({ setShowLogin }) {
  const { isLoggedIn } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleImageClick = () => {
    if (isLoggedIn) navigate('/profile');
    else setShowLogin(true);
  };

  return (
    <header>
      <h1 onClick={() => navigate('/')}>LibZ</h1>
      <div className='flex-div'>
        <SearchBox />
        <img
          src='https://picsum.photos/200'
          alt='Profile'
          onClick={handleImageClick}
        />
      </div>
    </header>
  );
}

export default Header;

import { useContext } from 'react';
import { useNavigate } from 'react-router';
import { useLocation } from 'react-router';
import { AuthContext } from '../contexts/AuthContext';
import default_user from '../images/default_user.png';
import SearchBox from './SearchBox';
import '../styles/Header.css';

function Header({
  setShowLogin,
  searchBooks,
  searchedBooks,
  searchQuery,
  setSearchQuery,
}) {
  const { isLoggedIn, user } = useContext(AuthContext);
  const navigate = useNavigate();
  const location = useLocation();
  const { pathname } = location;

  const handleImageClick = () => {
    if (isLoggedIn) navigate('/profile');
    else setShowLogin(true);
  };

  return (
    <header>
      <h1 onClick={() => navigate('/')}>LibZ</h1>
      <div className='flex-div'>
        {pathname !== '/profile' && (
          <SearchBox
            searchBooks={searchBooks}
            searchedBooks={searchedBooks}
            searchQuery={searchQuery}
            setSearchQuery={setSearchQuery}
          />
        )}
        <img
          src={(user && user.image) ? require(`../images/${user.image}`) : default_user}
          alt='Profile'
          onClick={handleImageClick}
        />
      </div>
    </header>
  );
}

export default Header;

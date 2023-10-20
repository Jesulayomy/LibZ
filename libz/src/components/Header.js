import { IoIosSearch } from 'react-icons/io';
import '../styles/Header.css';

function Header() {
  return (
    <header>
      <h1>LibZ</h1>
      <div className='flex-div'>
        <div className='search-box'>
          <input type='text' />
          <button>
            <IoIosSearch />
          </button>
        </div>
        <img src='https://picsum.photos/200' alt='Profile' />
      </div>
    </header>
  );
}

export default Header;

import { IoIosSearch } from 'react-icons/io';

function SearchBox() {
  return (
    <div className='search-box'>
      <input type='text' />
      <button>
        <IoIosSearch />
      </button>
    </div>
  );
}

export default SearchBox;

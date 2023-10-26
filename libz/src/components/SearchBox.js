import { IoIosSearch } from 'react-icons/io';
import { AiOutlineClose } from 'react-icons/ai';

function SearchBox({
  searchBooks,
  searchedBooks,
  searchQuery,
  setSearchQuery,
}) {
  return (
    <div className='search-box'>
      <input
        type='text'
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <button onClick={() => searchBooks(searchQuery)}>
        {searchedBooks && searchedBooks.length > 0 ? (
          <AiOutlineClose />
        ) : (
          <IoIosSearch />
        )}
      </button>
    </div>
  );
}

export default SearchBox;

/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from 'react';
import axios from 'axios';
import ProfileBookCard from './ProfileBookCard';
import SearchBox from './SearchBox';

function ProfileBooks({ user }) {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const getBooks = async () => {
      try {
        const response = await axios.get(
          `http://localhost:5000/api/users/${user.id}/books`
        );
        setBooks(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    getBooks();
  }, []);

  console.log(books);

  return (
    <div className='profile-books'>
      <SearchBox />
      <div className='profile-books-list'>
        {books.map((book) => (
          <ProfileBookCard key={book.id} book={book} />
        ))}
      </div>
    </div>
  );
}

export default ProfileBooks;

/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from 'react';
import axiosRequest from '../utils/Axios';
import ProfileBookCard from './ProfileBookCard';
import SearchBox from './SearchBox';

function ProfileBooks({ user }) {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const getBooks = async () => {
      try {
        const response = await axiosRequest.get(
          `http://127.0.0.1:5000/api/users/${user.id}/books`
        );
        setBooks(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    getBooks();
  }, []);

  const deleteBook = async (id) => {
    try {
      await axiosRequest.delete(`http://127.0.0.1:5000/api/books/${id}`);
      setBooks(books.filter((book) => book.id !== id));
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className='profile-books'>
      <SearchBox />
      <div className='profile-books-list'>
        {books.map((book) => (
          <ProfileBookCard key={book.id} book={book} deleteBook={deleteBook} />
        ))}
      </div>
    </div>
  );
}

export default ProfileBooks;

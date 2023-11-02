import { useState, useEffect } from 'react';
import { RiFileUploadFill } from 'react-icons/ri';
import axiosRequest from '../utils/Axios';
import Card from '../components/Card';
import TopUpload from '../components/TopUpload';
import BookDetails from '../components/BookDetails';
import BookUpload from '../components/BookUpload';
import AuthPage from '../components/AuthPage';
import '../styles/Home.css';

function Home({ showLogin, setShowLogin, searchedBooks }) {
  const [books, setBooks] = useState([]);
  const [topBooks, setTopBooks] = useState([]);
  const [topUploaders, setTopUploaders] = useState([]);
  const [bookDetails, setBookDetails] = useState(null);
  const [showUpload, setShowUpload] = useState(false);

  useEffect(() => {
    const getAllBooks = async () => {
      try {
        const res = await axiosRequest.get('http://127.0.0.1:5000/api/books', {
          withCredentials: true,
        });
        setBooks(res.data);
      } catch (err) {
        console.log(err);
      }
    };

    const getTopBooks = async () => {
      try {
        const res = await axiosRequest.get(
          'http://127.0.0.1:5000/api/books/top',
          {
            withCredentials: true,
          }
        );
        setTopBooks(res.data);
      } catch (err) {
        console.log(err);
      }
    };

    const getTopUploaders = async () => {
      try {
        const res = await axiosRequest.get(
          'http://127.0.0.1:5000/api/users/top',
          {
            withCredentials: true,
          }
        );
        setTopUploaders(res.data);
      } catch (err) {
        console.log(err);
      }
    };

    getAllBooks();
    getTopBooks();
    getTopUploaders();
  }, []);

  return (
    <div className='home'>
      <p className='sub-head'>
        A library for your <span className='span-books'>Books</span>
      </p>
      <div className='top'>
        <div className='top-downloads'>
          <h2>Top downloads</h2>
          <div className='top-downloads-in'>
            {topBooks.map((book) => (
              <Card
                key={book.id}
                name={book.name}
                author={book.author}
                thumbnailLink={book.thumbnailLink}
                cardClass='top-card'
                showDetails={() => setBookDetails(book)}
              />
            ))}
          </div>
        </div>
        <div className='top-uploaders'>
          <h2>Top uploaders</h2>
          <div className='top-uploaders-in'>
            {topUploaders.map((uploader) => (
              <TopUpload
                key={uploader.id}
                avatarUrl='https://picsum.photos/200/300'
                displayName={uploader.display_name}
                uploads={uploader.uploads}
              />
            ))}
          </div>
        </div>
      </div>
      <div className='card-container'>
        {searchedBooks.length > 0
          ? searchedBooks.map((book) => (
              <Card
                key={book.id}
                name={book.name}
                author={book.author}
                thumbnailLink={book.thumbnailLink}
                cardClass='norm-card'
                showDetails={() => setBookDetails(book)}
              />
            ))
          : books.map((book) => (
              <Card
                key={book.id}
                name={book.name}
                author={book.author}
                thumbnailLink={book.thumbnailLink}
                cardClass='norm-card'
                showDetails={() => setBookDetails(book)}
              />
            ))}
      </div>
      {bookDetails && (
        <div className='modal'>
          <BookDetails
            name={bookDetails.name}
            description={bookDetails.description}
            author={bookDetails.author}
            uploader={bookDetails.uploader}
            downloads={bookDetails.downloads}
            thumbnailLink={bookDetails.thumbnailLink}
            downloadLink={bookDetails.downloadLink}
            close={() => setBookDetails(null)}
          />
        </div>
      )}
      {showUpload && (
        <div className='modal'>
          <BookUpload close={() => setShowUpload(false)} />
        </div>
      )}
      {showLogin && (
        <div className='modal'>
          <AuthPage close={() => setShowLogin(false)} />
        </div>
      )}
      <button className='upload-button' onClick={() => setShowUpload(true)}>
        <RiFileUploadFill color='white' />
      </button>
    </div>
  );
}

export default Home;

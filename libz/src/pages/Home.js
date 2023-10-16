import { useState } from 'react';
import Card from '../components/Card';
import TopUpload from '../components/TopUpload';
import BookDetails from '../components/BookDetails';
import BookUpload from '../components/BookUpload';
import { mockBooks, mockTopBooks, mockUploaders } from '../mock';
import '../styles/Home.css';

function Home() {
  const [bookDetails, setBookDetails] = useState(null);
  const [showUpload, setShowUpload] = useState(false);
  return (
    <div className='home'>
      <p className='sub-head'>
        A library for your <span className='span-books'>Books</span>
      </p>
      <div className='top'>
        <div className='top-downloads'>
          <h2>Top downloads</h2>
          <div className='top-downloads-in'>
            {mockTopBooks.map((book, index) => (
              <Card
                key={book.name + index}
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
            {mockUploaders.map((uploader, index) => (
              <TopUpload
                key={uploader.displayName + index}
                avatarUrl={uploader.avatarUrl}
                displayName={uploader.displayName}
                downloads={uploader.downloads}
              />
            ))}
          </div>
        </div>
      </div>
      <div className='card-container'>
        {mockBooks.map((book, index) => (
          <Card
            key={book.name + index}
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
      <button className='upload-button' onClick={() => setShowUpload(true)}>
        Upload Book
      </button>
    </div>
  );
}

export default Home;

import { BiDownload } from 'react-icons/bi';
import { MdDelete } from 'react-icons/md';

function ProfileBookCard({ book, deleteBook }) {
  return (
    <div className='book-card'>
      <div className='header'>
        <img
          src='https://picsum.photos/200/300'
          alt={book.title}
          className='profile-book-card-image'
        />
        <div>{book.description}</div>
      </div>
      <div className='book-card-details'>
        <div className='title'>
          <p className='book-card-title'>{book.name}</p>
        </div>
        <div className='details'>
          <p className='book-card-author'>Author: {book.author}</p>
          <p className='book-card-downloads'>Downloads: {book.downloads}</p>
        </div>
      </div>
      <div className='actions'>
        <button className='delete-button' onClick={() => deleteBook(book.id)}>
          <MdDelete />
        </button>
        <a href={book.downloadLink} rel='noreferrer'>
          <BiDownload />
        </a>
      </div>
    </div>
  );
}

export default ProfileBookCard;

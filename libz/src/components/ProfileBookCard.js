function ProfileBookCard({ book }) {
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
    </div>
  );
}

export default ProfileBookCard;

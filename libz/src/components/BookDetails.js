import '../styles/BookDetails.css';

function BookDetails({
  name,
  description,
  author,
  uploader,
  downloads,
  thumbnailLink,
  downloadLink,
  close,
}) {
  return (
    <div className='modal'>
      <div className='book-details'>
        <button onClick={close} className='close-button'>
          Close
        </button>
        <img src={thumbnailLink} alt={name} />
        <div className='book-details-body'>
          <p className='name'>{name}</p>
          <p className='description'>{description}</p>
          <p>Author: {author}</p>
          <p>Uploaded by: {uploader}</p>
          <p>Downloads: {downloads}</p>
          <a href={downloadLink} target='_blank' rel='noreferrer'>
            <button>Download</button>
          </a>
        </div>
      </div>
    </div>
  );
}

export default BookDetails;

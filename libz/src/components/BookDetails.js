import { BiDownload } from 'react-icons/bi';
import { AiOutlineClose } from 'react-icons/ai';
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
    <div className='book-details'>
      <button onClick={close} className='close-button'>
        <AiOutlineClose color='white' />
      </button>
      <img src={thumbnailLink} alt={name} />
      <div className='book-details-body'>
        <p className='name'>{name}</p>
        <p className='description'>{description}</p>
        <p>Author: {author}</p>
        <p>Uploaded by: {uploader}</p>
        <p>Downloads: {downloads}</p>
        <a href={downloadLink} rel='noreferrer'>
          <BiDownload color='white' />
        </a>
      </div>
    </div>
  );
}

export default BookDetails;

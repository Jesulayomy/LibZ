import { BiDownload } from 'react-icons/bi';
import { AiOutlineClose } from 'react-icons/ai';
import axiosRequest from '../utils/Axios';
import default_book from '../images/default_book.jpg';
import '../styles/BookDetails.css';

function BookDetails({
  id,
  name,
  description,
  author,
  uploader,
  downloads,
  thumbnailLink,
  downloadLink,
  close,
}) {

  const handleDownload = async (e) => {
    const formData = new FormData();
    formData.append('downloads', downloads + 1);
    try {
      const res = await axiosRequest.put(
        `http://127.0.0.1:5000/api/books/${id}`,
        formData
      );
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className='book-details'>
      <button onClick={close} className='close-button'>
        <AiOutlineClose color='white' />
      </button>
      <img src={thumbnailLink ? require(`../images/${thumbnailLink}`) : default_book} alt={name} />
      <div className='book-details-body'>
        <p className='name'>{name}</p>
        <p className='description'>{description}</p>
        <p>Author: {author}</p>
        <p>Uploaded by: {uploader}</p>
        <p>Downloads: {downloads}</p>
        <a href={downloadLink} rel='noreferrer' onClick={handleDownload}>
          <BiDownload color='white' />
        </a>
      </div>
    </div>
  );
}

export default BookDetails;

import { useState } from 'react';
import { AiOutlineClose } from 'react-icons/ai';
import axiosRequest from '../contexts/Axios';
import '../styles/BookUpload.css';

function BookUpload({ close }) {
  const [uploadData, setUploadData] = useState({
    name: '',
    author: '',
    description: '',
  });
  const [isPublic, setIsPublic] = useState(false);
  const [file, setFile] = useState(null);

  const handleFormChange = (e) => {
    const { name, value } = e.target;
    setUploadData((previousUploadData) => ({
      ...previousUploadData,
      [name]: value,
    }));
  };

  const clearForm = () => {
    setUploadData({
      name: '',
      author: '',
      description: '',
    });
    setIsPublic(false);
    setFile(null);
  };

  const uploadBook = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('name', uploadData.name);
    formData.append('author', uploadData.author);
    formData.append('description', uploadData.description);
    formData.append('public', isPublic);
    formData.append('book_file', file);
    try {
      const res = await axiosRequest.post(
        'http://127.0.0.1:5000/api/books/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        },
        { withCredentials: true }
      );
      console.log(res);
    } catch (err) {
      console.log(err);
    } finally {
      clearForm();
    }
  };

  return (
    <div className='book-upload'>
      <button onClick={close} className='close-button'>
        <AiOutlineClose />
      </button>
      <p>Upload a book</p>
      <form onSubmit={uploadBook}>
        <input
          type='text'
          name='name'
          placeholder='Title'
          value={uploadData.name}
          onChange={handleFormChange}
        />
        <br />
        <input
          type='text'
          name='author'
          placeholder='Author'
          value={uploadData.author}
          onChange={handleFormChange}
        />
        <br />
        <label htmlFor='public'>Public</label>
        <input
          type='checkbox'
          id='public'
          checked={isPublic}
          name='public'
          onChange={(e) => setIsPublic(e.target.checked)}
        />
        <br />
        <textarea
          name='description'
          placeholder='Description'
          value={uploadData.description}
          onChange={handleFormChange}
        />
        <br />
        <input
          type='file'
          name='book_file'
          onChange={(e) => setFile(e.target.files[0])}
        />
        <br />
        <input type='submit' value='Upload' />
      </form>
    </div>
  );
}

export default BookUpload;

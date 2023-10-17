import '../styles/BookUpload.css';

function BookUpload({ close }) {
  return (
    <div className='book-upload'>
      <button onClick={close} className='close-button'>
        Close
      </button>
      <p>Upload a book</p>
      <form>
        <input type='text' name='title' placeholder='Title' />
        <br />
        <input type='text' name='author' placeholder='Author' />
        <br />
        <input type='text' name='description' placeholder='Describe the book' />
        <br />
        <label for='isPublic'>Public</label>
        <input type='checkbox' name='isPublic' />
        <br />
        <input type='file' name='file' />
        <br />
        <input type='submit' value='Upload' />
      </form>
    </div>
  );
}

export default BookUpload;

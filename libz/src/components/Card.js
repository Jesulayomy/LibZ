import '../styles/Card.css';
import default_book from '../images/default_book.jpg';

function Card({ name, author, thumbnailLink, cardClass, showDetails }) {
  return (
    <div className={'card ' + cardClass}>
      <img src={thumbnailLink ? require(`../images/${thumbnailLink}`) : default_book} alt={name} />
      <div className='card-body'>
        <p className='name'>{name}</p>
        <p className='author'>By {author}</p>
        <div className='details-button' onClick={showDetails}>
          <div></div>
          <div></div>
          <div></div>
        </div>
      </div>
    </div>
  );
}

export default Card;

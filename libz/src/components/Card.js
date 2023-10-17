import '../styles/Card.css';

function Card({ name, author, thumbnailLink, cardClass, showDetails }) {
  return (
    <div className={'card ' + cardClass}>
      <div className='card-img'>
        <img src={thumbnailLink} alt={name} />
      </div>
      <div className='card-body'>
        <p className='name'>{name}</p>
        <p className='author'>By {author}</p>
        <button onClick={showDetails}>More</button>
      </div>
    </div>
  );
}

export default Card;

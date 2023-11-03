import '../styles/TopUpload.css';
import default_user from '../images/default_user.png';

function TopUpload({ avatarUrl, displayName, uploads }) {
  return (
    <div className='top-upload'>
      <div>
        <img src={avatarUrl ? require(`../images/${avatarUrl}`) : default_user} alt={displayName} />
      </div>
      <div>{displayName}</div>
      <div>{uploads} uploads</div>
    </div>
  );
}

export default TopUpload;

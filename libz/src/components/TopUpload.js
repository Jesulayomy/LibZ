import '../styles/TopUpload.css';

function TopUpload({ avatarUrl, displayName, uploads }) {
  return (
    <div className='top-upload'>
      <div>
        <img src={avatarUrl} alt={displayName} />
      </div>
      <div>{displayName}</div>
      <div>{uploads} uploads</div>
    </div>
  );
}

export default TopUpload;

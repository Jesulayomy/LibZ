import '../styles/TopUpload.css';

function TopUpload({ avatarUrl, displayName, downloads }) {
  return (
    <div className='top-upload'>
      <div>
        <img src={avatarUrl} alt={displayName} />
      </div>
      <div>{displayName}</div>
      <div>{downloads} downloads</div>
    </div>
  );
}

export default TopUpload;

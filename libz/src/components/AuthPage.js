import { useContext, useState } from 'react';
import { AiOutlineClose } from 'react-icons/ai';
import { AuthContext } from '../contexts/AuthContext';
import Login from './Login';
import SignUp from './SignUp';
import '../styles/AuthPage.css';

function AuthPage({ close }) {
  const { isLoggedIn } = useContext(AuthContext);
  const [isSigningUp, setIsSigningUp] = useState(false);

  if (isLoggedIn) close();

  return (
    <div className='login-form'>
      <button onClick={close} className='close-button'>
        <AiOutlineClose color='black' />
      </button>
      <div className='select-login'>
        <div
          className={isSigningUp ? 'current' : ''}
          onClick={() => setIsSigningUp(true)}
        >
          Sign Up
        </div>
        <div
          className={!isSigningUp ? 'current' : ''}
          onClick={() => setIsSigningUp(false)}
        >
          Login
        </div>
      </div>
      {isSigningUp ? <SignUp /> : <Login />}
    </div>
  );
}

export default AuthPage;

import { Outlet } from 'react-router-dom';
import Header from '../components/Header';
import '../styles/Layout.css';

function Layout({ setShowLogin }) {
  return (
    <>
      <Header setShowLogin={setShowLogin} />
      <Outlet />
    </>
  );
}

export default Layout;

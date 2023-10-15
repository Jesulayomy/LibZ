import { Outlet } from 'react-router-dom';
import Header from '../components/Header';
import '../styles/Layout.css';

function Layout() {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
}

export default Layout;

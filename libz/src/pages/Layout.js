import { Outlet } from 'react-router-dom';
import Header from '../components/Header';
import '../styles/Layout.css';

function Layout({
  setShowLogin,
  searchBooks,
  searchedBooks,
  searchQuery,
  setSearchQuery,
}) {
  return (
    <>
      <Header
        setShowLogin={setShowLogin}
        searchBooks={searchBooks}
        searchedBooks={searchedBooks}
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
      />
      <Outlet />
    </>
  );
}

export default Layout;

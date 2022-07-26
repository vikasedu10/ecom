import './App.css';
import { About } from './About';
import { Header } from './Header';
import { Contact } from './Contact';
import { Footer } from './Footer';
import { Homepage } from './Homepage';

import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
  Link,
  Outlet,
  useParams,
  NavLink,
  useNavigate,
  useLocation
} from 'react-router-dom';

function App() {
  return (
    <>
    <Router>
        <Header title="eCom" searchBar="true" />
        <Homepage />
        <Routes>
          <Route path="/contact" element={<Contact />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Router>
      <Footer />
    </>
  );
}

export default App;

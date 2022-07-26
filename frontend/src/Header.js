import React from "react";
import PropTypes from 'prop-types';
import { NavLink } from "react-router-dom";
import './Footer';

export const Header = (props) => {
  let logo = {
    color: "red",
    fontWeight: 'bold',
    fontSize: "25px",
  }
  let iconCart = {
    border: "0px solid black"
  }
  return (
    <nav className="navbar navbar-expand-lg bg-dark navbar-dark">
      <div className="container-fluid">
        <NavLink to={"/"} className="navbar-brand" style={logo}>
          {props.title}
        </NavLink>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink to={"/contact"} className="nav-link">
                Contact
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to={"/about"} className="nav-link">
                About
              </NavLink>
            </li>
            <li className="nav-item dropdown">
              <a
                href="#test"
                className="nav-link dropdown-toggle"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                More tools
              </a>
              <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <a href="#test" className="dropdown-item">
                    Action
                  </a>
                </li>
                <li>
                  <a href="#test" className="dropdown-item">
                    Another
                  </a>
                </li>
              </ul>
            </li>
          </ul>
          {props.searchBar ? <form className="d-flex" role="search">
            <input
              className="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button className="btn btn-outline-success" style={iconCart} type="submit">
              Search
            </button>
            <li type="button" className="btn position-relative">
            <i class="fa fa-shopping-cart"></i>
              <span className="position-absolute top-0 translate-middle badge rounded-pill bg-danger">
                99+
                <span className="visually-hidden">unread messages</span>
              </span>
            </li>
          </form> : ""}
        </div>
      </div>
    </nav>
  );
};

Header.defaultProps = {
  searchBar: "true"
}

Header.propType = {
  title: PropTypes.string.isRequired,
  searchBar: PropTypes.bool
}
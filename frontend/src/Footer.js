import React from "react";
import "./footer.css"

export const Footer = () => {
  let footerStyle = {
    position: "fixed",
    bottom: "0px",
    left: "0px",
    right: "0px",
    backgroudColor: "rgba(0, 0, 0, 0.2)",

  }
  return (
    <>
      <div className="footer">

        <div className="bg-light text-light bg-dark b-0 py-0" style={footerStyle}>
          <div className="text-center p-1 py-2">
            <p>© 2020 Copyright <a class="text-light" href="amazon.com">ecom.com</a></p>
          </div>
        </div>
      </div>
    </>
  );
};

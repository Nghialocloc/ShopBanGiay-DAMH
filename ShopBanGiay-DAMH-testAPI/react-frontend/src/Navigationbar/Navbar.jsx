import "./Navbar.css";

const active = () => {
  return "active";
};
var defaultA = true;
var defaultB = false;
const defaultActive = (activate) => {
  if (activate == true) {
    return "active";
  } else {
    return "0";
  }
};

function navBar() {
  return (
    <nav>
      <script
        src="https://kit.fontawesome.com/1147679ae7.js"
        crossOrigin="anonymous"
      />
      <link
        rel="stylesheet"
        href="https://use.fontawesome.com/releases/v5.15.4/css/all.css"
      />
  
      <section id="header">
        <a href="#">
          <img src="#" className="logo" />
        </a>
        <div className="nav-container">
          <li>
            <input
              type="text"
              className="search-input"
              placeholder="Nhập tên/hãng giày cần tìm."
            />
          </li>
        </div>
        <div>
          <ul id="navbar">
            <li>
              <a className="active" href="trangchu.html">
                Home
              </a>
            </li>
            <li>
              <a href="shoping.html">Shopping</a>
            </li>
            <li>
              <a href="blog.html">Blog</a>
            </li>
            <li>
              <a href="about.html">About</a>
            </li>
            <li>
              <a href="contact.html">Contact</a>
            </li>
            <li>
              <a href="cart.html">
                <i className="fa fa-shopping-bag"></i>
              </a>
            </li>
            <li>
              <a href="nguoidung.html">
                <i className="fa fa-user"></i>
              </a>
            </li>
          </ul>
        </div>
      </section>
      {/*icons*/}
    </nav>
  );
}

export default navBar;

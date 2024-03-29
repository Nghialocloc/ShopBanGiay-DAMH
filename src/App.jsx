import Navigationbar from "./Navigationbar/Navbar";
import Productions from "./Productions/Products";
import Recommmened from "./Recommended/Recommmened";
import Sidebar from "./Sidebar/Sidebar";
import Trangchu from "./Pages/Trangchu";
import Cart from "./Pages/Cart";
import About from "./Pages/About";
import Shopping from "./Pages/Shopping";
import Blog from "./Pages/Blog";
import Contact from "./Pages/Contact";
import Details from "./Pages/Details";
import Dashboard from "./Admin/DashBoard";
import { Fragment } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./Pages/LoginPage";
import SignUp from "./Pages/SignUp";

function App() {
  // const [count, setCount] = useState(0)

  return (<>
      {/* <Trangchu /> */}
      {/* <Cart /> */}
      {/* <Shopping /> */}
      {/* <About /> */}
      {/* <Blog /> */}
      {/* <Contact /> */}
      {/* <Details /> */}
      {/* <Dashboard /> */}

       <Router>
        <Fragment>
          <Routes>
            <Route path="" element={<Details />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/signup" element={<SignUp />} />
          </Routes>
        </Fragment>
       </Router>
      </>
  );
}

export default App

// import React, { useState } from "react";
// import axios from "axios";
// import { useNavigate } from "react-router-dom";

// function Login() {
//   const [form, setForm] = useState({ username: "", password: "" });
//   const navigate = useNavigate();

//   const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

//   const handleSubmit = async e => {
//     e.preventDefault();
//     try {
//       const response = await axios.post("http://192.168.100.87:8000/login", new URLSearchParams(form), {
//         headers: { "Content-Type": "application/x-www-form-urlencoded" },
//       });
//       localStorage.setItem("token", response.data.access_token);
//       navigate("/dashboard");
//     } catch (error) {
//       alert("Login failed!");
//     }
//   };

//   return (
//     <div className="container">
//       <h2>Login</h2>
//       <form onSubmit={handleSubmit}>
//         <input type="text" name="username" placeholder="Email" onChange={handleChange} required />
//         <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
//         <button type="submit">Login</button>
//       </form>
//       <p onClick={() => navigate("/signup")}>Don't have an account? Signup</p>
//     </div>
//   );
// }

// export default Login;


import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {
  const [form, setForm] = useState({ username: "", password: "" });
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

const handleSubmit = async e => {
  e.preventDefault();
  try {
    console.log("Sending login request with:", form);

    const response = await axios.post(
      "http://192.168.100.87:8000/login",
      new URLSearchParams(form),
      {
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      }
    );

    console.log("Login response:", response.data);

    const { access_token, user_id } = response.data;

    if (!access_token || !user_id) {
      alert("Login successful but token or user ID missing!");
      return;
    }

    localStorage.setItem("token", access_token);
    localStorage.setItem("user_id", user_id.toString());

    navigate("/dashboard");
  } catch (error) {
    console.error("Login error:", error.response?.data || error.message);
    alert("Login failed!");
  }
};



  return (
    <div className="container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Email"
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
          required
        />
        <button type="submit">Login</button>
      </form>
      <p onClick={() => navigate("/signup")}>Don't have an account? Signup</p>
    </div>
  );
}

export default Login;

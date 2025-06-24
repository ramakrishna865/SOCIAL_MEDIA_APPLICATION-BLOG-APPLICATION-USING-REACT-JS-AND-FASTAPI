
import React, { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
  const [blogs, setBlogs] = useState([]);
  const [userBlogs, setUserBlogs] = useState([]);
  const [showUserBlogs, setShowUserBlogs] = useState(false);
  const [userInfo, setUserInfo] = useState(null);
  const [showProfile, setShowProfile] = useState(false);
  const [newBlog, setNewBlog] = useState({ title: "", body: "" });

  const token = localStorage.getItem("token");
  const userId = localStorage.getItem("user_id");

  useEffect(() => {
    if (!token) return;

    axios
      .get("http://192.168.100.87:8000/blog/", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then(res => setBlogs(res.data))
      .catch(() => alert("Failed to fetch blogs"));

    if (userId) {
      axios
        .get(`http://192.168.100.87:8000/user/${userId}`, {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then(res => {
          setUserInfo(res.data);
          setUserBlogs(res.data.blogs || []);
        })
        .catch(() => alert("Failed to fetch user info"));
    }
  }, [token, userId]);

  const handleCreateBlog = () => {
    axios
      .post("http://192.168.100.87:8000/blog", newBlog, {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then(() => {
        alert("Blog created!");
        window.location.reload();
      })
      .catch(() => alert("Failed to create blog"));
  };

  const handleUpdate = (blogId) => {
    const updated = prompt("Enter updated content:");
    if (!updated) return;

    axios
      .put(
        `http://192.168.100.87:8000/blog/${blogId}`,
        { title: "Updated", body: updated },
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      )
      .then(() => {
        alert("Blog updated");
        window.location.reload();
      })
      .catch(() => alert("Failed to update blog"));
  };

 const handleDelete = (blogId) => {
  console.log("Trying to delete blog with ID:", blogId); // Add this
  if (!window.confirm("Delete this blog?")) return;

  axios
    .delete(`http://192.168.100.87:8000/blog/${blogId}`, {
      headers: { Authorization: `Bearer ${token}` },
    })
    .then(() => {
      alert("Blog deleted");
      window.location.reload();
    })
    .catch(() => alert("Failed to delete blog"));
};


  const containerStyle = {
    padding: "20px",
    backgroundColor: "#f5f5f5",
    minHeight: "100vh",
    position: "relative",
  };

  const gridStyle = {
    display: "flex",
    flexWrap: "wrap",
    gap: "16px",
    justifyContent: "center",
  };

  const cardStyle = {
    backgroundColor: "#fff",
    borderRadius: "12px",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
    padding: "16px",
    width: "300px",
    position: "relative",
  };

  const profileIconStyle = {
    position: "absolute",
    top: "20px",
    right: "20px",
    cursor: "pointer",
    fontSize: "24px",
  };

  const profileBoxStyle = {
    position: "absolute",
    top: "60px",
    right: "20px",
    backgroundColor: "#fff",
    padding: "16px",
    boxShadow: "0 0 10px rgba(0,0,0,0.1)",
    borderRadius: "10px",
    zIndex: 10,
  };

  const renderBlogs = (data, isUser = false) => {
    if (data.length === 0) {
      return isUser ? (
        <div>
          <h4>No blogs yet. Create one!</h4>
          <input
            placeholder="Title"
            onChange={e => setNewBlog({ ...newBlog, title: e.target.value })}
          />
          <textarea
            placeholder="Body"
            onChange={e => setNewBlog({ ...newBlog, body: e.target.value })}
          />
          <button onClick={handleCreateBlog}>Create Blog</button>
        </div>
      ) : (
        <p>No blogs found</p>
      );
    }

    return data.map((blog, i) => (
      <div key={i} style={cardStyle}>
        <h3>{blog.title}</h3>
        <p>{blog.body}</p>
        <small>By: {blog.creator?.name || userInfo?.name}</small>
        {isUser && (
          <div>
            <button onClick={() => handleUpdate(blog.id)}>Update</button>
            <button onClick={() => handleDelete(blog.id)}>Delete</button>
          </div>
        )}
      </div>
    ));
  };

  return (
    <div style={containerStyle}>
      <h2 style={{ textAlign: "center", marginBottom: "20px" }}>
        {showUserBlogs ? "My Blogs" : "All Blogs"}
      </h2>

      <div style={profileIconStyle} onClick={() => setShowProfile(!showProfile)}>
        👤
      </div>

      {showProfile && userInfo && (
        <div style={profileBoxStyle}>
          <p><strong>Name:</strong> {userInfo.name}</p>
          <p><strong>Email:</strong> {userInfo.email}</p>
          <button onClick={() => setShowUserBlogs(true)}>View My Blogs</button>
          <button onClick={() => setShowUserBlogs(false)}>View All Blogs</button>
        </div>
      )}

      <div style={gridStyle}>
        {showUserBlogs ? renderBlogs(userBlogs, true) : renderBlogs(blogs)}
      </div>
    </div>
  );
}

export default Dashboard;

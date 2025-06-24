import React, { useState } from "react";
import { toast, ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'
import axios from "axios";

const App = () => {
  
  <ToastContainer
            position="bottom-right"
            autoClose={3000}
            hideProgressBar={false}
            newestOnTop
            closeOnClick
            pauseOnFocusLoss
            draggable
            pauseOnHover
            theme="dark"
          />
  const [url, seturl] = useState("");
  const [targetprice, settargetprice] = useState("");
  const [email, setEmail] = useState("");
  const [productPreview, setProductPreview] = useState(null);
  const [success, setsuccess] = useState(false);

  const cleanedUrl = url.trim();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!url || !targetprice || !email) {
      toast.error("Please fill in all fields.");
      return;
    }

    try {

      const prevRes = await axios.get("http://127.0.0.1:5000/api/track/preview", {
        params: {url: cleanedUrl}
      });

      setProductPreview(prevRes.data);

      const res = await axios.post("http://127.0.0.1:5000/api/track/", {
        url: cleanedUrl,
        target_price : targetprice,
        email: email
      });

      if (res.status === 200) {
        setsuccess(true);
        toast.success("Product is being tracked successfully!");
        seturl("");
        setTargetprice("");
        setEmail("");
      }
    } catch (error) {
        toast.error(error.response?.data?.error || error.message || "Error tracking product");
        toast.error("Failed to track product. Please check the inputs or try again.");
}

  }


  return (
    <div className="min-h-screen bg-gray-100 font-poppins">
      <header className="bg-white shadow">
        <div className="max-w-6xl mx-auto py-4 px-6">
          <span className="text-2xl font-bold text-rose-600">TrendTicker</span>
        </div>
      </header>
      <main className="max-w-4xl mx-auto mt-10 flex flex-col md:flex-row gap-8 px-4">
        <section className="bg-white rounded-lg shadow p-8 flex-1">
          <h1 className="text-xl font-semibold mb-6 text-gray-800">
            Track product price
          </h1>
          <form className="space-y-5" onSubmit={handleSubmit}>
            <div>
              <label className="block text-sm font-medium text-rose-400 mb-1">
                Product URL
              </label>
              <input
                type="text"
                placeholder="Enter product URL"
                className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-rose-400"
                onChange={(e) => seturl(e.target.value)}
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-rose-400 mb-1">
                Target Price
              </label>
              <input
                type="text"
                placeholder="Enter target price"
                className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-rose-400"
                onChange={(e) => settargetprice(e.target.value)}
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-rose-400 mb-1">
                Your Email
              </label>
              <input
                type="email"
                placeholder="Enter your email"
                className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-rose-400"
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <button
              type="submit"
              className="w-full bg-rose-500 text-white font-semibold py-2 rounded hover:bg-rose-800 transition cursor-pointer"
            >
              Track Now
            </button>
          </form>
        </section>
        <section className="bg-white rounded-lg shadow p-8 flex-1">
          <h1 className="text-xl font-semibold mb-6 text-gray-800">
            Live product preview
          </h1>
          {productPreview ?(
          <div className="flex flex-col items-center">
            <img
              src={productPreview ? productPreview.image : "https://via.placeholder.com/150"}
              alt="Product Preview"
              className="rounded mb-4 border"
              style={{ width: "180px", height: "180px", objectFit: "contain" }}
            />
            <h2 className="text-lg font-medium mb-2">{productPreview.title}</h2>
            <p className="text-gray-700 mb-1">
              Current Price:{" "}
              <span className="font-semibold text-rose-400">₹{productPreview.price}</span>
            </p>
            <p className="text-gray-700 mb-1">
              Target Price:{" "}
              <span className="font-semibold text-rose-400">₹{targetprice}</span>
            </p>
            { success ?
            <p className="text-green-600 font-semibold">Status: Tracking</p> :
            <p className="text-red-600 font-semibold">Status: Not Tracking</p>
            }
          </div>
          ) :
            <p className="text-gray-400 text-center">No preview available yet.</p>}
        </section>
      </main>
    </div>
  );
};

export default App;

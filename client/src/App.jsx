import React from "react";

const App = () => {
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
          <form className="space-y-5">
            <div>
              <label className="block text-sm font-medium text-rose-400 mb-1">
                Product URL
              </label>
              <input
                type="text"
                placeholder="Enter product URL"
                className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-rose-400"
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
              />
            </div>
            <button
              type="submit"
              className="w-full bg-rose-500 text-white font-semibold py-2 rounded hover:bg-rose-800 transition"
            >
              Track Now
            </button>
          </form>
        </section>
        <section className="bg-white rounded-lg shadow p-8 flex-1">
          <h1 className="text-xl font-semibold mb-6 text-gray-800">
            Live product preview
          </h1>
          <div className="flex flex-col items-center">
            <img
              src="https://via.placeholder.com/150"
              alt="Product Preview"
              className="rounded mb-4 border"
            />
            <h2 className="text-lg font-medium mb-2">Product Name</h2>
            <p className="text-gray-700 mb-1">
              Current Price:{" "}
              <span className="font-semibold text-rose-400">₹100</span>
            </p>
            <p className="text-gray-700 mb-1">
              Target Price:{" "}
              <span className="font-semibold text-rose-400">₹80</span>
            </p>
            <p className="text-green-600 font-semibold">Status: Tracking</p>
          </div>
        </section>
      </main>
    </div>
  );
};

export default App;

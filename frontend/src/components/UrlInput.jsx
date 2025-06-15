import React from "react";
const UrlInput = ({url_input, setUrlInput}) => {

    const handleChange = (e) => {
        setUrlInput(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Submitted URL:", url_input);
        // Add your submission logic here
    };
    return (
    <form onSubmit={handleSubmit} className="w-full max-w-md mx-auto p-4">
        <div className="flex items-center gap-2">
            <input
            type="text"
            value={url_input}
            onChange={handleChange}
            placeholder="Enter your URL here"
            className="text-white flex-grow px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
            type="submit"
            className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
            >
                Shorten
            </button>
        </div>
    </form>
        );
};

export default UrlInput;
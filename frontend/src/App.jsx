import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UrlInput from './components/UrlInput.jsx'

function App() {
  const [url_input, setUrlInput] = useState("")
  return (
    <main>
      <div className='bg-custom-hero absolute inset-0 bg-cover bg-center'>
      <div class="bg-custom-hero-overlay"></div>
      <div className='wrapper z-10 relative justify-center items-center flex flex-col h-screen'>
        <div className='text-center mb-8'>
          <h1 className='text-white'>Turn Long URLs Into Quick, Clickable Links</h1>
        </div>
          <UrlInput url_input={url_input} setUrlInput={setUrlInput}/>
        </div>
        </div>
    </main>
  )
}

export default App

import { useEffect, useState } from 'react'

function App() {
  const [message, setMessage] = useState('Loading...')
  const [healthStatus, setHealthStatus] = useState('Checking...')

  useEffect(() => {
    // Fetch backend message
    fetch('/api/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage('Failed to connect to backend'))

    // Check backend health
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setHealthStatus(data.status))
      .catch(() => setHealthStatus('unhealthy'))
  }, [])

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <h1 className="text-4xl font-bold mb-4">Based Agent</h1>
      <div className="bg-white p-6 rounded-lg shadow-md">
        <p className="text-lg mb-2">Backend Status: {healthStatus}</p>
        <p className="text-lg">Message: {message}</p>
      </div>
    </div>
  )
}

export default App

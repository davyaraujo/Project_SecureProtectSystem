import { useState, useEffect} from 'react'
import EventCard from './EventCard'

function App() {
  const [events, setEvents] = useState([])
  useEffect(() => {
    fetch('http://localhost:8000/events/')
      .then(res => res.json())
      .then(data => setEvents(data))
    const ws = new WebSocket('ws://localhost:8000/ws/live')
    ws.onmessage = (message) => {
      const newEvent = JSON.parse(message.data)
      setEvents(prev => [newEvent , ...prev])
    }
    return () => ws.close()
  }, [])

  const totalAlertas = events.filter(e => e.is_alert).length

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      
      <header className="p-6 flex items-center justify-center gap-4">
        <img src="/securevision.png" alt="securevision" className="h-48 w-3xl" />
        <h1 className="text-3xl font-bold text-center">
        </h1>
      </header>

      <div className="max-w-3xl mx-auto p-2">

        <div className="grid grid-cols-2 gap-5 mb-6">
          <div className="bg-gray-800 rounded-xl p-4 text-center">
            <p className="text-gray-400 text-sm">Total de Eventos</p>
            <p className="text-4xl font-bold">{events.length}</p>
          </div>
          <div className="bg-red-900 rounded-xl p-4 text-center">
            <p className="text-red-300 text-sm">Alertas</p>
            <p className="text-4xl font-bold text-red-400">{totalAlertas}</p>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-6">
          {events.map(event => (
            <EventCard key={event.id} event={event} />
          ))}
        </div>

      </div>
    </div>
  )   
}

export default App
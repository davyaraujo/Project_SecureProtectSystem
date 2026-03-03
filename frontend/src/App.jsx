import { useState, useEffect} from 'react'
import EventCard from './EventCard'
import './App.css'

function App() {
  const [events, setEvents] = useState([])
  useEffect(() => {
    fetch('http://localhost:8000/events/')
      .then(res => res.json())
      .then(data => setEvents(data))
  }, [])

  return (
    <div>
      <h1>SecureVision Dashboard</h1>
      <p>Total de eventos: {events.length}</p>
      <div>
        {events.map(events => (
          <EventCard key={events.id} events={events} />
        ))}
      </div>
    </div>
  )
}

export default App
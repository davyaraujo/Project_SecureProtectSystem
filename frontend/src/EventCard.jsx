function EventCard({ event }) {
  if (!event) return null

  return (
    <div className={`rounded-xl p-4 border ${
      event.is_alert 
        ? 'bg-red-950 border-red-700' 
        : 'bg-gray-800 border-gray-700'
    }`}>
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-bold capitalize">{event.object_detect}</h3>
        <span className={`text-sm px-3 py-1 rounded-full ${
          event.is_alert 
            ? 'bg-red-700 text-red-100' 
            : 'bg-green-800 text-green-100'
        }`}>
          {event.is_alert ? '🚨 Alerta' : '✅ Normal'}
        </span>
      </div>
      <div className="mt-2 text-gray-400 text-sm flex justify-between">
        <span>Confiança: {(event.confidence * 100).toFixed(0)}%</span>
        <span>{new Date(event.created_at).toLocaleString()}</span>
      </div>
    </div>
  )
}

export default EventCard
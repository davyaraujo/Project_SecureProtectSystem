function EventCard({events}){
    return(
        <div style ={{
            border: '1px solid #000000',
            borderRadius: '100px',
            padding: '8px',
            margin: '8px',
            backgroundColor: events.is_alert ? '#c70906' : '#0af034'        
        }}>
            <h3>{events.object_detect}</h3>
            <p>Confiança: {events.confidence}</p>
            <p>Alerta: {events.is_alert ? '🚨 Sim' : '✅ Não'}</p>
            <p>Data: {new Date(events.created_at).toLocaleString()}</p>
        </div>
    )
}   

export default EventCard
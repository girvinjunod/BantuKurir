const AnakJawaban = ({ pengiriman }) => {
    return (
        <div>
            <h3>Pengiriman {pengiriman.id + 1}</h3>
            <h4>Jalur Terpendek</h4>
            <p>{pengiriman.jalur}</p>
            <h4>Jarak Terpendek</h4>
            <p>{pengiriman.jarak}</p>
            <h4>Estimasi Waktu</h4>
            <p>{pengiriman.estimasi}</p><br/>
            <p></p>
        </div>
    )
}

export default AnakJawaban
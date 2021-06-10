const AnakJawaban = ({ pengiriman }) => {
    return (
        <div>
                <h3>Jalur yang Ditempuh Kurir</h3>
                <p>Jalur: {pengiriman.jalur}</p><br/>
                <h3>Waktu Pengiriman</h3>
                <p>Waktu (HH:MM:SS): {pengiriman.waktu}</p><br/>
                <h3>Estimasi Waktu Pengiriman Selesai</h3>
                <p>Estimasi (HH:MM:SS): {pengiriman.estimasi}</p><br/>
                <h3>Jarak yang Ditempuh</h3>
                <p>Jarak: {pengiriman.cost} km</p>
        </div>
    )
}

export default AnakJawaban
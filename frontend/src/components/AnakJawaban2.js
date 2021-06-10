const AnakJawaban2 = ({ pengiriman }) => {
    return (
        <>
            <h3>Pengiriman {pengiriman.id + 1}</h3>
            <h4>Jalur yang Ditempuh Kurir</h4>
            <p>Jalur: {pengiriman.jalur}</p><br/>
            <h4>Waktu Pengiriman</h4>
            <p>Waktu (HH:MM:SS): {pengiriman.waktu}</p><br/>
            <h4>Estimasi Waktu Pengiriman Selesai</h4>
            <p>Estimasi (HH:MM:SS): {pengiriman.estimasi}</p><br/>
            <h4>Jarak yang Ditempuh</h4>
            <p>Jarak: {pengiriman.cost} km</p><br/>
        </>
    )
}

export default AnakJawaban2
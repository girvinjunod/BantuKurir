const Jawaban2 = ({jawaban}) => {
    if (jawaban.found){
        return (
            <div>
                <h2>Hasil Pencarian</h2>
                <h3>Jalur yang Ditempuh Kurir</h3>
                <p>Jalur: {jawaban.jalur}</p><br/>
                <h3>Waktu Pengiriman</h3>
                <p>Waktu (HH:MM:SS): {jawaban.waktu}</p><br/>
                <h3>Estimasi Waktu Pengiriman Selesai</h3>
                <p>Estimasi (HH:MM:SS): {jawaban.estimasi}</p><br/>
                <h3>Jarak yang Ditempuh</h3>
                <p>Jarak: {jawaban.cost} km</p>
            </div>
        )
    }
    else{
        return (
            <div>
                <h2>Hasil Pencarian</h2>
                <p>{jawaban.msg}</p>
            </div>
        )
    }


}

export default Jawaban2
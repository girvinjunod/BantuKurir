import Lokasi from "./Lokasi.js";

const Lokasi2 = ({ lokasi, onDelete }) => {
    return (
        <>
          <h4>Lokasi-lokasi Pengiriman</h4>
          { lokasi.map((s)=> (
          <Lokasi key = {s.id} lokasi = {s} onDelete = {onDelete} />)) } 
          <br/>
        </>
    )
}

export default Lokasi2

import Syarat from "./Syarat.js";

const Soal = ({ syarat, onDelete }) => {
    return (
        <>
          <h3>Sistem Kekongruenan Linear</h3>
          { syarat.map((s)=> (
          <Syarat key = {s.id} syarat = {s} onDelete = {onDelete} />)) } 
        </>
    )
}

export default Soal

import AnakJawaban from "./AnakJawaban.js";

const Jawaban = ({ jawaban }) => {
    let ajalur = jawaban.jalur
    let ajarak = jawaban.jarak
    let aestimasi = jawaban.estimasi
    let agraf = jawaban.graf
    let aobj = []
    for (let i = 0; i< ajalur.length; i++){
        aobj[i] = {id: i, jalur: ajalur[i], jarak: ajarak[i], estimasi: aestimasi[i], graf:agraf[i] }
    }
    return (
        <>
        <br/>
        <br/>
          <h3>Solusi TSP</h3>
          { aobj.map((s)=> (
          <AnakJawaban key = {s.id} pengiriman= {s} />)) } 
        </>
    )
}

export default Jawaban

import AnakJawaban2 from "./AnakJawaban.js";
const Jawaban2 = ({jawaban}) => {
    if (jawaban.found){
        //"jalur": ajalur, "waktu": awaktu, "estimasi": aestimasi, "cost": acost
        let ajalur = jawaban.jalur
        let awaktu = jawaban.waktu
        let aestimasi = jawaban.estimasi
        let acost = jawaban.cost
        let aobj = []
        for (let i = 0; i< ajalur.length; i++){
            aobj[i] = {id: i, jalur: ajalur[i], jarak: awaktu[i], estimasi: aestimasi[i], cost:acost[i] }
        }
            return (
                <>
                <br/>
                <br/>
                <h2>Hasil Pencarian</h2>
                  { aobj.map((s)=> (
                  <AnakJawaban2 key = {s.id} pengiriman= {s} />)) } 
                </>
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
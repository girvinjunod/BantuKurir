import Button from "./Button";

const GetJawaban = ({titikasal, koordinat,identitas, waktu, kecepatan, onSubmit}) => {
    const onClick = () =>{
        if (titikasal.length === 0 || koordinat.length === 0 || identitas.length === 0 || waktu.length === 0 || kecepatan.length === 0){
            alert("Input Kosong");
            return;
        }
        let namalokasi = []
        let koorlokasi = []
        
        //titik asal
        namalokasi[0] = "Perusahaan"
        koorlokasi[0] = [titikasal[0]["x"], titikasal[0]["y"]]

        //lokasi tujuan
        let n = koordinat.length
        for (let i = 0; i < n;i ++){
            namalokasi[i+1] = koordinat[i]["lokasi"]
            koorlokasi[i+1] = [koordinat[i]["x"], koordinat[i]["y"]]
        }

        let identity = identitas[0]
        let time = waktu[0]
        let velo = kecepatan[0]

        onSubmit([namalokasi],[koorlokasi],[identity.nama], [time.time], [velo.kecepatan]);
    };
    return (
            <Button onClick = {onClick} text="Cari Jalur Terpendek"/>
    )
}

export default GetJawaban

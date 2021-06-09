const Jawaban = ({jawaban}) => {
    let question = jawaban.pertanyaan.split('\n').map(i => {
        return <p>{i}</p>
    });
    let teksmodulus = () =>{
        var str = "m = ";
        if (jawaban.pembagi.length === 1) return str +=jawaban.pembagi[0];
        for (let i = 0;i < jawaban.pembagi.length; i++){
            str += jawaban.pembagi[i];
            if (i !== jawaban.pembagi.length -1){
                str += " * ";
            }
        }
        str += " = " + jawaban.modulus;
        return str;
    }
    let teksM = () => {
        var str = "";
        let n = jawaban.pembagi.length;
        if (n === 1){
            str += "M1 = 1";
            return str;
        }
        let M = [];
        for (let i = 0; i < n;i++){
            M[i] = [];
            for (let j = 0; j < n;j++){
                if (j !== i){
                    M[i].push(jawaban.pembagi[j]);
                }
            }
        }
        for (let i = 0; i < M.length;i++){
            str += "M" + (i+1)+ " = ";
            for (let j = 0; j < M[i].length;j++){
                str += M[i][j];
                if (j !== M[i].length - 1){
                    str += " * ";
                }
                else{
                    str += " = " + jawaban.M[i];
                }
            }
            if (i !== M.length - 1) str += ", ";
        }
        return str;
    }

    let teksY = () => {
        var str = "";
        let n = jawaban.pembagi.length;
        for (let i = 0; i < n;i++){
            str += "y" + (i+1) + " = " + jawaban.y[i] + " karena " + jawaban.M[i] + " * " + jawaban.y[i] + " ≡ 1 (mod " + jawaban.pembagi[i] + ")\n";
        }
        return str;
    }
    let y = teksY().split('\n').map(i => {
        return <p>{i}</p>
    });

    let teksAkhir = () => {
        var str = "x = ";
        let n = jawaban.pembagi.length;
        for (let i = 0; i < n;i++){
            str += jawaban.sisa[i] + " * " + jawaban.M[i] + " * " + jawaban.y[i];
            if (i !== n-1){
                str += " + ";
            }
        }
        str += " = " + jawaban.hasil;
        return str;
    }
    if (jawaban.ada){
        return (
            <div>
                <br/>
                <h3>Pertanyaan:</h3>
                {question}
                <p>Berapakah nilai x?</p>
                <br/>
                <h3>Rumus:</h3>
                <p>CRT mengatakan bahwa untuk m1,m2,...,mn bilangan bulat positif 
                    dan semuanya saling koprima, terdapat solusi unik untuk sistem kekongruenan linear di atas
                    dalam modulus m = m1 * m2 * ... * mn
                </p>
                <br/>
                <p>Solusi umum sistem kekongruenan linear= <br/>
                x = a1M1y1 + a2M2y2 + ... + anMnyn</p><br/>
                <p>mk = Kekongruenan ke-k dalam sistem kekongruenan linear</p>
                <p>Mk = perkalian semua modulus kecuali mk</p>
                <p>yk = balikan Mk dalam modulus mk</p>
                <p>ak = sisa untuk kekongruenan k</p><br/>
                <h3>Langkah-langkah:</h3>
                <p>Cek untuk syarat CRT:</p>
                <p>Semua pembagi harus saling koprima = {jawaban.ada ? "True" : "False"}</p><br/>
                <p>{teksmodulus()}</p>
                <p>{teksM()}</p>
                {y}
                <p>Maka solusi unik dari sistem kekongruenan tersebut adalah</p>
                <p>{teksAkhir()}</p><br/>
                <h3>Jawaban:</h3>
                <p>{jawaban.ans}</p>
    
            </div>
        )
    }
    else {
        return (
            <div>
                <br/>
                <h3>Pertanyaan:</h3>
                {question}
                <p>Berapakah nilai x?</p>
                <br/>
                <h3>Rumus:</h3>
                <p>CRT mengatakan bahwa untuk m1,m2,...,mn bilangan bulat positif 
                    dan semuanya saling koprima, terdapat solusi unik untuk sistem kekongruenan linear di atas
                    dalam modulus m = m1 * m2 * ... * mn
                </p>
                <br/>
                <p>Solusi umum sistem kekongruenan linear= <br/>
                x = a1M1y1 + a2M2y2 + ... + anMnyn</p><br/>
                <p>mk = Kekongruenan ke-k dalam sistem kekongruenan linear</p>
                <p>Mk = perkalian semua modulus kecuali mk</p>
                <p>yk = balikan Mk dalam modulus mk</p>
                <p>ak = sisa untuk kekongruenan k</p><br/>
                <h3>Langkah-langkah:</h3>
                <p>Cek untuk syarat CRT:</p>
                <p>Semua pembagi harus saling koprima = {jawaban.ada ? "True" : "False"}</p><br/>
                <p>Tidak memenuhi syarat CRT</p><br/>
                <h3>Jawaban:</h3>
                <p>{jawaban.ans}</p>
    
            </div>
        )
    }

}

export default Jawaban

import random
from datetime import datetime

nombre = "BUBUBUBUBU"

html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Para {nombre} ❤️</title>

<style>
body {{
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
}}

/* 🔥 IMAGE ROW */
.image-row {{
    position: fixed;
    top: 20px;
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 20px;
    z-index: 0;
}}

.image-row img {{
    width: 120px;
    height: 120px;
    object-fit: cover;
    opacity: 0.25;
    border-radius: 10px;
    transition: transform 0.3s ease;
}}

/* slight rotation */
.image-row img:nth-child(1) {{ transform: rotate(-10deg); }}
.image-row img:nth-child(2) {{ transform: rotate(8deg); }}
.image-row img:nth-child(3) {{ transform: rotate(-6deg); }}
.image-row img:nth-child(4) {{ transform: rotate(10deg); }}
.image-row img:nth-child(5) {{ transform: rotate(-8deg); }}
.image-row img:nth-child(6) {{ transform: rotate(6deg); }}

/* hover */
.image-row img:hover {{
    transform: scale(1.1) rotate(0deg);
    opacity: 0.4;
}}

/* 💌 CARD */
.container {{
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}}

.card {{
    background: white;
    padding: 40px;
    max-width: 600px;
    
    border: 4px solid black;
    border-radius: 25px;
    
    box-shadow: 8px 8px 0px black;
    
    animation: fadeIn 1.5s ease-in-out;
}}

h1 {{
    text-align: center;
    color: #ff4d6d;
}}

p {{
    font-size: 18px;
    line-height: 1.6;
    color: #333;
    white-space: pre-line;
}}

@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
</style>

</head>

<body>

<!-- 🔥 IMAGE LINE -->
<div class="image-row">
    <img src="src1.jpeg">
    <img src="src2.jpeg">
    <img src="src3.jpeg">
    <img src="src4.jpeg">
    <img src="src5.jpeg">
    <img src="src6.jpeg">
</div>

<!-- 💌 CARD -->
<div class="container">
    <div class="card">
        <h1>Para {nombre} ❤️</h1>
        <p id="carta"></p>
        <p style="text-align:right;">{datetime.now().strftime('%d/%m/%Y')}</p>
    </div>
</div>

<!-- ✨ RANDOM TEXT SCRIPT -->
<script>
const nombre = "{nombre}";

const aperturas = [
    `Muchas gracias por llegar a mi vida, ${nombre}, por hacerme sentir bien y disfrutar cada momento contigo.`,
    `${nombre}, tu sabes que a mi me encantas, incluso cuando dices cosas raras jajaja.`,
    `Cada instante contigo, ${nombre}, se siente como un sueño del que no quiero despertar.`
];

const cuerpo = [
    "Tu sonrisa siempre me da ganas de reir, asuhaushuashu (Me HAPPY).",
    "Jamas me faltaron momentos especiales. µ.o",
    "Aprecio cada momento que tengo contigo obviamente 7.7"
];

const cierres = [
    "Te quiero un montonoonononononono bibibi",
    "💕💖💕💕💖💕💕💖💕💕💖💕",
    "Quiero seguir construyendo momentos contigo o tambien tener momentos vergonzosos, no me quejo sjjsjsjs"
];

const despedidas = [
    "Con todo mi corazon 3.3",
    "De parte de eu eu eu",
    "Y bueno ya sabes quien hizo esto 😏"
];

function random(arr) {{
    return arr[Math.floor(Math.random() * arr.length)];
}}

const texto = `
${{random(aperturas)}}

${{random(cuerpo)}} ${{random(cuerpo)}}

${{random(cierres)}}

${{random(despedidas)}}
`;

document.getElementById("carta").innerText = texto;
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("❤️ Carta generada: abre 'index.html'")
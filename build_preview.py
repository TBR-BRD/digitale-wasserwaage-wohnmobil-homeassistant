import pathlib
card = pathlib.Path("womo-level-card.js").read_text()
html = f"""<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Womo Wasserwaage – Vorschau</title>
<style>
  :root {{ --primary-text-color:#212121; --secondary-text-color:#727272; --primary-color:#03a9f4;
          --card-bg:#fff; --page-bg:#f2f2f6; }}
  body.dark {{ --primary-text-color:#e1e1e1; --secondary-text-color:#9b9b9b; --card-bg:#1c1c1c; --page-bg:#111; }}
  body {{ margin:0; background:var(--page-bg); font-family: -apple-system, Roboto, "Segoe UI", sans-serif;
         color:var(--primary-text-color); }}
  .wrap {{ max-width:420px; margin:0 auto; padding:16px; }}
  ha-card {{ display:block; background:var(--card-bg); border-radius:12px; box-shadow:0 1px 4px rgba(0,0,0,.12); }}
  .ctrl {{ background:var(--card-bg); border-radius:12px; padding:12px 14px; margin-bottom:14px; font-size:14px; }}
  .ctrl label {{ display:flex; align-items:center; gap:10px; margin:6px 0; }}
  .ctrl input[type=range] {{ flex:1; }}
  .ctrl output {{ width:52px; text-align:right; font-variant-numeric: tabular-nums; }}
  .ctrl .row {{ display:flex; gap:8px; flex-wrap:wrap; margin-top:8px; }}
  .ctrl button {{ border:1px solid #ccc; background:transparent; color:inherit; border-radius:6px; padding:5px 9px; font:inherit; font-size:13px; cursor:pointer; }}
  h1 {{ font-size:15px; margin:0 0 6px; }}
</style></head>
<body>
<div class="wrap">
  <div class="ctrl">
    <h1>Vorschau mit Testwerten</h1>
    <label>Längs <input id="p" type="range" min="-4" max="4" step="0.1" value="-0.6"><output id="po"></output></label>
    <label>Quer <input id="r" type="range" min="-4" max="4" step="0.1" value="1.1"><output id="ro"></output></label>
    <div class="row">
      <button data-p="0" data-r="0">Waagerecht</button>
      <button data-p="-0.6" data-r="1.1">Typischer Stellplatz</button>
      <button data-p="2.5" data-r="-3">Zu steil</button>
      <button id="dark">Hell/Dunkel</button>
    </div>
  </div>
  <womo-level-card id="card"></womo-level-card>
</div>
<script>
customElements.define("ha-card", class extends HTMLElement {{}});
{card}
const card = document.getElementById("card");
card.setConfig({{ pitch_entity:"sensor.p", roll_entity:"sensor.r", title:"Benimar Tessoro 488", wheelbase:395, track:170 }});
const p = document.getElementById("p"), r = document.getElementById("r");
function upd() {{
  document.getElementById("po").textContent = Number(p.value).toFixed(1) + "°";
  document.getElementById("ro").textContent = Number(r.value).toFixed(1) + "°";
  card.hass = {{ states: {{ "sensor.p": {{state:p.value}}, "sensor.r": {{state:r.value}} }} }};
}}
p.oninput = r.oninput = upd;
document.querySelectorAll("button[data-p]").forEach(b => b.onclick = () => {{ p.value=b.dataset.p; r.value=b.dataset.r; upd(); }});
document.getElementById("dark").onclick = () => document.body.classList.toggle("dark");
upd();
</script>
</body></html>"""
pathlib.Path("vorschau.html").write_text(html)

"""Baut simulator/index.html aus simulator/template.html und womo-level-card.js."""
import pathlib
root = pathlib.Path(__file__).parent
card = (root / "womo-level-card.js").read_text()
tpl = (root / "simulator" / "template.html").read_text()
(root / "simulator" / "index.html").write_text(tpl.replace("/*CARD*/", card))
print("simulator/index.html gebaut")

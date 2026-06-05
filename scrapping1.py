import requests
from bs4 import BeautifulSoup

url="https://datosabiertos.bogota.gov.co/"

respuesta=requests.get(url)
html=respuesta.text

soup=BeautifulSoup(html, 'html.parser')

# Seleccionar cada tarjeta temática (col-md-3)
cols = soup.select("div.col-md-3")
if not cols:
	print("No se encontraron elementos 'col-md-3'.")
else:
	for i, col in enumerate(cols, 1):
		title_el = col.select_one("h3.media-heading a")
		img_el = col.select_one("a.module-image img")
		href_el = col.select_one("a.module-image")
		title = title_el.get_text(strip=True) if title_el else None
		href = href_el["href"] if href_el and href_el.has_attr("href") else None
		img = img_el["src"] if img_el and img_el.has_attr("src") else None
		print(f"{i}.", title, "|", href, "|", img)

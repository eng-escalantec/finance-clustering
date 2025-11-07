"""
download_prices.py
------------------

Este script descarga precios históricos de varias acciones desde Yahoo Finance
y guarda un archivo CSV con los precios de cierre ajustados.

Flujo del script:
1. Define una lista de *tickers* (símbolos de acciones) y un rango de fechas.
2. Usa `yfinance` para descargar los datos diarios, con `auto_adjust=True`
   para que los precios estén corregidos por dividendos y splits.
3. Extrae únicamente la columna 'Close' del conjunto descargado,
   que contiene los precios de cierre ajustados.
4. Crea la carpeta `data/raw/` si no existe y guarda el archivo CSV allí.
5. Imprime información básica de validación:
   - Ruta del archivo guardado
   - Dimensión del DataFrame (filas, columnas)
   - Primeras filas
   - Rango de fechas y conteo de valores nulos

Resultado:
  Un archivo llamado `adj_close_2020_2025.csv` en la ruta `data/raw/`
  con los precios ajustados de 10 acciones (AAPL, MSFT, NVDA, etc.)
  desde 2020 hasta el último día de 2024.
"""

import pandas as pd
import yfinance as yf
from pathlib import Path

p = Path ('data/raw/adj_close_2020_2025.csv')

TICKERS = ["AAPL", "MSFT", "NVDA", "AMZN", "TSLA", "META", "GOOGL", "JPM", "XOM", "KO"]
START = "2020-01-01"
END = "2025-01-01"

df = yf.download(TICKERS, start=START, end=END, auto_adjust=True)


close = df['Close']   # toma el nivel 'Close' del MultiIndex


p.parent.mkdir(parents=True, exist_ok=True)

close.to_csv(p, index=True)
print(f"Guardado {p.resolve()} con forma {close.shape}")

print(close.head(3))
print("Fechas:", close.index.min(), "→", close.index.max())
print("Nulos totales:", close.isna().sum().sum())

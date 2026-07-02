import numpy as np
import pandas as pd
import requests

IMF_BASE_URL = "https://www.imf.org/external/datamapper/api/v1/"


def get_imf_indicator(indicator_code: str, col_name: str) -> pd.DataFrame | None:
    """Descarga un indicador de la IMF DataMapper API y lo devuelve en formato largo."""
    url = f"{IMF_BASE_URL}/{indicator_code}"
    response = requests.get(url, timeout=30)

    if response.status_code != 200:
        print(f"Error {response.status_code} para {indicator_code}")
        return None

    values = response.json().get("values", {}).get(indicator_code, {})

    rows = [
        {"geo": country, "year": int(year), col_name: float(value)}
        for country, year_data in values.items()
        for year, value in year_data.items()
    ]
    return pd.DataFrame(rows)


def normalize_robust(series: pd.Series, v_min: float, v_max: float) -> pd.Series:
    """Normaliza una serie a escala 0-100 usando umbrales fijos con significado
    económico, en vez de min-max sobre los datos observados."""
    clipped = series.clip(lower=v_min, upper=v_max)
    return (clipped - v_min) / (v_max - v_min) * 100


def classify_solvency_dynamics(row: pd.Series) -> str | float:
    """Clasifica la dinámica fiscal de un país-año: Saludable, En recuperación,
    En deterioro o Crítico."""
    cols = ["deficit_pct_gdp", "gdp_growth_pct"]
    if any(pd.isna(row[col]) for col in cols):
        return np.nan

    impulso_neto = row["gdp_growth_pct"] + row["deficit_pct_gdp"]
    saldo = row["gdp_growth_pct"]

    if impulso_neto > 0:
        return "Saludable" if saldo >= 0 else "En recuperación"
    else:
        return "En deterioro" if saldo >= 0 else "Crítico"

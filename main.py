from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

EXCEL_PATH = "E:\VSCodeProjects\mt93-backend\productos.xlsx"

@app.get("/api/products/by-barcode/{barcode}")
def get_product(barcode: str):
    try:
        df = pd.read_excel(EXCEL_PATH)

        product = df[df["barcode"].astype(str) == barcode]

        if product.empty:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        row = product.iloc[0]

        return {
            "id": str(row["id"]),
            "barcode": str(row["barcode"]),
            "name": str(row["name"]),
            "price": str(row["price"]),
            "stock": str(row["stock"])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, get_db

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Shopping API")



# CATEGORY APIs
# ==========================

@app.get("/categories", response_model=list[schemas.Category])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@app.get(
    "/categories/{category_id}/products",
    response_model=list[schemas.Product]
)
def get_products_by_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_products_by_category(category_id, db)



# PRODUCT APIs
# ==========================

@app.post("/products", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(product, db)


@app.get("/products", response_model=list[schemas.Product])
def get_all_products(
    db: Session = Depends(get_db)
):
    return crud.get_all_products(db)


@app.get("/products/{product_id}", response_model=schemas.Product)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_product(product_id, db)


@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.update_product(
        product_id,
        product,
        db
    )


@app.patch("/products/{product_id}", response_model=schemas.Product)
def patch_product(
    product_id: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):
    return crud.patch_product(
        product_id,
        product,
        db
    )


@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_product(
        product_id,
        db
    )
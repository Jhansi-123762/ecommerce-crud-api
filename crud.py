from sqlalchemy.orm import Session
from fastapi import HTTPException

import models
import schemas



# CATEGORY CRUD
# ==========================

def get_categories(db: Session):
    return db.query(models.Category).all()


def get_products_by_category(category_id: int, db: Session):

    category = db.query(models.Category).filter(
        models.Category.id == category_id
    ).first()

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return db.query(models.Product).filter(
        models.Product.category_id == category_id
    ).all()



# PRODUCT CRUD
# ==========================

def create_product(product: schemas.ProductCreate, db: Session):

    category = db.query(models.Category).filter(
        models.Category.id == product.category_id
    ).first()

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    new_product = models.Product(
        name=product.name,
        category_id=product.category_id,
        price=product.price,
        quantity=product.quantity
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


def get_all_products(db: Session):

    return db.query(models.Product).all()


def get_product(product_id: int, db: Session):

    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


def update_product(product_id: int,
                   product: schemas.ProductCreate,
                   db: Session):

    db_product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    category = db.query(models.Category).filter(
        models.Category.id == product.category_id
    ).first()

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    db_product.name = product.name
    db_product.category_id = product.category_id
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
    db.refresh(db_product)

    return db_product


def patch_product(product_id: int,
                  product: schemas.ProductUpdate,
                  db: Session):

    db_product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    update_data = product.model_dump(exclude_unset=True)

    if "category_id" in update_data:

        category = db.query(models.Category).filter(
            models.Category.id == update_data["category_id"]
        ).first()

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(product_id: int, db: Session):

    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }
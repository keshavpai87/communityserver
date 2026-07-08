from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

def get_db() :
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    # db.query()

    count = db.query(database_models.Product).count
    print(count)
    if(count == 0):
        for product in products :
            db.add(database_models.Product(**product.model_dump()))
    db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)) :
    db_products = db.query(database_models.Product).all()
    print(db_products)
    return db_products

# greet()

# GET - Get the data as per the request by the user
@app.get("/productbyid/{id}")
def get_product_by_id(id : int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product Not Found"

# POST - Insert a new record
@app.post("/products")
def add_product(product : Product, db : Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

# PUT - Update an existing record
@app.put("/products/{id}")
def update_product(id: int, product : Product, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product :
        db_product.name = product.name
        db_product.description = product.description
        db_product.quantity = product.quantity
        db_product.price = product.price
        db.commit()
        return "Product with id {} updated successfully".format(db_product.id)
    else :
        return "Product Not Found"

@app.delete("/products/{id}")
def delete_product(id : int, db : Session = Depends(get_db)) :
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product :
        db.delete(db_product)
        db.commit()
        return "Product Deleted Successfully"
    else :
        return "Product Not Found"
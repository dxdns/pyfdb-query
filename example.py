import pyfdb_query as lib

def get_products():
    config = lib.Config(dir="/tmp/database.fdb")
    db = lib.Open(config)
    
    return db.Table("products").Columns((
        "product_id",
        "barcode",
        "description",
        "stock",
        "value"
    )).Limit(2).OrderBy("product_id DESC").all()

def main():
    products = get_products()
    print(products)
    
if __name__ == "__main__":
    main()
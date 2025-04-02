import sqlite3

conn = sqlite3.connect('baza.db')
cursor = conn.cursor()


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     price REAL CHECK(price > 0),
#     stock INTEGER DEFAULT 0 CHECK(stock > 0)
# )
# """)

# conn.commit()


# CRUD
# create
# read
# update
# delete

def add_product(name, price, stock, cursor, conn):
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))

    conn.commit()

def get_products(cursor):
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return products

def update_price(product_id, new_price, cursor, conn):
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()

def delete_product(product_id, cursor, conn):
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()


add_product(
    name='Mouse',
    price=21,
    stock=3,
    cursor=cursor,
    conn=conn
)

print(type((12)))
print(type((12,)))

for product in get_products(cursor=cursor):
    print(product)

update_price(3, 12, cursor=cursor, conn=conn)
delete_product(4, cursor=cursor, conn=conn)
conn.close()
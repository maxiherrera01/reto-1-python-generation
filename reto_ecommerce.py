productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "categoria": "Computo", "precio": 25000, "descuento": 0.1},
    {"id": 2, "nombre": "Mouse Gamer X", "categoria": "Accesorios", "precio": 1200, "descuento": 0.15},
    {"id": 3, "nombre": "Teclado Mecánico K1", "categoria": "Accesorios", "precio": 3500, "descuento": 0.05},
    {"id": 4, "nombre": "Monitor 27’‘ 4K", "categoria": "Computo", "precio": 18000, "descuento": 0.2},
    {"id": 5, "nombre": "Audífonos Bluetooth Z", "categoria": "Audio", "precio": 8000, "descuento": 0.1}
]

ventas = [
    {"venta_id": 101, "producto_id": 1, "cantidad": 1, "cliente": "Ana"},
    {"venta_id": 102, "producto_id": 2, "cantidad": 2, "cliente": "Luis"},
    {"venta_id": 103, "producto_id": 4, "cantidad": 1, "cliente": "Sophia"},
    {"venta_id": 104, "producto_id": 3, "cantidad": 1, "cliente": "Marco"},
    {"venta_id": 105, "producto_id": 5, "cantidad": 3, "cliente": "Andrés"}
]

tienda_info = ("TechieStore", "Santiago", 2025)

# 
nombre_tienda = tienda_info[0]
ciudad = tienda_info[1]
año = tienda_info[2]

print(f"bienvenido a {nombre_tienda}" en {ciudad} {año})
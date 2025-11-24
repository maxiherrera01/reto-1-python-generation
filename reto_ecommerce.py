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

#  MENSAJE DE BIENVENIDA

nombre_tienda = tienda_info[0]
ciudad = tienda_info[1]
año = tienda_info[2]

print(f"bienvenido a {nombre_tienda} en {ciudad} {año}")

# MOSTRAR CUANTOS PRODUCTOS EXISTEN

total_productos = len(productos)

print("Total de productos:", total_productos)

# Objetivo 3: Precio final con descuento (sin loops)

# Producto 1
precio1 = productos[0]["precio"]
descuento1 = productos[0]["descuento"]
precio_final1 = precio1 - (precio1 * descuento1)
print(productos[0]["nombre"], "→ $", precio_final1)

# Producto 2
precio2 = productos[1]["precio"]
descuento2 = productos[1]["descuento"]
precio_final2 = precio2 - (precio2 * descuento2)
print(productos[1]["nombre"], "→ $", precio_final2)

# Producto 3
precio3 = productos[2]["precio"]
descuento3 = productos[2]["descuento"]
precio_final3 = precio3 - (precio3 * descuento3)
print(productos[2]["nombre"], "→ $", precio_final3)

# Producto 4
precio4 = productos[3]["precio"]
descuento4 = productos[3]["descuento"]
precio_final4 = precio4 - (precio4 * descuento4)
print(productos[3]["nombre"], "→ $", precio_final4)

# Producto 5
precio5 = productos[4]["precio"]
descuento5 = productos[4]["descuento"]
precio_final5 = precio5 - (precio5 * descuento5)
print(productos[4]["nombre"], "→ $", precio_final5)

# Objetivo 4: Total de cada venta (sin loops)

# Venta 101
venta_101 = ventas[0]
producto_101 = productos[venta_101["producto_id"] - 1]
total_venta_101 = precio_final1 * venta_101["cantidad"]
print(f"Venta {venta_101['venta_id']}: {venta_101['cliente']} compró {venta_101['cantidad']} {producto_101['nombre']} y pagó {total_venta_101}")

# Venta 102
venta_102 = ventas[1]
producto_102 = productos[venta_102["producto_id"] - 1]
total_venta_102 = precio_final2 * venta_102["cantidad"]
print(f"Venta {venta_102['venta_id']}: {venta_102['cliente']} compró {venta_102['cantidad']} {producto_102['nombre']} y pagó {total_venta_102}")

# Venta 103
venta_103 = ventas[2]
producto_103 = productos[venta_103["producto_id"] - 1]
total_venta_103 = precio_final4 * venta_103["cantidad"]
print(f"Venta {venta_103['venta_id']}: {venta_103['cliente']} compró {venta_103['cantidad']} {producto_103['nombre']} y pagó {total_venta_103}")

# Venta 104
venta_104 = ventas[3]
producto_104 = productos[venta_104["producto_id"] - 1]
total_venta_104 = precio_final3 * venta_104["cantidad"]
print(f"Venta {venta_104['venta_id']}: {venta_104['cliente']} compró {venta_104['cantidad']} {producto_104['nombre']} y pagó {total_venta_104}")

# Venta 105
venta_105 = ventas[4]
producto_105 = productos[venta_105["producto_id"] - 1]
total_venta_105 = precio_final5 * venta_105["cantidad"]
print(f"Venta {venta_105['venta_id']}: {venta_105['cliente']} compró {venta_105['cantidad']} {producto_105['nombre']} y pagó {total_venta_105}")


# Objetivo 5: Ingreso total de la tienda
ingreso_total = (
    total_venta_101 +
    total_venta_102 +
    total_venta_103 +
    total_venta_104 +
    total_venta_105
)

print("Ingreso total de la tienda:", ingreso_total)


CREATE DATABASE IF NOT EXISTS ferreteria_casa_clavo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ferreteria_casa_clavo;

CREATE TABLE IF NOT EXISTS proveedores (
  id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL, contacto VARCHAR(80) NOT NULL,
  telefono VARCHAR(10) NOT NULL, correo VARCHAR(120) NOT NULL UNIQUE,
  producto VARCHAR(100) NOT NULL, activo BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS clientes (
  id_cliente INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(80) NOT NULL, cedula VARCHAR(10) NOT NULL UNIQUE,
  telefono VARCHAR(10) NOT NULL, correo VARCHAR(120) NOT NULL UNIQUE,
  activo BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS productos (
  id_producto INT AUTO_INCREMENT PRIMARY KEY,
  codigo VARCHAR(10) NOT NULL UNIQUE, nombre VARCHAR(80) NOT NULL,
  categoria VARCHAR(30) NOT NULL, precio DECIMAL(10,2) NOT NULL,
  stock INT NOT NULL, descripcion VARCHAR(200) NOT NULL, id_proveedor INT NOT NULL,
  CONSTRAINT chk_producto_precio CHECK (precio > 0),
  CONSTRAINT chk_producto_stock CHECK (stock >= 0),
  CONSTRAINT fk_producto_proveedor FOREIGN KEY (id_proveedor)
    REFERENCES proveedores(id_proveedor) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS facturas (
  id_factura INT AUTO_INCREMENT PRIMARY KEY,
  numero VARCHAR(15) NOT NULL UNIQUE, id_cliente INT NOT NULL,
  fecha DATE NOT NULL, total DECIMAL(10,2) NOT NULL,
  estado ENUM('Pendiente', 'Pagada') NOT NULL DEFAULT 'Pendiente',
  CONSTRAINT chk_factura_total CHECK (total > 0),
  CONSTRAINT fk_factura_cliente FOREIGN KEY (id_cliente)
    REFERENCES clientes(id_cliente) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

INSERT IGNORE INTO proveedores (id_proveedor, nombre, contacto, telefono, correo, producto, activo) VALUES
(1, 'Distribuidora Andina', 'Luis Andrade', '0988888100', 'ventas@andina.com', 'Herramientas', TRUE),
(2, 'Materiales Oriente', 'Paola Silva', '0988889200', 'ventas@oriente.com', 'Materiales de construcción', TRUE),
(3, 'Fijaciones Ecuador', 'José Molina', '0993344556', 'ventas@fijaciones.com', 'Tornillos y pernos', TRUE);

INSERT IGNORE INTO clientes (id_cliente, nombre, cedula, telefono, correo, activo) VALUES
(1, 'María López', '1600123456', '0987654321', 'maria@example.com', TRUE),
(2, 'Carlos Pérez', '1600234567', '0991234567', 'carlos@example.com', TRUE),
(3, 'Ana Torres', '1600345678', '0974567890', 'ana@example.com', FALSE);

INSERT IGNORE INTO productos (codigo, nombre, categoria, precio, stock, descripcion, id_proveedor) VALUES
('HER-001', 'Martillo de uña', 'Herramientas', 12.50, 18, 'Martillo resistente con mango ergonómico.', 1),
('FIJ-001', 'Caja de clavos', 'Fijaciones', 6.75, 35, 'Caja de clavos galvanizados para madera.', 3),
('MAT-001', 'Cemento 50 kg', 'Materiales', 9.90, 24, 'Saco de cemento para trabajos de construcción.', 2);

INSERT IGNORE INTO facturas (numero, id_cliente, fecha, total, estado) VALUES
('F-001', 1, '2026-08-10', 104.25, 'Pagada'),
('F-002', 2, '2026-08-12', 31.05, 'Pendiente');

// JavaScript general del proyecto.
document.addEventListener("DOMContentLoaded", () => {
  // Año automático en elementos que lo requieran en futuras ampliaciones.
  console.log("Ferretería La Casa del Clavo - aplicación Flask cargada correctamente.");

  // Filtro sencillo del módulo Productos.
  const buscador = document.getElementById("buscarProducto");
  const tabla = document.getElementById("tablaProductos");

  if (buscador && tabla) {
    buscador.addEventListener("input", () => {
      const texto = buscador.value.toLowerCase().trim();
      const filas = tabla.querySelectorAll("tbody tr");

      filas.forEach((fila) => {
        fila.style.display = fila.textContent.toLowerCase().includes(texto) ? "" : "none";
      });
    });
  }
});

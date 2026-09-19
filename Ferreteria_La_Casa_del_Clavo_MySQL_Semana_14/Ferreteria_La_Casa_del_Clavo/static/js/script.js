function mostrarMensaje(nombreProducto) {
    alert("Producto seleccionado: " + nombreProducto);
}

function confirmarEliminacion(nombreProducto) {
    return window.confirm("¿Está seguro de eliminar el producto " + nombreProducto + "?");
}

document.addEventListener("DOMContentLoaded", function () {
    console.log("Sistema Ferretería La Casa del Clavo cargado correctamente.");
});

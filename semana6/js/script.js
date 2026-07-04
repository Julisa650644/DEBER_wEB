// Productos iniciales por categoría
const productos = {
  herramientas: ["Taladro eléctrico", "Sierra circular", "Nivel de burbuja"],
  fijaciones: ["Pernos de acero", "Arandelas", "Anclajes de pared"],
  materiales: ["Cemento rápido", "Yeso en polvo", "Tubos de PVC"]
};

// ----------------------
// Catálogo dinámico
// ----------------------
function mostrarCategoria(nombre, items) {
  const columna = document.createElement("div");
  columna.className = "col-md-4 mb-3";

  const card = document.createElement("div");
  card.className = "card h-100";

  const body = document.createElement("div");
  body.className = "card-body";

  const titulo = document.createElement("h5");
  titulo.className = "card-title text-center";
  titulo.textContent = nombre.charAt(0).toUpperCase() + nombre.slice(1);

  const lista = document.createElement("ul");
  lista.className = "list-group list-group-flush";

  items.forEach(item => {
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.textContent = item;
    lista.appendChild(li);
  });

  body.appendChild(titulo);
  card.appendChild(body);
  card.appendChild(lista);
  columna.appendChild(card);

  document.getElementById("lista-productos").appendChild(columna);
}

function cargarCatalogo(categoria) {
  const lista = document.getElementById("lista-productos");
  lista.innerHTML = "";
  if (categoria === "todos") {
    for (let cat in productos) {
      mostrarCategoria(cat, productos[cat]);
    }
  } else {
    mostrarCategoria(categoria, productos[categoria]);
  }
}

// Inicializar mostrando todos
cargarCatalogo("todos");

// Evento del filtro
document.getElementById("filtro").addEventListener("change", function() {
  cargarCatalogo(this.value);
});

// ----------------------
// Formulario de compras
// ----------------------
let totalCompras = 0;

const cliente = document.getElementById("cliente");
const categoriaCompra = document.getElementById("categoria-compra");
const productoSelect = document.getElementById("producto");
const cantidad = document.getElementById("cantidad");
const precio = document.getElementById("precio");

const feedbackCliente = document.getElementById("feedback-cliente");
const feedbackCategoriaCompra = document.getElementById("feedback-categoria-compra");
const feedbackProducto = document.getElementById("feedback-producto");
const feedbackCantidad = document.getElementById("feedback-cantidad");
const feedbackPrecio = document.getElementById("feedback-precio");

// Al cambiar categoría, cargar productos en el select
categoriaCompra.addEventListener("change", () => {
  const cat = categoriaCompra.value;
  productoSelect.innerHTML = '<option value="">Seleccione un producto</option>';
  if (cat && productos[cat]) {
    productos[cat].forEach(p => {
      const option = document.createElement("option");
      option.value = p;
      option.textContent = p;
      productoSelect.appendChild(option);
    });
  }
});

// Validaciones dinámicas
cliente.addEventListener("input", () => {
  if (cliente.value.trim().length >= 3) {
    cliente.classList.add("is-valid");
    cliente.classList.remove("is-invalid");
    feedbackCliente.textContent = "Nombre válido ✔";
    feedbackCliente.className = "text-success";
  } else {
    cliente.classList.add("is-invalid");
    cliente.classList.remove("is-valid");
    feedbackCliente.textContent = "Debe tener al menos 3 caracteres";
    feedbackCliente.className = "text-danger";
  }
});

categoriaCompra.addEventListener("blur", () => {
  if (categoriaCompra.value !== "") {
    categoriaCompra.classList.add("is-valid");
    categoriaCompra.classList.remove("is-invalid");
    feedbackCategoriaCompra.textContent = "Categoría seleccionada ✔";
    feedbackCategoriaCompra.className = "text-success";
  } else {
    categoriaCompra.classList.add("is-invalid");
    categoriaCompra.classList.remove("is-valid");
    feedbackCategoriaCompra.textContent = "Debe seleccionar una categoría";
    feedbackCategoriaCompra.className = "text-danger";
  }
});

productoSelect.addEventListener("blur", () => {
  if (productoSelect.value !== "") {
    productoSelect.classList.add("is-valid");
    productoSelect.classList.remove("is-invalid");
    feedbackProducto.textContent = "Producto seleccionado ✔";
    feedbackProducto.className = "text-success";
  } else {
    productoSelect.classList.add("is-invalid");
    productoSelect.classList.remove("is-valid");
    feedbackProducto.textContent = "Debe seleccionar un producto";
    feedbackProducto.className = "text-danger";
  }
});

cantidad.addEventListener("input", () => {
  if (parseInt(cantidad.value) > 0) {
    cantidad.classList.add("is-valid");
    cantidad.classList.remove("is-invalid");
    feedbackCantidad.textContent = "Cantidad válida ✔";
    feedbackCantidad.className = "text-success";
  } else {
    cantidad.classList.add("is-invalid");
    cantidad.classList.remove("is-valid");
    feedbackCantidad.textContent = "Debe ser mayor a 0";
    feedbackCantidad.className = "text-danger";
  }
});

precio.addEventListener("input", () => {
  if (parseFloat(precio.value) > 0) {
    precio.classList.add("is-valid");
    precio.classList.remove("is-invalid");
    feedbackPrecio.textContent = "Precio válido ✔";
    feedbackPrecio.className = "text-success";
  } else {
    precio.classList.add("is-invalid");
    precio.classList.remove("is-valid");
    feedbackPrecio.textContent = "Debe ser mayor a 0";
    feedbackPrecio.className = "text-danger";
  }
});

// Registrar compra
document.getElementById("form-compra").addEventListener("submit", function(e) {
  e.preventDefault();

  const clienteVal = cliente.value.trim();
  const productoVal = productoSelect.value;
  const cantidadVal = cantidad.value.trim();
  const precioVal = precio.value.trim();

  if (!clienteVal || !productoVal || !cantidadVal || !precioVal) {
    mostrarMensaje("Todos los campos son obligatorios", "danger");
    return;
  }

  const total = (parseFloat(cantidadVal) * parseFloat(precioVal)).toFixed(2);

  const li = document.createElement("li");
  li.className = "list-group-item d-flex justify-content-between align-items-center";
  li.textContent = `${clienteVal} compró ${cantidadVal} ${productoVal}(s) - Total: $${total}`;

  const btnEliminar = document.createElement("button");
  btnEliminar.className = "btn btn-sm btn-danger ms-2";
  btnEliminar.textContent = "Eliminar";
  btnEliminar.addEventListener("click", function() {
    li.remove();
    totalCompras--;
    actualizarTotal();
    mostrarMensaje("Compra eliminada", "warning");
  });

  li.appendChild(btnEliminar);
  document.getElementById("lista-compras").appendChild(li);

  totalCompras++;
  actualizarTotal();
  mostrarMensaje("Compra registrada correctamente", "success");
  this.reset();
  productoSelect.innerHTML = '<option value="">Seleccione un producto</option>';
});

function mostrarMensaje(texto, tipo) {
  const contenedor = document.createElement("div");
  contenedor.className = `alert alert-${tipo} mt-2`;
  contenedor.textContent = texto;
  document.getElementById("mensajes").appendChild(contenedor);
  setTimeout(() => contenedor.remove(), 3000);
}

function actualizarTotal() {
  document.getElementById("total").textContent = "Total de compras registradas: " + totalCompras;
}

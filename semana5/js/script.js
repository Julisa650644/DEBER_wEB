// Productos iniciales
const productos = {
  herramientas: ["Taladro eléctrico", "Sierra circular", "Nivel de burbuja"],
  fijaciones: ["Pernos de acero", "Arandelas", "Anclajes de pared"],
  materiales: ["Cemento rápido", "Yeso en polvo", "Tubos de PVC"]
};

// Mostrar productos según categoría
document.getElementById("filtro").addEventListener("change", function() {
  const categoria = this.value;
  const lista = document.getElementById("lista-productos");
  lista.innerHTML = "";

  if (categoria === "todos") {
    for (let cat in productos) {
      mostrarCategoria(cat, productos[cat]);
    }
  } else {
    mostrarCategoria(categoria, productos[categoria]);
  }
});

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

// Inicializar mostrando todos
document.getElementById("filtro").value = "todos";
document.getElementById("filtro").dispatchEvent(new Event("change"));

// Formulario de compras
let totalCompras = 0;

document.getElementById("form-compra").addEventListener("submit", function(e) {
  e.preventDefault();

  const cliente = document.getElementById("cliente").value.trim();
  const producto = document.getElementById("producto").value.trim();
  const cantidad = document.getElementById("cantidad").value.trim();
  const precio = document.getElementById("precio").value.trim();

  if (!cliente || !producto || !cantidad || !precio) {
    mostrarMensaje("Todos los campos son obligatorios", "danger");
    return;
  }

  const total = (parseFloat(cantidad) * parseFloat(precio)).toFixed(2);

  const li = document.createElement("li");
  li.className = "list-group-item d-flex justify-content-between align-items-center";
  li.textContent = `${cliente} compró ${cantidad} ${producto}(s) - Total: $${total}`;

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

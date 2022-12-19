<template>
  <!-- Isaac chinchilla 192063 -->
  <div id="app">
    <div class="barra">BODEGUITA FLORES EIREL</div>
    <h2>Realizar compra</h2>
    <div class="espcacioCliente">
      <label for="">Cliente: </label>
      <input type="text" placeholder="ingrese nombre cliente" /><br />
      <label for="">Correo: </label>
      <input type="text" placeholder="ingrese tu correo" /><br />
      <hr />
    </div>
    <div class="centro">
      <table>
        <tr>
          <th>Imagen</th>
          <th>nombre</th>
          <th>precio</th>
          <th>cantidad</th>
          <th>sub total</th>
          <th>Eliminar</th>
        </tr>

        <ProductosVender :pro="productos"> hermosa </ProductosVender>
      </table>
    </div>
  </div>
</template>

<script>
import ProductosVender from "@/components/ProductosVender.vue";
export default {
  name: "App",
  components: {
    ProductosVender,
  },
  data() {
    return {
      total: 0,
      productos: [
        {
          imagen:
            "https://www.pcware.com.co/wp-content/uploads/2018/05/portatil-lenovo-v310-i3_portatil-lenovo-v310-i3_lenovo-v310.jpg",
          nombre: "LENOVO",
          precio: 4000,
        },
        {
          imagen:
            "https://www.pcware.com.co/wp-content/uploads/2018/05/portatil-lenovo-v310-i3_portatil-lenovo-v310-i3_lenovo-v310.jpg",
          nombre: "LENOVO",
          precio: 4000,
        },
        {
          imagen:
            "https://www.pcware.com.co/wp-content/uploads/2018/05/portatil-lenovo-v310-i3_portatil-lenovo-v310-i3_lenovo-v310.jpg",
          nombre: "LENOVO",
          precio: 4000,
        },
      ],
    };
  },
  methods: {
    eliminarProdutco(index) {
      return this.productos.splice(index, 1);
    },
  },
  computed: {},
};
</script>

<style lang="scss">
* {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
}
.espcacioCliente {
  text-align: center;
}
hr {
  margin: 20px 100px;
}
.espcacioCliente > input {
  width: 60%;
}
.espcacioCliente input,
label {
  margin: 10px;
}
table {
  text-align: center;
  margin: auto;
}
tr,
table {
  border-top: 1px solid gray;
  border-bottom: 1px solid gray;
  padding: 5px 15px;
  // border-collapse: collapse;
}

td,
th {
  padding: 0 10px;
}
.centro {
  display: flex;
}
#app {
  .barra {
    color: white;
    background-color: rgb(56, 50, 50);
    padding: 10px 0;
  }
  h2 {
    text-align: center;
  }
}
img {
  width: 25px;
}
</style>

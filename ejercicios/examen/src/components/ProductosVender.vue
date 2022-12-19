<template>
  <tbody>
    <tr v-for="(prod, index) in pro" :key="index">
      <td><img :src="prod.imagen" /></td>
      <td>{{ prod.nombre }}</td>
      <td>{{ prod.precio }}</td>
      <td><input type="text" v-model="cantidad" /></td>
      <td>{{ calcularSubTotal(prod.precio) }}</td>
      <td>
        <img
          class="im"
          src="https://img.freepik.com/iconos-gratis/x-simbolo_318-1407.jpg"
          alt=""
        />
      </td>
      <br />
    </tr>
    <div class="lin">
      <tr>
        <span>{{ subTotal }} </span>
      </tr>
      <tr>
        <td>Sub total</td>
      </tr>
      <tr>
        <td>Sub total</td>
      </tr>
    </div>
  </tbody>
</template>

<script>
export default {
  name: "ProductosVender",
  props: {
    pro: Array,
  },
  data() {
    return {
      cantidad: 1,
      total: 0,
      subTotal: 0,
    };
  },
  methods: {
    calcularSubTotal(index) {
      this.subTotal = this.cantidad * index;
      return this.cantidad * index;
    },
    SubTotal(index) {
      //   return this.cantidad * calcularSubTotal(index);
    },
  },
  computed: {},
};
</script>

<style scoped>
tr > td > img {
  width: 60px;
}
.im {
  width: 20px;
}
td {
  border-top: 1px solid gray;
}
</style>

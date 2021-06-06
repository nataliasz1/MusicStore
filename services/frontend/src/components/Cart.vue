<template>
  <div class="cart-container">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-row no-gutters>
      <b-col md="9">
        <CartItem v-for="product in products" :key="product.slug" v-bind:product="product"></CartItem>
      </b-col>
      <b-col md="3">
        <p class="h3">Do zapłaty: {{ totalPrice }} PLN</p>
        <b-button variant="primary">Kupuję i płacę</b-button>
      </b-col>
    </b-row>
  </div>
</template>
<script>
import CartItem from "@/components/CartItem";
import axios from "axios";

export default {
  name: "Cart",
  components: {CartItem},
  data: function () {
    return {
      breadcrumbs: [
        {
          text: 'Home',
          to: '/'
        },
        {
          text: 'Koszyk',
          href: '#'
        }],
      products: [],
      totalPrice: 0
    }
  },
  mounted() {
    axios.get('/api/basket/basket/').then(
        response => {
          this.products = response.data;
          console.log(response.data);
          this.totalPrice = 0;
          for (var product in this.products) {
            this.totalPrice += product.price;
          }
        }
    )
  }
}
</script>
<style scoped>
.cart-container {
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 16px;
  text-align: right;
}
</style>

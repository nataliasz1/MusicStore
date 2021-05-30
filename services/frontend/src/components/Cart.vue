<template>
  <div class="cartContainer">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-row no-gutters>
      <b-col md="9">
        <CartItem v-for="index in 5" :key="index"></CartItem>
      </b-col>
      <b-col md="3">
        <p class="h3">Do zapłaty: {{ 999.99 * 5 }} PLN</p>
        <b-button variant="primary">Kupuję i płacę</b-button>
      </b-col>
    </b-row>
<!--    <b-jumbotron lead="Twój koszyk jest pusty">-->
<!--      <p>pls kup coś</p>-->
<!--    </b-jumbotron>-->
  </div>
</template>

<script>
import CartItem from "@/components/CartItem";
export default {
name: "Cart",
  components: {CartItem},
  data: function () {
    return {
      breadcrumbs: [
        {
          text: 'Home',
          href: '#'
        },
        {
          text: 'Koszyk',
          href: '#'
        }]
    }
  }
}
</script>

<style scoped>
.cartContainer {
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 16px;
  text-align: right;
}
</style>

<template>
  <div class="order-container">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-card
        bg-variant="light"
        class="mb-3"
        style="object-fit: cover">
      <b-row no-gutters>
        <b-col md="4">
          <h4 class="mb-0">Numer zamówienia</h4>
          <p>{{ order.order_id }}</p>
        </b-col>
        <b-col md="4">
          <h4 class="mb-0">Status zamówienia</h4>
          <p>{{ order.status }}</p>
        </b-col>
        <b-col md="4">
          <h4 class="mb-0">Wartość zamówienia</h4>
          <p>{{ order.total_amount }}</p>
        </b-col>
      </b-row>
      <b-row no-gutters>
        <b-col md="12">
          <h4 align="left" class="mt-4">Produkty z zamówienia:</h4>
          <OrderItem v-for="orderItem in order.order_items" :key="orderItem.order_item_id" v-bind:orderItem="orderItem"></OrderItem>
          <p align="left" v-if="order.order_items.length == 0">brak</p>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";
import OrderItem from "@/components/OrderItem";

export default {
name: "Order",
  components: {OrderItem},
  data: function () {
    return {
      breadcrumbs: [
        {
          text: 'Home',
          to: '/'
        },
        {
          text: 'Profil',
          to: '/profile'
        },
        {
          text: 'Zamówienie',
          href: '#'
        }],
      order: null
    }
  },
  mounted() {
    axios.get('/api/order/orders/' + this.$route.params.id + "/").then(
        response => {
          this.order = response.data;
          console.log(this.order);
          console.log(this.order.order_items);
        }
    )
  }
}
</script>

<style scoped>
.order-container {
  margin-top: 16px;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}
</style>

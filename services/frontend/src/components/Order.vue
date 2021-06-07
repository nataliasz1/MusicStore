<template>
  <div class="order-container">
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
          tu lista produktow
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
name: "Order",
  data: function (){
    return {
      order: null
    }
  },
  mounted() {
    axios.get('/api/order/orders/' + this.$route.params.id).then(
        response => {
          this.order = response.data;
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

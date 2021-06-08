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
          <p>{{ order.total_amount }} PLN</p>
        </b-col>
      </b-row>
      <b-row no-gutters>
        <b-col md="12">
          <b-button variant="primary" class="float-right" @click="$router.push('/order/'+order.order_id)">Szczegóły</b-button>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
export default {
name: "OrderBox",
props: ['order']
}
</script>

<style scoped>

</style>

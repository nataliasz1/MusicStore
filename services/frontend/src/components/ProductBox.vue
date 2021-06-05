<template>
  <div class="shadow product-card">
    <b-card
        bg-variant="light"
        :title="product.name"
        img-src="https://via.placeholder.com/500"
        img-bottom
        img-height="300px"
        style="max-width: 384px; height: 100%;">
      <b-card-text>{{ product.price }} PLN</b-card-text>
      <b-button variant="primary" @click="$router.push('product/' + product.slug)">Sprawdź</b-button>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "ProductBox",
  props: ['product']
}
</script>

<style scoped>
.product-card {
  /*width: 100%;*/
  /*height: 100%;*/
  /*max-width: 400px;*/
  /*max-height: 400px;*/
  margin: 8px;
}
</style>

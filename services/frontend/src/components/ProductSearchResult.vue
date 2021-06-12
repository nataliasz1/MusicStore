<template>
  <div class="result-container">
    <b-card
        bg-variant="light"
        class="mb-3"
        style="object-fit: cover">
      <b-row no-gutters>
        <b-col md="3">
          <b-card-img src="https://via.placeholder.com/500"></b-card-img>
        </b-col>
        <b-col md="9">
          <b-card-body :title="product.name" class="text-right">
            <p>{{product.description}}</p>
            <b-card-text right class="text-primary">
              <b-card-text class="h3">{{ product.price }}</b-card-text>
              <b-button variant="primary" @click="$router.push('/product/' + product.catalog_item_id)">Sprawdź</b-button>
            </b-card-text>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>
<script>
export default {
  name: "ProductSearchResult",
  props: ['product']
}
</script>

<style scoped>

</style>

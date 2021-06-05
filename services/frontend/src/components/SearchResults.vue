<template>
  <b-container fluid class="search-container">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-row no-gutters>
      <b-col xl="3">
        <b-card bg-variant="light" class="search-filter-container text-left">
          <p class="h3 mb-4">Filtry</p>
          <b-form-checkbox v-for="index in 10" :key="index" class="mt-1">Jakaś opcja</b-form-checkbox>
          <b-button variant="primary" class="mt-3">Filtruj</b-button>
        </b-card>
      </b-col>
      <b-col xl="9">
        <div class="result-container">
          <ProductSearchResult v-for="index in 10" :key="index"></ProductSearchResult>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import ProductSearchResult from "@/components/ProductSearchResult";

export default {
  name: "SearchResults",
  components: {ProductSearchResult},
  data: function () {
    return {
      breadcrumbs: [
        {
          text: 'Home',
          to: '/'
        },
        {
          text: 'Kategoria',
          href: '#'
        }]
    }
  }
}
</script>

<style scoped>
.search-container {
  max-width: 1400px;
  margin-top: 16px;
  margin-left: auto;
  margin-right: auto;
}

.search-filter-container {
  height: calc(100% - 16px);
}

.result-container {
  margin-left: 8px;
  margin-bottom: 8px;
}
</style>

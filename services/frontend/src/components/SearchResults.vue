<template>
  <b-container fluid class="searchContainer">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-row no-gutters>
      <b-col xl="3">
        <b-card bg-variant="light" class="searchFilterContainer text-left">
          <p class="h3 mb-4">Filtry</p>
            <b-form-checkbox v-for="index in 10" :key="index" class="mt-1">Jakaś opcja</b-form-checkbox>
            <b-button variant="primary" class="mt-3">Filtruj</b-button>
        </b-card>
      </b-col>
      <b-col xl="9">
        <div class="resultContainer"><ProductSearchResult v-for="index in 10" :key="index"></ProductSearchResult></div>
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
          href: '#'
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
  .searchContainer {
    max-width: 1400px;
    margin-top: 16px;
    margin-left: auto;
    margin-right: auto;
  }
  .searchFilterContainer {
    height: calc(100% - 16px);
  }
  .resultContainer {
    margin-left: 8px;
    margin-bottom: 8px;
  }
</style>

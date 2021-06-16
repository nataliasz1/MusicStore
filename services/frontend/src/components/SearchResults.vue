<template>
  <b-container fluid class="search-container">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-row no-gutters>
      <b-col xl="3">
        <b-card bg-variant="light" class="search-filter-container text-left">
          <p class="h3 mb-4">Filtry</p>
          <p class="mb-0">Nazwa:</p>
          <b-form-input class="mb-2" v-model="name"></b-form-input>
          <p class="mb-0">Kategoria:</p>
          <b-form-select class="mb-2" v-model="category" :options="categories"></b-form-select>
          <p class="mb-0">Cena od:</p>
          <b-form-input class="mb-2" type="number" v-model="priceMin"></b-form-input>
          <p class="mb-0">Cena do:</p>
          <b-form-input class="mb-2" type="number" v-model="priceMax"></b-form-input>
          <p class="mb-0">Opinie:</p>
          <b-form-rating variant="primary" no-border inline class="opinion-avg-rating" v-model="opinion"></b-form-rating><br>
          <b-button variant="primary" class="mt-3" @click="fetchData">Filtruj</b-button>
        </b-card>
      </b-col>
      <b-col xl="9">
        <div class="result-container">
          <div v-if="loading">
            <h5 primary>WCZYTYWANIE DANYCH</h5>
            <b-spinner style="width: 3rem; height: 3rem;" variant="primary"></b-spinner>
          </div>
          <ProductSearchResult v-for="product in products" :key="product.catalog_item_id" v-bind:product="product"></ProductSearchResult>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import ProductSearchResult from "@/components/ProductSearchResult";
import axios from "axios";

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
          text: 'Wyszukiwanie',
          href: '#'
        }
        ],
      products: null,
      loading: true,
      categories: [],
      category: null,
      name: null,
      priceMin: 0,
      priceMax: null,
      opinion: 0
    }
  },
  methods: {
    fetchData: function (){
      this.loading = true;
      this.products = [];
      let url = "/api/catalog/products/?";
      if(this.name != null){
        url += "name="+this.name+"&";
      }
      if(this.category != null){
        url += "category="+this.category+"&";
      }
      if(this.priceMax != null){
        url += "max_price="+this.priceMax+"&";
      }
      if(this.priceMin !== 0){
        url += "min_price="+this.priceMin+"&";
      }
      if(this.opinion !== 0){
        url += "stars="+this.opinion+"&";
      }
      url = url.slice(0, -1);
      console.log(url);
      axios.get(url).then(
          response => {
            this.products = response.data;
            console.log(response.data);
            this.loading = false;
          }
      )
    }
  },
  mounted() {
    if(this.$route.query.name){
      this.name = this.$route.query.name;
    }
    if(this.$route.query.category){
      this.category = this.$route.query.category;
    }
    this.fetchData();
    axios.get('/api/catalog/categories/').then(
        response => {
          this.categories.push({value: null,  text: "Dowolna"});
          for(let cat of response.data){
            this.categories.push({value: cat.id, text: cat.name})
          }
          console.log(response.data)
          console.log(this.categories);
        }
    )
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
.opinion-avg-rating {
  background: #F8F9FA;
}
</style>

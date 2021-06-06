<template>
  <div class="home-container">
    <div class="deal-container">
      <b-jumbotron class="daily-deal-banner" text-variant="white" border-variant="dark">
        <template #header>Okazja dnia</template>
        <template #lead>Śmieszny ksylofon</template>
        <template #default>Kliknij, by sprawdzić ></template>
      </b-jumbotron>
    </div>
    <p class="text-left ml-2 h2">Promowane produkty</p>
    <div class="products-container">
      <ProductBox v-for="product in products" :key="product.catalog_item_id" v-bind:product="product"></ProductBox>
    </div>
  </div>
</template>

<script>
import ProductBox from "@/components/ProductBox";
import axios from "axios";

export default {
  name: "Home",
  components: {ProductBox},
  data: function () {
    return {
      products: []
    }
  },
  mounted() {
    axios.get('/api/catalog/').then(
        response => {
          this.products = response.data;
          console.log(response.data)
        }
    )
  }
}
</script>

<style scoped>
.home-container {
  max-width: 1600px;
  margin-right: auto;
  margin-left: auto;
  margin-top: 16px;
}

.deal-container {
  padding: 8px;
}

.products-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.daily-deal-banner {
  background-image: url("../assets/banner.png");
  background-size: cover;
  background-position: right;
  min-height: 400px;
  text-align: left;
  text-shadow: 5px 5px 5px #000000;
}
</style>

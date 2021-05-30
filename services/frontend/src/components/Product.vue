<template>
  <b-container fluid class="product-container">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-card
      bg-variant="light"
      no-body>
      <b-row no-gutters>
        <b-col xl="6">
          <b-card-img v-b-modal:product-modal src="https://via.placeholder.com/500" style="max-width: 500px; max-height: 500px"></b-card-img>
        </b-col>
        <b-col xl="6">
          <b-card-body :title="product.name" style="height: 100%; border-style: solid; border-color: lightgray; border-width: 0px 0px 0px 1px">
            <b-card-text>
              <p>tu opis krótki</p>
            </b-card-text>
            <div class="price-button-container">
              <p>{{ product.price }} PLN</p>
              <b-button variant="primary">DO KOSZYKA</b-button>
            </div>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
    <b-modal id="product-modal" title="Zdjęcie" ok-only ok-title="Zamknij">
      <b-card>
        <b-card-img src="../assets/guitar.png"/>
      </b-card>
    </b-modal>
    <b-navbar variant="light" class="navbar-sticky shadow-sm mt-4">
      <div class="navbar-container">
        <b-navbar-nav tabs fill>
          <b-nav-item @click="scrollToTop">Zdjęcie</b-nav-item>
          <b-nav-item @click="scrollToDesc">Opis produktu</b-nav-item>
          <b-nav-item @click="scrollToOpinions">Opinie klientów</b-nav-item>
        </b-navbar-nav>
      </div>
    </b-navbar>
    <b-card id="desc-container" bg-variant="light" class="mt-4" title="Opis produktu" text-variant="left">
      <p>opis produktu długi</p>
      <p>bla bla</p>
      <p>bla bla</p>
    </b-card>
    <b-card id="opinion-container" bg-variant="light" class="mt-4" title="Opinie klientów" text-variant="left">
      <b-card class="mt-2" v-for="index in 10" :key="index">
        <p>jakaś opinia</p>
      </b-card>
    </b-card>
  </b-container>
</template>

<script>
import axios from "axios";

export default {
name: "Product",
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
        },
        {
          text: '{Produkt}',
          href: '#'
        }],
      product: null
    }
  },
  methods: {
    scrollToDesc: function() {
      var element = document.getElementById('desc-container');
      var headerOffset = 72+72; // hardcoded, terrible solution, but I don't have any other ideas
      var elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
      var offsetPosition = elementPosition - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });
    },
    scrollToOpinions: function() {
      var element = document.getElementById('opinion-container');
      var headerOffset = 72 + 72; // hardcoded, terrible solution, but I don't have any other ideas
      var elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
      var offsetPosition = elementPosition - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });
    },
    scrollToTop: function() {
      var offsetPosition = 0;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8002/catalog/' + this.$route.params.id).then(
        response => {this.product = response.data; console.log(response); this.breadcrumbs[2].text = response.data.name}
    )
  }
}
</script>

<style scoped>
  .product-container {
    margin-top: 16px;
    max-width: 1400px;
    margin-left: auto;
    margin-right: auto;
  }
  .price-button-container {
    position: absolute;
    bottom: 16px;
    right: 16px;
    font-size: 24px;
  }
  .navbar-sticky {
    position: -webkit-sticky;
    position: sticky;
    top: 72px;
    z-index: 1;
    /*border-color: darkgray;*/
    /*border-style: solid;*/
    /*border-width: 0px 1px 1px 1px;*/
  }
</style>

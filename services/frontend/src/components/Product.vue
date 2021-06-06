<template>
  <b-container fluid class="product-container">
    <div v-if="product == null">
      <h5 primary>WCZYTYWANIE DANYCH</h5>
      <b-spinner style="width: 3rem; height: 3rem;" variant="primary"></b-spinner>
    </div>
    <div v-if="product != null">
      <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
      <b-card
          bg-variant="light"
          no-body>
        <b-row no-gutters>
          <b-col xl="6">
            <b-card-img v-b-modal:product-modal src="https://via.placeholder.com/500"
                        style="max-width: 500px; max-height: 500px"></b-card-img>
          </b-col>
          <b-col xl="6">
            <b-card-body :title="product.name"
                         style="height: 100%; border-style: solid; border-color: lightgray; border-width: 0px 0px 0px 1px">
              <b-card-text>
                <b-form-rating v-model="averageStars" variant="primary" no-border readonly inline class="opinion-avg-rating"></b-form-rating>
                <p class="text-left">{{ product.description }}</p>
              </b-card-text>
              <div class="price-button-container">
                <p>{{ product.price }} PLN</p>
                <b-button variant="primary" @click="addToCart(product)">DO KOSZYKA</b-button>
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
        <p>{{ product.description_long }}</p>
      </b-card>
      <b-card id="opinion-container" bg-variant="light" class="mt-4" title="Opinie klientów" text-variant="left">
        <p v-if="this.opinions.length === 0">Brak opinii o tym produkcie</p>
        <b-card class="mt-2" v-for="opinion in opinions" :key="opinion.opinion_id">
          <div class="opinion-rating-container">
            <b-form-rating v-model="opinion.stars" variant="primary" inline no-border readonly class="opinion-rating"></b-form-rating>
          </div>
          <h4>{{opinion.user_id}}</h4>
          <p>{{opinion.text}}</p>
        </b-card>
      </b-card>
    </div>
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
          to: '/'
        },
        {
          text: 'Kategoria',
          href: '#'
        },
        {
          text: '{Produkt}',
          href: '#'
        }],
      product: null,
      opinions: [],
      averageStars: 0
    }
  },
  methods: {
    scrollToDesc: function () {
      var element = document.getElementById('desc-container');
      var headerOffset = 72 + 72; // hardcoded, terrible solution, but I don't have any other ideas
      var elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
      var offsetPosition = elementPosition - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });
    },
    scrollToOpinions: function () {
      var element = document.getElementById('opinion-container');
      var headerOffset = 72 + 72; // hardcoded, terrible solution, but I don't have any other ideas
      var elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
      var offsetPosition = elementPosition - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });
    },
    scrollToTop: function () {
      var offsetPosition = 0;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });
    },
    addToCart: function (product) {
      axios.post('/api/basket/basket/add/', {
        "product_id": product.catalog_item_id,
        "quantity": 1
      }).then(
          response => {
            console.log(response);
            this.$router.push('/cart');
          }
      )
    }
  },
  mounted() {
    this.product = null;
    axios.get('/api/catalog/product/' + this.$route.params.slug).then(
        response => {
          this.product = response.data[0];
          console.log(response.data[0]);
          this.breadcrumbs[2].text = response.data[0].name

          axios.get('/api/catalog/opinionProd/?prod_id=' + this.product.catalog_item_id).then(
              response => {
                this.opinions = response.data;
                console.log(response.data);

                this.averageStars = 0;
                for(var opinion of this.opinions){
                  this.averageStars += opinion.stars;
                }
                this.averageStars /= this.opinions.length;
              }
          )

        }
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

.opinion-avg-rating {
  background: #F8F9FA;
}
.opinion-rating {
}

.opinion-rating-container {
  position: absolute;
  right: 0px;
  top: 0px;
}
</style>

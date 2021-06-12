<template>
  <div class="cart-container">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-row no-gutters>
      <b-col md="9">
        <div v-if="loading" class="cart-loading-container">
          <h5 primary>WCZYTYWANIE DANYCH</h5>
          <b-spinner style="width: 3rem; height: 3rem;" variant="primary"></b-spinner>
        </div>
        <div v-if="!loading">
          <CartItem v-for="product in products" :key="product.slug" v-bind:product="product"></CartItem>
        </div>
      </b-col>
      <b-col md="3">
        <p class="h3">Do zapłaty: {{ totalPrice }} PLN</p>
        <b-button :disabled="loading || products.length===0" variant="primary" @click="$router.push('/pay')">Kupuję i płacę</b-button>
      </b-col>
    </b-row>
  </div>
</template>
<script>
import CartItem from "@/components/CartItem";
import axios from "axios";

export default {
  name: "Cart",
  components: {CartItem},
  data: function () {
    return {
      breadcrumbs: [
        {
          text: 'Home',
          to: '/'
        },
        {
          text: 'Koszyk',
          href: '#'
        }],
      products: [],
      totalPrice: 0,
      user: null,
      loading: true
    }
  },
  mounted() {
    let self = this;
    axios.get('/api/user/rest-auth/user/', {withCredentials: true, headers: { 'Authorization': "Token " + this.$session.get("key") }}).then(
        response => {
          console.log(response.data);
          this.user = response.data;
          axios.get('/api/basket/basket/?user_id=' + this.user.id).then(
              response => {
                console.log(response.data)
                let basketSize = 0;
                let expectedBasketSize = response.data[0].basket_item.length;
                if(expectedBasketSize > 0){
                  for(let basketItem of response.data[0].basket_item) {
                    axios.get('/api/catalog/product/' + basketItem.catalog_item_id).then(
                        response => {
                          let product = response.data[0];
                          console.log(product);
                          product.quantity = basketItem.quantity;
                          this.products.push(product);
                          this.totalPrice += (product.price * product.quantity);
                          basketSize++; // leaving a way to react to failed requests
                          console.log("Cart entry " + basketSize + " of " + expectedBasketSize);
                          if (basketSize === expectedBasketSize) {
                            this.loading = false;
                          }
                        }
                    )
                  }
                }
                else {
                  this.loading = false;
                }
              }
          ).catch(function(err){
            console.log(err)
          });
        }
    ).catch(function (error){
      console.log(error);
      self.$session.remove("key");
      self.$bvModal.show("modal-profile-auth");
      self.$router.push("/login");
    });
  }
}
</script>
<style scoped>
.cart-container {
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 16px;
  text-align: right;
}
.cart-loading-container {
  width: 100%;
  text-align: center;
}
</style>

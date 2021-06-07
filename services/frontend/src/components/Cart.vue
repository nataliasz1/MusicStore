<template>
  <div class="cart-container">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-row no-gutters>
      <b-col md="9">
        <CartItem v-for="product in products" :key="product.slug" v-bind:product="product"></CartItem>
      </b-col>
      <b-col md="3">
        <p class="h3">Do zapłaty: {{ totalPrice }} PLN</p>
        <b-button variant="primary" @click="$router.push('/pay')">Kupuję i płacę</b-button>
      </b-col>
    </b-row>
  </div>
</template>
<script>
import CartItem from "@/components/CartItem";
import axios from "axios";
// import axios from "axios";

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
      user: null
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
                for(let basketItem of response.data){
                  axios.get('/api/catalog/product/' + basketItem.slug).then(
                      response => {
                        let product = response.data;
                        product.quantity = basketItem.quantity;
                        this.products.append(product);
                        this.totalPrice += (product.price * product.quantity);
                      }
                  )
                }
              }
          )
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
</style>

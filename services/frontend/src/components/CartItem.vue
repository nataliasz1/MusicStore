<template>
  <div class="orderItemContainer">
    <b-card
        bg-variant="light"
        class="mb-3 cart-item"
        style="object-fit: cover">
      <b-row no-gutters>
        <b-col md="1">
          <b-card-img src="https://via.placeholder.com/500" class="cart-item-image"></b-card-img>
        </b-col>
        <b-col md="11">
          <b-card-body class="text-right">
            <b-card-text right class="text-primary">
              <b-card-text class="h3 text-dark">{{product.name}}</b-card-text>
              <b-card-text class="h5">Ilość: {{ product.quantity }}</b-card-text>
              <b-card-text class="h5">{{ product.price * product.quantity }} PLN</b-card-text>
              <b-button variant="primary" @click="removeFromCart">Usuń z koszyka</b-button>
            </b-card-text>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CartItem",
  props: ['product'],
  data: function (){
    return {
      user: null
    }
  },
  methods: {
    removeFromCart: function (){
      axios.get('/api/user/rest-auth/user/', {withCredentials: true, headers: { 'Authorization': "Token " + this.$session.get("key") }}).then(
          response => {
            console.log(response.data);
            this.user = response.data;
            axios.post('/api/basket/basket/removeItem/?user_id=' + this.user.id,
                {
                  "product_id": this.product.catalog_item_id,
                  "quantity": this.product.quantity
                }).then(
                response => {
                  console.log(response.data);
                  this.$router.go();
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
}
</script>

<style scoped>
.orderItemContainer {

}

.cart-item {

}

.cart-item-image {
  height: 150px;
  width: auto;
}
</style>

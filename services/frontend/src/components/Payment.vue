<template>
  <div class="payment-container">
    <h4 v-if="!loading" class="mb-4">Do zapłaty: {{ totalPrice }} PLN</h4>
    <div v-if="loading" class="payment-loading-container">
      <h5 primary>WCZYTYWANIE DANYCH</h5>
      <b-spinner style="width: 3rem; height: 3rem;" variant="primary"></b-spinner>
    </div>
    <div :hidden="loading" id="paypal-button-container"></div>
    <b-button variant="primary" @click="simulatePayment">Kup na zeszyt</b-button>
    <b-button variant="danger" @click="$router.push('/cart')">Anuluj</b-button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Payment",
  data: function () {
    return {
      user: null,
      products: [],
      loading: true,
      totalPrice: 0
    }
  },
  methods: {
    simulatePayment: function (){
      axios.get('/api/order/order/?user_id=' + this.user.id).then(
          response => {
            console.log(response.data);
          }
      ).catch(function (error){
        console.log(error);
      })
    }
  },
  mounted() {
    let self = this;
    // eslint-disable-next-line no-undef
    paypal.Buttons({

      createOrder: function (data, actions) {
        console.log('' + self.totalPrice);
        return actions.order.create({
          purchase_units: [{
            amount: {
              value: '' + self.totalPrice
            }
          }]
        });
      },

      onApprove: function (data, actions) {
        return actions.order.capture().then(function (details) {
          alert('Transaction completed by ' + details.payer.name.given_name + '!');
        });
      }


    }).render('#paypal-button-container');

    axios.get('/api/user/rest-auth/user/', {
      withCredentials: true,
      headers: {'Authorization': "Token " + this.$session.get("key")}
    }).then(
        response => {
          console.log(response.data);
          this.user = response.data;
          axios.get('/api/basket/basket/?user_id=' + this.user.id).then(
              response => {
                console.log(response.data)
                let basketSize = 0;
                let expectedBasketSize = response.data[0].basket_item.length;
                if (expectedBasketSize > 0) {
                  for (let basketItem of response.data[0].basket_item) {
                    axios.get('/api/catalog/products/' + basketItem.catalog_item_id).then(
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
                } else {
                  this.loading = false;
                }
              }
          ).catch(function (err) {
            console.log(err)
          });
        }
    ).catch(function (error) {
      console.log(error);
      self.$session.remove("key");
      self.$bvModal.show("modal-profile-auth");
      self.$router.push("/login");
    });
  }
}
</script>
<style scoped>
.payment-container {
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 16px;
  text-align: center;
}

.payment-loading-container {
  width: 100%;
  text-align: center;
}
</style>

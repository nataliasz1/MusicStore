<template>
  <div class="orderItemContainer">
    <b-card
        bg-variant="light"
        class="mb-3 cart-item"
        style="object-fit: cover">
      <b-row no-gutters>
        <b-col md="1">
          <b-card-img v-if="product.images.length > 0" :src="product.images[0].img_url" class="order-item-image"/>
          <b-card-img v-if="product.images.length === 0" src="../assets/guitar.png" class="order-item-image"/>
        </b-col>
        <b-col md="11">
          <b-card-body class="text-right">
            <b-card-text right class="text-primary">
<!--              <b-card-text class="h3 text-dark">{{product.name}}</b-card-text>-->
              <b-card-text class="h3 text-dark">{{ product.name }}</b-card-text>
              <b-card-text class="h5">Ilość: {{ orderItem.quantity }}</b-card-text>
              <p class="text-dark mb-0">Cena katalogowa:</p>
              <b-card-text class="h5">{{ orderItem.price }} PLN</b-card-text>
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
name: "OrderItem",
  props: ['orderItem'],
  data: function (){
    return {
      product: null
    }
  },
  mounted() {
    axios.get('/api/catalog/products/' + this.orderItem.catalog_item_id).then(
        response => {
          this.product = response.data[0];
          console.log(response.data[0]);
        }
    )
  }
}
</script>

<style scoped>
.order-item-image {
  height: 150px;
  width: auto;
}
</style>

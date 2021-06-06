<template>
  <div class="cartItemContainer">
    <b-card
        bg-variant="light"
        class="mb-3 cart-item"
        style="object-fit: cover">
      <b-row no-gutters>
        <b-col md="1">
          <b-card-img src="../assets/guitar.png" class="cart-item-image"></b-card-img>
        </b-col>
        <b-col md="11">
          <b-card-body class="text-right">
            <b-card-text right class="text-primary">
              <b-card-text class="h3 text-dark">Jakaś gitara akustyczna</b-card-text>
              <b-card-text class="h5">999,99 PLN</b-card-text>
              <b-button variant="primary" @click="$router.push('product')">Usuń z koszyka</b-button>
            </b-card-text>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "CartItem",
  props: ['product']
}
</script>

<style scoped>
.cartItemContainer {

}

.cart-item {

}

.cart-item-image {
  height: 150px;
  width: auto;
}
</style>

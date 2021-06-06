<template>
  <div class="catbar-full-container mb-4">
    <b-navbar variant="light" class="shadow">
      <div class="catbar-container">
        <b-navbar-nav tabs fill>
          <b-nav-item v-for="category in categories" :key="category.category_id" @click="$router.push('/search')">
            {{ category.name }}
          </b-nav-item>
        </b-navbar-nav>
      </div>
    </b-navbar>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CategoryBar",
  data: function () {
    return {
      categories: []
    }
  },
  mounted() {
    axios.get('/api/catalog/categories/').then(
        response => {
          this.categories = response.data;
          console.log(response.data)
        }
    )
  }
}
</script>

<style scoped>
.catbar-full-container {
  margin-top: 117px;
}

.catbar-container {
  margin: auto;
  width: 1600px;
  padding: 8px;
  font-size: 16px;
}
</style>

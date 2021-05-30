<template>
  <div class="catbar-full-container mb-4">
    <b-navbar variant="light" class="shadow">
      <div class="catbar-container">
          <b-navbar-nav tabs fill>
            <b-nav-item @click="$router.push('/search')">Dęte</b-nav-item>
            <b-nav-item @click="$router.push('/search')">Gitary</b-nav-item>
            <b-nav-item @click="$router.push('/search')">Klawiszowe</b-nav-item>
            <b-nav-item @click="$router.push('/search')">Nagłośnienie</b-nav-item>
            <b-nav-item @click="$router.push('/search')">Kable</b-nav-item>
            <b-nav-item @click="$router.push('/search')">Oświetlenie</b-nav-item>
            <b-nav-item @click="$router.push('/search')">Perkusyjne</b-nav-item>
            <b-nav-item @click="$router.push('/search')">Smyczkowe</b-nav-item>
          </b-navbar-nav>
      </div>
    </b-navbar>
  </div>
</template>

<script>
export default {
name: "CategoryBar"
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

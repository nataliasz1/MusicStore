<template>
  <div id="app">
    <div class="content">
      <Navbar id="navbar"></Navbar>
      <CategoryBar></CategoryBar>
      <transition name="fade" appear mode="out-in">
        <router-view></router-view>
      </transition>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import CategoryBar from "@/components/CategoryBar";
// import Home from "@/components/Home";
// import Product from "@/components/Product";

export default {
  name: 'App',
  components: {
    // Product,
    // Home,
    CategoryBar,
    Footer,
    Navbar
  },
  created() {
    window.addEventListener('scroll', this.onScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.onScroll);
  },
  data: function() {
    return {
      isScrolled: false
    }
  },
  methods: {
    onScroll(){
      this.isScrolled = document.body.scrollTop > 80 || document.documentElement.scrollTop > 80;
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  min-height: 100%;
}

.content {
  min-height: 100vh;
}

body {
  height: 100%;
}

html {
  height: 100%;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>

<template>
  <div class="helloContainer">
    <transition name="slide">
      <side-menu v-if="menuShow"></side-menu>
    </transition>
    <div class="helloContent">
      <p v-for="index in 40" :key="index">test {{index}}<br></p>
      <button v-on:click="toggleMenu()">test</button>
    </div>
  </div>
</template>

<script>
import SideMenu from "@/components/SideMenu";
export default {
  name: 'HelloWorld',
  components: {SideMenu},
  props: {
    msg: String,
  },
  data: function () {
    return {
      menuShow: false
    }
  },
  methods: {
    toggleMenu: function () {
      this.menuShow = !this.menuShow;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.helloContainer{
  min-height: 100%;
}
</style>

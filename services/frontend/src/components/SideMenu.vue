<template>
<div class="navContainer">
  <p class="menuLink">COUNTRY</p>
  <p class="menuLink">ROADS</p>
  <p class="menuLink">TAKE</p>
  <p class="menuLink">ME</p>
  <p class="menuLink">HOME</p>
  <p class="menuLink">TO</p>
  <p class="menuLink">THE</p>
  <p class="menuLink">PLACE</p>
  <p class="menuLink">I</p>
  <p class="menuLink">BELONG</p>
</div>
</template>

<script>
export default {
name: "SideMenu"
}
</script>

<style scoped>
.navContainer {
  width: 300px;
  min-height: 100%;
  float: left;
  position: fixed;
  left: 0px;
  top: 0px;
  bottom: 0px;
  background: white;
  z-index: 1;
  padding: 6px;
  border-style: solid;
  border-width: 0px 1px 0px 0px;
}

.menuLink {
  margin-top: 8px;
  color: BLACK;
  font-size: 25px;
}

p {
  line-height: 25px;
}
/* Enter and leave animations can use different */
/* durations and timing functions.              */
.slide-enter-active {
  transition: 1s;
}
.slide-leave-active {
  transition: 1s;
}
.slide-enter {
  transform: translate(-100%, 0);
  background: #007BFF;
}
.slide-leave-to{
  transform: translate(-100%, 0);
  background: #007BFF;
}


</style>

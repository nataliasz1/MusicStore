<template>
  <div class="nav-container">
    <p class="menu-link">COUNTRY</p>
    <p class="menu-link">ROADS</p>
    <p class="menu-link">TAKE</p>
    <p class="menu-link">ME</p>
    <p class="menu-link">HOME</p>
    <p class="menu-link">TO</p>
    <p class="menu-link">THE</p>
    <p class="menu-link">PLACE</p>
    <p class="menu-link">I</p>
    <p class="menu-link">BELONG</p>
  </div>
</template>

<script>
export default {
  name: "SideMenu"
}
</script>

<style scoped>
.nav-container {
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

.menu-link {
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

.slide-leave-to {
  transform: translate(-100%, 0);
  background: #007BFF;
}


</style>

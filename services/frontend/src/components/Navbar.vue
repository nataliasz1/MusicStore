<template>
  <div class="full-navbar">
    <b-navbar variant="primary" fixed="top">
      <div class="nav-container" v-bind:class="{'nav-container': this.$parent.$data.isScrolled,  'nav-container-thin': this.$parent.$data.isScrolled}">
        <b-icon v-if="this.$parent.$data.isScrolled" icon="list" variant="light" class="h1 border rounded p-2 mt-2"></b-icon>
        <b-navbar-brand v-if="this.$parent.$data.isScrolled" href="#" class="nav-logo-thin mt-1 ml-4" @click="$router.push('/')"><img src="../assets/logo_note.png"></b-navbar-brand>
        <b-navbar-brand v-else href="#" class="nav-logo" @click="$router.push('/')"><img src="../assets/logo_cropped.png"></b-navbar-brand>
        <div class="nav-buttons">
          <b-navbar-nav align="right" v-bind:class="{'nav-buttons': !this.$parent.$data.isScrolled,  'nav-buttons-thin': this.$parent.$data.isScrolled}">
            <b-nav-form v-if="this.$parent.$data.isScrolled" class="nav-search">
              <b-form-input size="md" class="mr-md-2 nav-search-bar" placeholder="Jakiego produktu szukasz?"></b-form-input>
              <b-button size="md" class="my-2 my-sm-0" variant="primary" type="submit" @click="$router.push('/search')">SZUKAJ</b-button>
            </b-nav-form>
            <b-nav-form v-else class="nav-search">
              <b-form-input size="lg" class="mr-lg-2 nav-search-bar" placeholder="Jakiego produktu szukasz?"></b-form-input>
              <b-button size="lg" class="my-2 my-sm-0" variant="primary" type="submit" @click="$router.push('/search')">SZUKAJ</b-button>
            </b-nav-form>
            <b-nav-item><b-button variant="primary" class="nav-button" @click="$router.push('/login')">MOJE KONTO</b-button></b-nav-item>
            <b-nav-item><b-button variant="primary" class="nav-button" @click="$router.push('/cart')">KOSZYK</b-button></b-nav-item>
            </b-navbar-nav>
        </div>
      </div>
    </b-navbar>
  </div>
</template>

<script>
export default {
name: "Navbar",
}
</script>

<style scoped>
  .nav-container {
    margin: auto;
    width: 1600px;
    text-align: left;
    padding: 8px;
    display: flex;
  }
  .nav-container-thin {
    margin: auto;
    width: 1600px;
    text-align: left;
    padding: 0;
    display: flex;
  }
  .nav-logo {
    font-size: 36px;
    color: white;
  }
  .nav-logo-thin {
    font-size: 16px;
    color: white;
  }
  .nav-buttons {
    margin-left: auto;
    margin-top: auto;
    margin-bottom: auto;
    font-size: 24px;
  }
  .nav-buttons-thin {
    margin-left: auto;
    margin-top: auto;
    margin-bottom: auto;
    font-size: 16px;
  }
  .nav-button {
    color: white;
  }
  .nav-search {
    margin-right: 50px;
  }
</style>

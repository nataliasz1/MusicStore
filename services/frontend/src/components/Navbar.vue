<template>
  <div class="full-navbar">
    <b-navbar variant="primary" fixed="top">
      <div class="nav-container"
           v-bind:class="{'nav-container': this.$parent.$data.isScrolled,  'nav-container-thin': this.$parent.$data.isScrolled}">
        <div v-if="this.$parent.$data.isScrolled">
          <b-dropdown size="lg" variant="link" toggle-class="text-decoration-none" no-caret>
            <template #button-content>
              <img src="../assets/list.png" class="list-icon-button">
            </template>
            <b-dropdown-header>Kategorie</b-dropdown-header>
            <b-dropdown-item v-for="category in categories" :key="category.category_id" @click="$router.push('/search')">
              {{ category.name }}
            </b-dropdown-item>
          </b-dropdown>
        </div>
        <b-navbar-brand v-if="this.$parent.$data.isScrolled" href="#" class="nav-logo-thin mt-1 ml-4"
                        @click="$router.push('/')"><img src="../assets/logo_note.png"></b-navbar-brand>
        <b-navbar-brand v-else href="#" class="nav-logo" @click="$router.push('/')"><img
            src="../assets/logo_cropped.png"></b-navbar-brand>
        <div class="nav-buttons">
          <b-navbar-nav align="right"
                        v-bind:class="{'nav-buttons': !this.$parent.$data.isScrolled,  'nav-buttons-thin': this.$parent.$data.isScrolled}">
            <b-nav-form v-if="this.$parent.$data.isScrolled" class="nav-search">
              <b-form-input size="md" class="mr-md-2 nav-search-bar"
                            placeholder="Jakiego produktu szukasz?"></b-form-input>
              <b-button size="md" class="my-2 my-sm-0" variant="primary" type="submit" @click="$router.push('/search')">
                SZUKAJ
              </b-button>
            </b-nav-form>
            <b-nav-form v-else class="nav-search">
              <b-form-input size="lg" class="mr-lg-2 nav-search-bar"
                            placeholder="Jakiego produktu szukasz?"></b-form-input>
              <b-button size="lg" class="my-2 my-sm-0" variant="primary" type="submit" @click="$router.push('/search')">
                SZUKAJ
              </b-button>
            </b-nav-form>
            <b-nav-item>
              <b-button v-if="!$session.get('key')" variant="primary" class="nav-button" @click="$router.push('/profile')">MOJE KONTO</b-button>
              <b-button v-if="$session.get('key') && user.id" variant="primary" class="nav-button" @click="$router.push('/profile')">MOJE KONTO ({{user.email}})</b-button>
            </b-nav-item>
            <b-nav-item>
              <b-button variant="primary" class="nav-button" @click="$router.push('/cart')">KOSZYK</b-button>
            </b-nav-item>
          </b-navbar-nav>
        </div>
      </div>
    </b-navbar>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Navbar",
  data: function () {
    return {
      categories: [],
      user: null
    }
  },
  mounted() {
    let self = this;
    axios.get('/api/catalog/categories/').then(
        response => {
          this.categories = response.data;
          console.log(response.data)
        }
    )
    if(this.$session.has("key")){
      axios.get('/api/user/rest-auth/user/', {withCredentials: true, headers: { 'Authorization': "Token " + this.$session.get("key") }}).then(
          response => {
            console.log(response.data);
            this.user = response.data;
          }
      ).catch(function (error){
        console.log(error);
        self.$session.remove("key");
        self.$bvModal.show("modal-profile-auth");
      });
    }
  }
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

.list-icon-button {
  width: 36px;
  height: 36px;
}
</style>

<template>
  <b-container fluid class="profile-container">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-row no-gutters>
      <b-col xl="10">
        <b-card bg-variant="light" title="Moje dane" class="text-left mr-2 mb-4">
          <h5 class="mb-0">Imię</h5>
          <p class="mb-4">placeholder</p>
          <h5 class="mb-0">Nazwisko</h5>
          <p class="mb-4">placeholder</p>
          <h5 class="mb-0">Telefon kontaktowy</h5>
          <p class="mb-4">placeholder</p>
          <h5 class="mb-0">Adres e-mail</h5>
          <p class="mb-4">placeholder</p>
        </b-card>
        <b-card bg-variant="light" title="Moje zamówienia" class="text-left mr-2 mb-4">
          <p>placeholder brak zamówień</p>
        </b-card>
      </b-col>
      <b-col xl="2">
        <b-card bg-variant="light" title="Ustawienia" text-variant="left" class="ml-2 text-left">
          <h5 class="mt-5">Konto</h5>
          <p>Zmień hasło</p>
          <p>Usuń konto</p>
          <h5 class="mt-5">Dane osobowe</h5>
          <p>Adres dostawy</p>
          <p>Dane do faktury</p>
          <p>Dane kontaktowe</p>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// import axios from "axios";

export default {
  name: "Profile",
  data: function () {
    return {
      breadcrumbs: [
        {
          text: 'Home',
          to: '/'
        },
        {
          text: 'Profil użytkownika',
          href: '#'
        }]
    }
  },
  // mounted() {
  //   axios.defaults.withCredentials = true;
  //   if(!this.$session.has("key")){
  //     this.$router.push('login');
  //   }
  //   else {
  //     axios.get('https://127.0.0.1:8003/rest-auth/user/', { headers: { 'Authorization': "Token " + this.$session.get("key") } }).then(
  //         response => {console.log(response.data)}
  //     )
  //   }
  // }
}
</script>

<style scoped>
.profile-container {
  margin-top: 16px;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}

.options-container {

}
</style>

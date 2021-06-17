<template>
  <b-container fluid class="profile-container">
    <b-breadcrumb :items="breadcrumbs"></b-breadcrumb>
    <b-row no-gutters>
      <b-col xl="10">
        <b-card bg-variant="light" title="Moje dane" class="text-left mr-2 mb-4">
          <h5 class="mb-0">Imię</h5>
          <p class="mb-4">{{user.first_name === "" ? "brak" : user.first_name}}</p>
          <h5 class="mb-0">Nazwisko</h5>
          <p class="mb-4">{{user.last_name === "" ?  "brak" : user.last_name}}</p>
          <h5 class="mb-0">Telefon kontaktowy</h5>
          <p class="mb-4">{{user.phone === "" ?  "brak" : user.phone}}</p>
          <h5 class="mb-0">Adres e-mail</h5>
          <p class="mb-4">{{ user.email }}</p>
        </b-card>
        <b-card bg-variant="light" title="Moje zamówienia" class="text-left mr-2 mb-4">
          <div v-if="loading">
            <h5 primary>WCZYTYWANIE DANYCH</h5>
            <b-spinner style="width: 3rem; height: 3rem;" variant="primary"></b-spinner>
          </div>
          <p v-if="orders.length === 0">brak zamówień</p>
          <OrderBox v-for="order in orders" :key="order.order_id" v-bind:order="order"></OrderBox>
        </b-card>
      </b-col>
      <b-col xl="2">
        <b-card bg-variant="light" title="Ustawienia" text-variant="left" class="ml-2 text-left">
          <h5 class="mt-5">Konto</h5>
          <p class="page-link profile-link">Zmień hasło</p>
          <p class="page-link profile-link">Usuń konto</p>
          <p class="page-link profile-link" @click="logout">Wyloguj</p>
          <h5 class="mt-5">Dane osobowe</h5>
          <p class="page-link profile-link">Adres dostawy</p>
          <p class="page-link profile-link">Dane do faktury</p>
          <p class="page-link profile-link">Dane kontaktowe</p>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from "axios";
import OrderBox from "@/components/OrderBox";

export default {
  name: "Profile",
  components: {OrderBox},
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
        }],
      user: null,
      orders: [],
      loading: true
    }
  },
  methods: {
    logout: function (){
      axios.post('/api/user/rest-auth/logout/', {}, {withCredentials: true, headers: { 'Authorization': "Token " + this.$session.get("key") }}).then(
          response => {
              console.log(response.data);
              this.$session.remove('key');
              this.user = null;
              window.location.reload();
            }
      )
    }
  },
  mounted(){
    let self = this;
    if (!this.$session.has("key")) {
      this.$router.push('/login');
    }
    else {
      console.log(this.$session.get("key"));
      axios.get('/api/user/rest-auth/user/', { headers: { 'Authorization': "Token " + this.$session.get("key") }, withCredentials: true }).then(
          response => {
            console.log(response.data);
            this.user = response.data;
            axios.get('/api/order/orders/user-id/' + this.user.id, { withCredentials: true }).then(
                response => {
                  console.log(response.data);
                  this.orders = response.data;
                  this.loading = false;
                }
            )
            .catch(error => {
              console.log(error);
              this.loading = false;
            })
          }
      ).catch(function (error){
        console.log(error);
        self.$bvModal.show("modal-profile-auth");
        self.$session.remove("key");
        self.$router.push("/login");
      });
    }
  }
}
</script>

<style scoped>
.profile-container {
  margin-top: 16px;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}
.profile-link {
  cursor: pointer;
}
.options-container {

}
</style>

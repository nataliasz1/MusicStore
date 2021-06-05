<template>

  <div class="login-container">
    <b-card bg-variant="light" class="login-card text-left">
      <p class="h2">Logowanie</p>
      <b-form-input placeholder="Nazwa użytkownika" class="mt-4"></b-form-input>
      <b-form-input placeholder="Hasło" type="password" class="mt-4"></b-form-input>
      <a class="mt-1">Nie pamiętam hasła</a><br>
      <b-button variant="primary" class="mt-4" @click="login">ZALOGUJ</b-button>
      <br><br>
      <p class="mb-0">Nie masz konta?</p>
      <b-button>ZAREJESTRUJ SIĘ</b-button>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  methods: {
    login: function () {
      if (!this.$session.exists()) {
        this.$session.start();
      }
      axios.defaults.withCredentials = true;
      axios.post('http://127.0.0.1:9090/api/user/rest-auth/login/', {
        "username": "admin",
        "email": "admin@admin.com",
        "password": "admin"
      }).then(
          response => {
            console.log(response.data);
            if (response.data.key) {
              this.$session.set('key', response.data.key)
              // axios.get('http://127.0.0.1:9090/api/user/rest-auth/user/').then(
              //     response => {console.log(response.data)}
              // )
            } else {
              console.log("key not returned")
            }
          }
      )
    }
  }
}
</script>

<style scoped>

.login-container {
  max-width: 1600px;
  margin-right: auto;
  margin-left: auto;
  margin-top: 16px;
}

.login-card {
  width: 600px;
  margin-left: auto;
  margin-right: auto;
}

</style>

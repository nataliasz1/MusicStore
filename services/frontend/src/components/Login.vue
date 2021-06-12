<template>
  <div class="register-container">
    <b-card bg-variant="light" class="register-card text-left">
      <p class="h2">Logowanie</p>
      <b-form-input placeholder="Adres e-mail" v-model="username" class="mt-4"></b-form-input>
      <b-form-input placeholder="Hasło" type="password" v-model="password" class="mt-4"></b-form-input>
      <a class="mt-1 pointer-text" @click="forgotPassword">Nie pamiętam hasła</a>
      <br>
      <b-button variant="primary" class="mt-4" @click="login">ZALOGUJ</b-button>
      <br><br>
      <p class="mb-0">Nie masz konta?</p>
      <b-button @click="$router.push('/register')">ZAREJESTRUJ SIĘ</b-button>
    </b-card>
    <b-modal id="modal-login-password" ok-only title="To projekt, nie produkt">
      <div class="kermit-modal-image-container">
        <img class="kermit-modal-image" src="https://media.tenor.com/images/26673b07e3efd6256d280eede517ab11/tenor.gif"/>
      </div>
    </b-modal>
    <b-modal id="modal-login-fail" ok-only title="Logowanie nieudane">
      <p>Logowanie nieudane.</p>
      <p>Sprawdź poprawność wprowadzonych danych i spróbuj ponownie.</p>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data: function () {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    login: function () {
      let self = this;
      if (!this.$session.exists()) {
        this.$session.start();
      }
      axios.post('/api/user/rest-auth/login/', {
        "email": this.username,
        "password": this.password
      }, {withCredentials: true}).then(
          response => {
            console.log(response.data);
            if (response.data.key) {
              this.$session.set('key', response.data.key);
              window.location.reload();
            } else {
              this.$bvModal.show("modal-login-fail");
            }
          }
      ).catch(function (error){
        console.log(error);
        self.$bvModal.show("modal-login-fail");
      })
    },
    forgotPassword: function () {
      this.$bvModal.show("modal-login-password");
    }
  },
  mounted(){
    if (this.$session.has("key")) {
      this.$router.push("/profile");
    }
  }
}
</script>

<style scoped>

.register-container {
  max-width: 1600px;
  margin-right: auto;
  margin-left: auto;
  margin-top: 16px;
}

.register-card {
  width: 600px;
  margin-left: auto;
  margin-right: auto;
}
.pointer-text {
  cursor: pointer;
}
.kermit-modal-image {
  width: 250px;
}
.kermit-modal-image-container{
  width: 100%;
  text-align: center;
}
</style>

<template>
  <div class="register-container">
    <b-card bg-variant="light" class="register-card text-left">
      <p class="h2">Rejestracja</p>
      <b-form-input placeholder="Adres e-mail" v-model="email" class="mt-4"></b-form-input>
      <b-form-input placeholder="Hasło" type="password" v-model="password" class="mt-4"></b-form-input>
      <b-form-input placeholder="Powtórz hasło" type="password" v-model="password2" class="mt-4"></b-form-input>
      <p class="text-danger" v-if="showPassWarning">Hasła muszą być jednakowe!</p>
      <b-form-checkbox id="tos-checkbox" name="tos-checkbox" v-model="tosAccepted">Akceptuję regulamin serwisu</b-form-checkbox>
      <p class="text-danger" v-if="showTosWarning">Musisz zaakceptować regulamin!</p>
      <br><br>
      <b-button variant="primary" @click="register">STWÓRZ KONTO</b-button>
    </b-card>
    <b-modal id="modal-register-success" ok-only title="Sukces!" @hidden="$router.push('/login')">
      <p>Konto zostało stworzone. Możesz się zalogować.</p>
    </b-modal>
    <b-modal id="modal-register-fail" ok-only title="Coś poszło nie tak">
      <p>Nie udało się stworzyć konta</p>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
name: "Register",
  data: function () {
    return {
      email: "",
      password: "",
      password2: "",
      tosAccepted: false,
      showPassWarning: false,
      showTosWarning: false
    }
  },
  methods: {
    register: function () {
      this.showTosWarning = false;
      this.showPassWarning = false;
      if(!this.tosAccepted){
        this.showTosWarning = true;
        return;
      }
      if(this.password !== this.password2){
        this.showPassWarning = true;
        return;
      }
      if (!this.$session.exists()) {
        this.$session.start();
      }
      axios.post('/api/user/rest-auth/registration/', {
        "email": this.email,
        "password1": this.password,
        "password2": this.password2
      }, {withCredentials: true}).then(
          response => {
            console.log(response.data);
            if(response.data.key){
              this.$bvModal.show("modal-register-success");
            }
            else {
              this.$bvModal.show("modal-register-fail");
            }
          }
      )
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
</style>

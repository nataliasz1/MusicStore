<template>

  <div class="login-container">
    <b-card bg-variant="light" class="login-card text-left">
      <p class="h2">Logowanie</p>
      <b-form-input placeholder="Nazwa użytkownika" class="mt-4"></b-form-input>
      <b-form-input placeholder="Hasło" type="password" class="mt-4"></b-form-input>
      <a class="mt-1">Nie pamiętam hasła</a><br>
      <b-button variant="primary" class="mt-4">ZALOGUJ</b-button>
      <br><br>
      <p class="mb-0">Nie masz konta?</p>
      <b-button>ZAREJESTRUJ SIĘ</b-button>
    </b-card>
  </div>
</template>

<script>
export default {
name: "Login"
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

<template>
  <div class="footer">
    <p>(C) 2021 Sklep muzyczny ERSMS</p>
    <b-modal id="modal-cookies" @hide="modalClosed" ok-only title="Ta strona wykorzystuje ciasteczka">
      <p>Nasza witryna stosuje pliki cookies w celu umożliwienia logowania i obsługi profilu użytkownika.
        Korzystając z tej strony wyrażasz zgodę na zapisywanie tych ciasteczek na Twoim urządzeniu.</p>
      <p>Brak zgody uniemożliwia poprawne działanie serwisu.</p>
      <div  class="cookie-modal-image-container">
        <img class="cookie-modal-image" src="../assets/cookie-monster-cropped.png"/>
      </div>
    </b-modal>
    <b-modal id="modal-profile-auth" ok-only title="Coś poszło nie tak">
      <p>Nie udało się uwierzytelnić użytkownika. Jesteś wylogowany.</p>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: "Footer",
  methods: {
    modalClosed: function () {
      console.log("Cookies accepted");
      this.$session.set("cookies", true);
    }
  },
  mounted() {
    if(!this.$session.has("cookies")){
      this.$session.set('cookies', false);
      this.$bvModal.show("modal-cookies");
    }
    else {
      if(this.$session.get("cookies") === false){
        this.$bvModal.show("modal-cookies");
      }
    }
  }
}
</script>

<style scoped>
.footer {
  background: #393939;
  height: 300px;
  color: white;
  position: relative;
  bottom: 0px;
  padding: 16px;
  text-align: left;
}
.cookie-modal-image {
  width: 250px;
}
.cookie-modal-image-container{
  width: 100%;
  text-align: center;
}
</style>

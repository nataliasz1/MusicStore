<template>
  <div class="footer">
    <p>(C) 2021 Sklep muzyczny ERSMS</p>
    <b-modal id="modal-cookies" @hide="modalClosed" ok-only title="Ta strona wykorzystuje ciasteczka">
      <p>Nasza witryna stosuje pliki cookies w celu umożliwienia logowania i obsługi profilu użytkownika.
        Korzystając z tej strony wyrażasz zgodę na zapisywanie tych ciasteczek na Twoim urządzeniu.</p>
      <p>Brak zgody uniemożliwia poprawne działanie serwisu.</p>
      <a v-b-toggle.collapse-rodo class="rodo-link">Treść zgody RODO</a>
      <b-collapse id="collapse-rodo" class="mt-2">
        <p>Na podstawie art. 6 ust. 1 lit. a, art. 9 ust. 2 lit. a rozporządzenia Parlamentu Europejskiego i
          Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony osób fizycznych w związku
          z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu takich danych oraz
          uchylenia dyrektywy 95/46/WE (ogólne rozporządzenie o ochronie danych) Dz. Urz. UE L
          119/1, z 4.5.2016, zwanego dalej „RODO” wyrażam zgodę na przetwarzanie następujących
          kategorii moich danych osobowych (imię, nazwisko, telefon, mail). Podane dane będą
          przetwarzane wyłącznie w zakresie wymaganym do realizacji usługi konta internetowego
          w sklepie online. Dane są przetwarzane przez administratora sklepu online (NIP:
          1234567819, adres: ul. Wspólna 1/3 00-529 Warszawa).</p>
        <p>Podanie przeze mnie danych osobowych jest dobrowolne.
          Jest mi wiadomym, że posiadam prawo do:</p>
        <p>1) żądania od wskazanego w niniejszym oświadczeniu administratora danych osobowych:
          <p class="ml-3">a) dostępu do moich danych osobowych;</p>
        <p class="ml-3">b) sprostowania moich danych osobowych;</p>
        <p class="ml-3">c) usunięcia moich danych osobowych, jeżeli zachodzi jedna z okoliczności wskazanych
          w art. 17 ust. 1 RODO i jeżeli przetwarzanie moich danych osobowych nie jest
          niezbędne w zakresie wskazanym w art. 17 ust. 3 RODO;</p>
        <p class="ml-3">d) ograniczenia przetwarzania moich danych osobowych w przypadkach wskazanych w
          art. 18 ust. 1 RODO, </p>
        <p>2) wniesienia do wskazanego w niniejszym oświadczeniu administratora danych osobowych
          sprzeciwu wobec przetwarzania moich danych osobowych:
          a) do celów badań naukowych lub historycznych lub do celów statystycznych na mocy art.
          89 ust. 1 RODO, z przyczyn związanych z moją szczególną sytuacją,</p>
        <p>3) przenoszenia moich danych osobowych,</p>
        <p>4) wniesienia skargi do organu nadzorczego, tj. do Prezesa Urzędu Ochrony Danych
          Osobowych, w przypadku uznania, że przetwarzanie moich danych osobowych narusza
          przepisy RODO,</p>
        <p>5) wycofania w dowolnym momencie zgody na przetwarzanie moich danych osobowych. </p>
      </b-collapse>
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
.rodo-link {
  cursor: pointer;
}
</style>

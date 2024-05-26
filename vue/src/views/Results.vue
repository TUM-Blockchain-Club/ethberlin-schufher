<template>
   <HeaderLoggedIn />
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card class="result-card" elevation="10">
            <v-card-text>
              <div class="result-label">Name: {{ form.name }}</div>
              <div class="result-label">Surname: {{ form.surname }}</div>
              <div class="result-label">Bank Credit Score: {{ banksData.creditScore }}</div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <Footer />
    </v-container>
  </template>
  
<script>
import HeaderLoggedIn from '@/components/HeaderLoggedIn.vue';
import Footer from '@/components/Footer.vue';

  export default {
    props: ['form', 'banksData']
  };
  </script>
  
  <style scoped>
  .result-card {
    padding: 20px;
    background-color: #222831;
    color: white;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  }
  
  .result-label {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 20px;
    color: white;
  }
</style>
  
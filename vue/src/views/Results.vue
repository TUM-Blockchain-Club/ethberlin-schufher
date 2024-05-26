<template>
    <HeaderLoggedIn />
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card class="result-card" elevation="10">
            <v-card-text>
              <div class="result-label">These data were collected from your accounts in:</div>
              <v-list dense>
                <v-list-item v-for="bank in banksData" :key="bank" class="bank-item">
                  <v-list-item-content class="bank-item-content">
                    <v-list-item-title>{{ bank }}</v-list-item-title>
                    <v-list-item-icon>
                      <v-icon color="green">mdi-check-circle</v-icon>
                    </v-list-item-icon>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
              <div class="result-label">Aggregated Bank Credit Score: {{ score }}</div>
            </v-card-text>
            <ScoreBar :score="score" />
          </v-card>
        </v-col>
      </v-row>
      <Footer />
    </v-container>
  </template>
  
  <script>
  import { mapGetters } from 'vuex';
  import HeaderLoggedIn from '@/components/HeaderLoggedIn.vue';
  import Footer from '@/components/Footer.vue';
  import ScoreBar from '@/components/ScoreBar.vue';
  
  export default {
    computed: {
      ...mapGetters(['getBanksData', 'getScore']),
      banksData() {
        return this.getBanksData;
      },
      score() {
        return this.getScore;
      }
    },
    components: {
      HeaderLoggedIn,
      Footer,
      ScoreBar
    },
    created() {
      console.log("Received Banks Data:", this.banksData);
      console.log("Received Score:", this.score);
    }
  };
  </script>
  
  <style scoped>
  .result-card {
    margin-top: 4vh;
    padding: 20px;
    background: linear-gradient(145deg, #f0f0f0, #fafafa);
    color: black;
    border-radius: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .result-label {
    margin-top: 3vh;
    margin-bottom: 4vh;
    font-size: 18px;
    font-weight: bold;
    color: black;
  }
  
  .bank-item {
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 10px;
    transition: background-color 0.3s;
  }
  
  .bank-item:hover {
    background-color: #f9f9f9;
  }
  
  .bank-item-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .bank-item-title {
    color: black;
    font-size: 16px;
    font-weight: bold;
  }
  </style>
  
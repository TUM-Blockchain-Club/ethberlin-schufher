<template>
    <Header />
    <v-container class="fill-height">
        <v-row justify="center" class="main-content">
            <v-col cols="12" md="10" lg="8">
                <v-card class="multistep-form" elevation="10">
                    <v-card-text>
                        <v-form @submit.prevent="submitForm">
                            <div class="step-indicator">STEP {{ step }} of 2</div>
                            <div v-if="step === 1">
                                <v-row>
                                    <v-col cols="12" md="6">
                                        <div class="field-label">Salutation</div>
                                        <v-select v-model="form.salutation" :items="['Male', 'Female', 'Unknown']"
                                            variant="solo"></v-select>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <div class="field-label">Name</div>
                                        <v-text-field v-model="form.name" variant="solo"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <div class="field-label">Surname</div>
                                        <v-text-field v-model="form.surname" variant="solo"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <div class="field-label">Email</div>
                                        <v-text-field v-model="form.email" variant="solo"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <div class="field-label">Street</div>
                                        <v-text-field v-model="form.street" variant="solo"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <div class="field-label">House Number</div>
                                        <v-text-field v-model="form.houseNumber" type="number"
                                            variant="solo"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <div class="field-label">Postcode</div>
                                        <v-text-field v-model="form.postcode" type="number"
                                            variant="solo"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <div class="field-label">Country</div>
                                        <v-text-field v-model="form.country" variant="solo"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <div class="field-label">Birthday</div>
                                        <v-text-field v-model="form.birthday" variant="solo"></v-text-field>
                                    </v-col>
                                </v-row>
                                <v-btn @click="nextStep" color="#76ABAE" block large
                                    class="rounded-btn white-text short-btn">Next</v-btn>
                            </div>
                            <div v-else-if="step === 2">
                                <v-row>
                                    <v-col cols="12">
                                        <div class="checkbox-item">
                                            <v-checkbox v-model="form.checkbox1"></v-checkbox>
                                            <div class="checkbox-content">
                                                <div class="checkbox-header">PRIVACY POLICY</div>
                                                <div class="checkbox-description">
                                                    Privacy Policy outlines how we collect, use, and protect your
                                                    personal information. By checking
                                                    the checkbox, you agree to these terms regarding the handling of
                                                    your data. Click here to read it.
                                                </div>
                                            </div>
                                        </div>
                                    </v-col>
                                    <v-col cols="12">
                                        <div class="checkbox-item">
                                            <v-checkbox v-model="form.checkbox2"></v-checkbox>
                                            <div class="checkbox-content">
                                                <div class="checkbox-header">SERVICE AGREEMENT</div>
                                                <div class="checkbox-description">
                                                    Service Agreement defines the terms and conditions under which our
                                                    credit scoring services are
                                                    provided. It covers aspects such as the scope of our services,
                                                    pricing, payment terms, and the
                                                    process of calculating and delivering credit scores to users. Users
                                                    are required to agree to these
                                                    terms to access and use our products. Click here to read it.
                                                </div>
                                            </div>
                                        </div>
                                    </v-col>
                                    <v-col cols="12">
                                        <div class="checkbox-item">
                                            <v-checkbox v-model="form.checkbox3"></v-checkbox>
                                            <div class="checkbox-content">
                                                <div class="checkbox-header">USER AGREEMENT</div>
                                                <div class="checkbox-description">
                                                    User Agreement governs your use of our credit scoring platform. It
                                                    specifies the rules and
                                                    guidelines for accessing and using the platform, including
                                                    acceptable behavior, prohibited
                                                    activities, and account security measures. By accessing and using
                                                    our products, users agree to
                                                    abide by the terms outlined in this agreement. Click here to read
                                                    it.
                                                </div>
                                            </div>
                                        </div>
                                    </v-col>
                                </v-row>
                                <v-btn @click="prevStep" color="#76ABAE" block
                                    class="rounded-btn white-text short-btn">Back</v-btn>
                                <v-btn :disabled="!allChecked" @click="submitForm" color="#76ABAE" block large
                                    class="rounded-btn white-text short-btn">Submit</v-btn>
                            </div>
                        </v-form>
                    </v-card-text>
                    <div class="horizontal-line"></div>
                </v-card>
            </v-col>
        </v-row>
        <Footer />
    </v-container>
</template>

<script>
import Header from '@/components/HeaderLoggedIn.vue';
import Footer from '@/components/Footer.vue';

export default {
    components: {
        Header,
        Footer
    },
    data() {
        return {
            step: 1,
            form: {
                salutation: '',
                name: '',
                surname: '',
                email: '',
                street: '',
                houseNumber: '',
                postcode: '',
                country: '',
                birthday: '',
                checkbox1: false,
                checkbox2: false,
                checkbox3: false
            },
            banksData: null,
            score: null
        };
    },
    computed: {
        allChecked() {
            return this.form.checkbox1 && this.form.checkbox2 && this.form.checkbox3;
        }
    },
    methods: {
        nextStep() {
            if (this.step < 2) {
                this.step++;
            }
        },
        prevStep() {
            if (this.step > 1) {
                this.step--;
            }
        },
        async fetchScore() {
            const fallbackScore = 81;  // for demo purposes only (no prod)
            try {
                const response = await fetch('https://de1c-35-187-154-238.ngrok-free.app/get_score/3', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'ngrok-skip-browser-warning': '42'
                    },
                });
                const data = await response.json();
                return data.score || fallbackScore;
            } catch (error) {
                console.error('Error fetching score:', error);
                return fallbackScore;
            }
        },
        async fetchBanksList() {
            const fallbackBanks = ["DemoBank", "N92", "Revola", "Banksta"]; // for demo purposes only (no prod)
            try {
                const response = await fetch('http://localhost:8042/api/v1/institutions?uid=3', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });
                const data = await response.json();
                return data.banks && data.banks.length > 0 ? data.banks : fallbackBanks;
            } catch (error) {
                console.error('Error fetching banks list:', error);
                return fallbackBanks;
            }
        },
        async submitForm() {
            try {
                const score = await this.fetchScore();
                const banks = await this.fetchBanksList();
                console.log('Banks:', banks);
                console.log('Score:', score);
                if (banks && score) {
                    this.$store.dispatch('updateBanksData', banks);
                    this.$store.dispatch('updateScore', score);
                    this.$router.push({ name: 'results' });
                } else {
                    console.error('Incomplete data:', banks, score);
                }
            } catch (error) {
                console.error('Error submitting form:', error);
            }
        }
    }
};
</script>

<style scoped>
.fill-height {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.main-content {
    flex: 1;
}

.multistep-form {
    width: 100%;
    padding: 20px;
    background-color: #222831;
    color: white;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.field-label {
    font-size: 14px;
    color: white;
    margin-bottom: 5px;
}

.v-card-text {
    margin-top: 20px;
}

.horizontal-line {
    border-top: 2px solid #76ABAE;
    margin: 10px 0;
}

.rounded-btn {
    border-radius: 40px;
    width: 50%;
    margin: 20px;
}

.short-btn {
    margin: 20px;
}

.black-text-btn {
    color: black !important;
}

.white-text {
    color: white !important;
}

.text-center {
    text-align: center;
}

.mb-4 {
    margin-bottom: 16px;
}

.step-indicator {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: white;
    margin-bottom: 20px;
    padding: 10px;
    border: 2px solid #76ABAE;
    border-radius: 10px;
}

.checkbox-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 20px;
}

.checkbox-content {
    margin-left: 10px;
}

.checkbox-header {
    font-size: 18px;
    text-transform: uppercase;
    font-weight: bold;
    color: white;
    margin-left: 20px;
}

.checkbox-description {
    font-size: 14px;
    color: white;
    margin-left: 20px;
}

.checkbox-description a {
    color: #76ABAE;
    text-decoration: underline;
}
</style>

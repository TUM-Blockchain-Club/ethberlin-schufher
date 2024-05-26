<template>
  <div class="home-container">
    <Header />
    <div class="content">
      <div class="split-container">
        <div class="left-side">
          <v-img :src="handsImageSrc" alt="Office Image" class="left-image" cover></v-img>
        </div>
        <div class="right-side">
          <LoginForm />
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import LoginForm from '@/components/LoginForm.vue'

const handsImageSrc = new URL('@/assets/images/hands.jpg', import.meta.url).href;

</script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.content {
  flex: 1;
  display: flex;
  background-color: #222831;
}

.split-container {
  display: flex;
  flex: 1;
  width: 100%;
  height: 100%;
}

.left-side {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.left-image {
  width: 100%;
  height: auto;
  max-height: 90vh;
  object-fit: cover;
  object-position: center;
}

.right-side {
  flex: 1;
  background-color: #222831;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}
</style>

<template>
  <div class="home-container">
    <Header />
    <div class="content">
      <div class="split-container">
        <div class="left-side">
          <img src="@/assets/images/hands.jpg" alt="Office Image" class="left-image" />
        </div>
        <div class="right-side">
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
</script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
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
  height: 100%;
  object-fit: cover;
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

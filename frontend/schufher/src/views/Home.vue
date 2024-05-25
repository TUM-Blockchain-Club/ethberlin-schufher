<template>
    <div class="app-container">
      <Header />
      <div class="content">
        <!-- Add your content here -->
      </div>
      <Footer />
    </div>
  </template>
  
  <script setup>
  import Header from '@/components/Header.vue'
  import Footer from '@/components/Footer.vue'
  </script>
  
  <style scoped>
  .app-container {
    display: flex;
    flex-direction: column;
    height: 95vh;
  }
  
  .content {
    flex: 1;
    overflow-y: auto;
  }
  </style>
  
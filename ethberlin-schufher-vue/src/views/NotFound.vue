<template>
    <main>
        <Header />
        <div class="centered-content">
            <p class="questionmark-icon">?</p>
            <h2 class="notfound-message">Error 404 - Not Found</h2>
            <p class="big-paragraph">The page you're trying to access does not exist.
                It might be misspelled or currently unavailable.</p>
            <p class="big-paragraph"><b>Please check the URL or try again later.</b></p>
        </div>
        <Footer />
    </main>
</template>
  
<script setup>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
</script>
  
<style scoped>
.centered-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 90vh;
    text-align: center;
    margin-top: -200px;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
}

.questionmark-icon {
    font-size: 200px;
    font-weight: 400;
    line-height: 300px;
    color: rgba(0, 0, 0, 0.5);
}

.notfound-message {
    font-size: 40px;
    font-weight: 700;
    line-height: 60px;
}

.big-paragraph {
    font-size: 21px;
    font-weight: 400;
    line-height: 32px;
    margin-top: 10px;
}

.big-paragraph b {
    font-weight: 700;
}</style>
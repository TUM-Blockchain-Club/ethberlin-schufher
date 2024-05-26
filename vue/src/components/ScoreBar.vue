<template>
    <div class="score-bar-container">
      <v-row>
        <v-col v-for="segment in segments" :key="segment.value" class="pa-1">
          <v-card :class="segmentClass(segment.value)" class="score-segment"></v-card>
        </v-col>
      </v-row>
      <div class="arrow" :style="arrowStyle">▼</div>
      <div class="score-label" :style="arrowStyle">{{ score }}</div>
      <v-row justify="space-between" class="legend">
        <v-col v-for="segment in segments" :key="segment.value" class="pa-1">
          <span>{{ segment.value }}</span>
        </v-col>
      </v-row>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      score: {
        type: Number,
        required: true
      }
    },
    computed: {
      segments() {
        return [
          { value: 20, color: 'red' },
          { value: 40, color: 'orange' },
          { value: 60, color: 'yellow' },
          { value: 80, color: 'lightgreen' },
          { value: 100, color: 'green' }
        ];
      },
      arrowStyle() {
        const position = this.score / 100 * 90;
        return {
          left: `calc(${position}% - 10px)`
        };
      }
    },
    methods: {
      segmentClass(value) {
        const segment = this.segments.find(seg => seg.value === value);
        return {
          'low': this.score < value,
          'high': this.score >= value,
          [segment.color]: true
        };
      }
    }
  };
  </script>
  
  <style scoped>
  .score-bar-container {
    position: relative;
    width: 100%;
    margin-bottom: 20px;
  }
  
  .score-segment {
    width: 100%;
    height: 30px;
    border-radius: 5px;
  }
  
  .low {
    opacity: 0.4;
  }
  
  .high {
    opacity: 1;
  }
  
  .red {
    background-color: red;
  }
  
  .orange {
    background-color: orange;
  }
  
  .yellow {
    background-color: yellow;
  }
  
  .lightgreen {
    background-color: lightgreen;
  }
  
  .green {
    background-color: green;
  }
  
  .arrow {
    position: absolute;
    top: 35px;
    font-size: 24px;
    color: red;
  }
  
  .score-label {
    position: absolute;
    top: 60px;
    font-size: 18px;
    color: black;
    text-align: center;
    width: 40px;
  }
  
  .legend {
    font-size: 14px;
    color: black;
    margin-top: 10px;
  }
  </style>
  
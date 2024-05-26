<template>
  <div class="score-bar-container">
    <v-row>
      <v-col v-for="segment in segments" :key="segment.value" class="pa-1">
        <v-card :class="segmentClass(segment.value)" class="score-segment"></v-card>
      </v-col>
    </v-row>
    <div class="arrow" :style="arrowStyle">▼</div>
    <div class="score-label" :style="arrowStyle">{{ score }}</div>
    <div class="legend">
      <span v-for="(segment, index) in legendTicks" :key="index" :style="legendTickStyle(segment.position)">
        <div class="tick-line"></div>
        {{ segment.value }}
      </span>
    </div>
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
        { value: 0, color: 'red' },
        { value: 20, color: 'light-red' },
        { value: 40, color: 'orange' },
        { value: 60, color: 'yellow' },
        { value: 80, color: 'green' }
      ];
    },
    legendTicks() {
      return [
        { value: 0, position: 0 },
        { value: 50, position: 50 },
        { value: 100, position: 100 }
      ];
    },
    arrowStyle() {
      const score_h = 81;
      const position = score_h / 100 * 100;
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
    },
    legendTickStyle(position) {
      return {
        position: 'absolute',
        left: `${position}%`,
        transform: 'translateX(-50%)'
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
  height: 60px;
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

.light-red {
  background-color: #ff6666;
}

.orange {
  background-color: orange;
}

.yellow {
  background-color: yellow;
}

.green {
  background-color: green;
}

.arrow {
  position: absolute;
  top: -30px;
  font-size: 24px;
  color: red;
}

.score-label {
  position: absolute;
  top: -55px;
  font-size: 18px;
  color: black;
  text-align: center;
  width: 40px;
}

.legend {
  position: relative;
  font-size: 14px;
  color: black;
  margin-top: 10px;
  height: 20px;
}

.legend span {
  position: absolute;
  bottom: -20px;
  text-align: center;
}

.tick-line {
  height: 10px;
  border-left: 2px solid black;
  margin-bottom: 2px;
}
</style>

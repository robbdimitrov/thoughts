<template>
  <div class="container">
    <thought-item></thought-item>
    <thought-item></thought-item>
    <thought-item></thought-item>
  </div>
</template>

<script>
import ThoughtItem from '../components/ThoughtItem.vue';

export default {
  components: {
    ThoughtItem
  }
};
</script>

<style scoped>
.container {
  background: white;
}
</style>

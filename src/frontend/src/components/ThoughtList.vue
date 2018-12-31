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

article {
  border-bottom: 1px solid #e6ecf0;
}

article:last-child {
  border-bottom: none;
}
</style>

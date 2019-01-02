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

<style lang="scss" scoped>
.container {
  flex-direction: column;
  background: white;
}

.container > article {
  width: 100%;
  border-bottom: 1px solid #e6ecf0;
}

article:last-child {
  border-bottom: none;
}
</style>

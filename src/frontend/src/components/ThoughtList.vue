<template>
  <div class="container">
    <thought-item class="item" />
    <thought-item class="item" />
    <thought-item class="item" />
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
}

.item {
  width: 100%;
  border-bottom: 1px solid #e6ecf0;
}

.item:last-child {
  border-bottom: none;
}
</style>

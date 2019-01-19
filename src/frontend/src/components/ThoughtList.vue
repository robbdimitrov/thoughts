<template>
  <div class="container">
    <thought-item v-for="item in items" :key="item"
      class="list-item" />
  </div>
</template>

<script>
import ThoughtItem from '../components/ThoughtItem.vue';

export default {
  components: {
    ThoughtItem
  },
  props: {
    items: Number
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/colors";
@import "../styles/helpers";

.container {
  flex-direction: column;
}

.list-item {
  width: 100%;
  @include separator;

  &:last-child {
    border-bottom: none;
  }
}
</style>

<template>
  <div id="app">
    <feed-view></feed-view>
  </div>
</template>

<script>
import FeedView from './views/FeedView.vue';

export default {
  name: 'app',
  components: {
    FeedView
  }
};
</script>

<style lang="scss">
@import 'styles/main';

body {
  background: $background-color;
  color: $primary-text-color;
}
</style>

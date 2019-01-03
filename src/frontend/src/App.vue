<template>
  <div id="app">
    <navigation-bar class="nav"></navigation-bar>
    <feed-view></feed-view>
  </div>
</template>

<script>
import FeedView from './views/FeedView.vue';
import NavigationBar from './components/NavigationBar.vue'

export default {
  name: 'app',
  components: {
    FeedView,
    NavigationBar
  }
};
</script>

<style lang="scss">
@import "styles/main";

body {
  background: $background-color;
  color: $primary-text-color;
}
</style>

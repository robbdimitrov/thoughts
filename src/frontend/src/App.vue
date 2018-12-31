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

<style>
body {
  font-family: 'Roboto', sans-serif;
  background: #e6ecf0;
}
</style>


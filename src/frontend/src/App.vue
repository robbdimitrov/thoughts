<template>
  <div id="app">
    <navigation-bar />
    <router-view />
  </div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue';

export default {
  name: 'app',
  components: {
    NavigationBar
  }
};
</script>

<style lang="scss">
@import "styles/main";
</style>

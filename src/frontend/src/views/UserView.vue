<template>
  <div class="container">
    <user-header></user-header>

    <control-bar></control-bar>

    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import ControlBar from '../components/ControlBar.vue';
import UserHeader from '../components/UserHeader.vue';

export default {
  name: 'user-view',
  components: {
    ControlBar,
    UserHeader
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";

.content {
  width: 100%;
  max-width: $content-main-width;
  margin: $spacing-md 0;
  margin-left: auto;
  margin-right: auto;
}
</style>

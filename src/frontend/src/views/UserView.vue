<template>
  <div class="container">
    <user-header />
    <control-bar />

    <div class="content main-content">
      <router-view />
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
  margin-top: $spacing-md;
  margin-bottom: $spacing-md;
}
</style>

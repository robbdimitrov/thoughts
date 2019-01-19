<template>
  <div class="container">
    <settings-nav class="nav" />

    <div class="content main-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import SettingsNav from '../components/SettingsNav.vue';

export default {
  name: 'settings-view',
  components: {
    SettingsNav
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";

.container {
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.nav {
  width: $content-secondary-width;
  margin: $spacing-md;
  margin-left: 0;
}

.content {
  background: $primary-color;
  margin-left: 0;
  margin-right: 0;
}

.content {
  margin-top: $spacing-md;
  margin-bottom: $spacing-md;
}

@media screen and (max-width: $break-md) {
  .container {
    flex-direction: column;
    align-items: center
  }

  .nav {
    margin: 0;
    width: 100%;
    max-width: $content-main-width;
  }
}
</style>

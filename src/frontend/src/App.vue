<template>
  <div id="app">
    <thought-overlay
      v-if="isPopupShown"
      v-on:close-popup="closePopup"
    />

    <navigation-bar v-on:open-popup="openPopup" />

    <router-view />
  </div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue';
import ThoughtOverlay from './views/ThoughtOverlay.vue';

export default {
  name: 'app',
  components: {
    NavigationBar,
    ThoughtOverlay
  },
  data: function () {
    return {
      isPopupShown: false
    };
  },
  methods: {
    openPopup: function () {
      this.isPopupShown = true;
    },
    closePopup: function () {
      this.isPopupShown = false;
    }
  }
};
</script>

<style lang="scss">
@import "styles/main";
</style>

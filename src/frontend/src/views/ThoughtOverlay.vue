<template>
  <div class="overlay">
    <thought-box
      class="popup"
      v-on:close-popup="$emit('close-popup')"
      v-on:create-post="createPost"
    />
  </div>
</template>

<script>
import ThoughtBox from '../components/ThoughtBox.vue';

export default {
  name: 'thought-overlay',
  components: {
    ThoughtBox
  },
  methods: {
    createPost: function (text) {
      console.log(`Create Post: ${text}`);
      this.$emit('close-popup');
    }
  }
};
</script>

<style lang="scss">
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";

.overlay {
  @include full-screen;
  background: $dark-background-color;
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  overflow-y: scroll;
  z-index: $z-index-popup;
}
</style>

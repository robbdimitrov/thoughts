<template>
  <div class="container main-content">
    <thought-item />
  </div>
</template>

<script>
import ThoughtItem from '../components/ThoughtItem.vue';

export default {
  name: 'profile-view',
  components: {
    ThoughtItem
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";

.container {
  margin-top: $spacing-md;
  margin-bottom: $spacing-md;
}
</style>

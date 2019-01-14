<template>
  <div class="container main-content">
    <thought-list :items="1" />
  </div>
</template>

<script>
import ThoughtList from '../components/ThoughtList.vue';

export default {
  name: 'profile-view',
  components: {
    ThoughtList
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

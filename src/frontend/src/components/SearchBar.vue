<template>
  <div class="container">
    <div class="content main-container">
      <input
        class="search-input"
        type="text"
        placeholder="Start typing..."
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'search-term-bar'
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";

$search-bar-background: #35393C;

.container {
  background: $search-bar-background;
}

.content {
  padding: $spacing-md 0;
  display: flex;
}

.search-input {
  background: $search-bar-background;
  font-size: rem(28);
  color: $primary-color;
  font-weight: $font-weight-semibold;
  margin: 0 $spacing-sm;
  flex: 1;
}
</style>

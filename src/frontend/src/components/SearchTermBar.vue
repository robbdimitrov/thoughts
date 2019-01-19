<template>
  <div class="container">
    <div class="content main-container">
      <span class="search-term">Search term</span>
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

$search-term-background: #35393C;

.container {
  background: $search-term-background;
  height: $button-height;
  padding: $spacing-sm 0;
}

.search-term {
  padding-left: 12px;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-size: rem(27);
  color: $primary-color;
  font-weight: $font-weight-semibold;
}
</style>

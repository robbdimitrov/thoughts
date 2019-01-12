<template>
  <div class="container">
    <i class="icon fas fa-search"></i>
    <input class="search-input" type="text"
      placeholder="Search Thoughts">
  </div>
</template>

<script>
export default {
  name: 'search-bar'
};
</script>

<style lang="scss" scoped>
@import "../styles/fonts";
@import "../styles/helpers";
@import "../styles/colors";
@import "../styles/variables";

.container {
  display: flex;
  border: 1px solid black;
  padding-left: $padding;
  padding-right: $padding;
}

.icon {
  font-size: 15px;
  margin-right: $padding / 2;
}

.search-input {
  font-weight: $font-weight-regular;
  font-size: rem(14);
  background: $background-color;
}
</style>

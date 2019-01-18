<template>
  <div class="container">
    <div class="content main-container">
      <div class="scope-nav-item active">
        <span class="scope-nav-item-title">
          All
        </span>
      </div>

      <div class="scope-nav-item">
        <span class="scope-nav-item-title">
          People
        </span>
      </div>

      <div class="scope-nav-item">
        <span class="scope-nav-item-title">
          Tweets
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'search-scope-bar'
}
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/colors";
@import "../styles/helpers";

.container {
  background: white;
  height: $bar-height;
}

.content {
  height: 100%;
}

.scope-nav-item {
  display: inline-flex;
  align-items: center;
  height: 100%;
  text-decoration: none;
  padding: 0 $padding;
  box-sizing: border-box;
}

.scope-nav-item-title {
  font-size: rem(14);
  font-weight: $font-weight-semibold;
}

.scope-nav-item.active {
  @include active-border;
}
</style>

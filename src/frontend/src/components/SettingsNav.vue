<template>
  <div class="container">
    <div class="nav-header nav-item">
      <span class="nav-item-title">
        Settings
      </span>
    </div>

    <div class="nav-item">
      <span class="nav-item-title">
        Edit profile
      </span>
    </div>

    <div class="nav-item active">
      <span class="nav-item-title">
        Change password
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'settings-nav'
}
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";

.container {
  background: $primary-color;
  flex-direction: column;
  width: 100%;
}

.nav-item {
  font-size: rem(17);
  width: 100%;
  @include separator;

  &:last-child {
    border-bottom: none;
  }

  &:hover {
    background: $selected-color;
  }
}

.nav-item.active {
  border-left: 2px solid $active-color;

  .title {
    margin-left: $spacing-sm - 2px;
  }
}

.nav-item.active, .nav-item.active:hover {
  &:hover {
    background: $primary-color;
  }
}

.nav-header, .nav-header:hover {
  font-weight: $font-weight-semibold;
  background: $secondary-color;
  font-size: rem(18);
}

.nav-item-title {
  margin: $spacing-sm;
  display: block;
}
</style>

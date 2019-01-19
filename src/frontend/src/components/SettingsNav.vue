<template>
  <div class="container">
    <div class="nav-header nav-item">
      <span class="nav-item-title">
        Settings
      </span>
    </div>

    <router-link to="/settings/account" class="nav-item nav-element">
      <span class="nav-item-title">
        Edit profile
      </span>
    </router-link>

    <router-link to="/settings/password" class="nav-item nav-element">
      <span class="nav-item-title">
        Change password
      </span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'settings-nav'
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";

$active-item-width: 4px;

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
}

.nav-element {
  box-sizing: border-box;
  text-decoration: none;
  color: $primary-text-color;

  &:hover {
    background: $selected-color;
  }

  &.router-link-active {
    border-left: $active-item-width solid $active-color;

    .nav-item-title {
      margin-left: $spacing-sm - $active-item-width;
    }

    &:hover {
      background: $primary-color;
    }
  }
}

.nav-header {
  font-weight: $font-weight-semibold;
  background: $secondary-color;
  font-size: rem(18);
}

.nav-item-title {
  margin: $spacing-sm;
  display: block;
}
</style>

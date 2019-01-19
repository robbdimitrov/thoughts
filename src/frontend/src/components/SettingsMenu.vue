<template>
  <div class="dropdown">
    <router-link to="/user" class="dropdown-item">
      <span class="dropdown-item-title">
        Profile
      </span>
    </router-link>

    <router-link to="/settings" class="dropdown-item">
      <span class="dropdown-item-title">
        Settings
      </span>
    </router-link>

    <router-link to="/" class="dropdown-item">
      <span class="dropdown-item-title">
        Sign out
      </span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'settings-menu'
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/colors";
@import "../styles/fonts";
@import "../styles/helpers";

.dropdown {
  background: white;
  @include border;
  box-shadow: 0 3px 12px $shadow-color;
}

.dropdown-item-title {
  margin: $spacing-sm;
  display: inline-block;
}

.dropdown-item {
  font-size: rem(17);
  @include separator;
  display: block;
  color: $primary-text-color;

  &:last-child {
    border-bottom: none;
  }

  &:hover {
    background: $selected-color;
  }
}
</style>

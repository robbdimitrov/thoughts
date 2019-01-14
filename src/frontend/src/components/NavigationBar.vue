<template>
  <header class="container bottom-shadow">
    <div class="content">
      <div class="left-items">
        <router-link to="/" exact class="home-button nav-button">
          <i class="nav-button-icon fas fa-home"></i>
          <span class="nav-button-label">Home</span>
        </router-link>

        <router-link to="/search" class="search-button nav-button">
          <i class="nav-button-icon fas fa-search"></i>
          <span class="nav-button-label">Search</span>
        </router-link>
      </div>

      <i class="icon fas fa-brain"></i>

      <div class="right-items">
        <search-bar class="search-bar"></search-bar>

        <router-link to="/user" class="profile-button">
          <img class="profile-button-image"
            src="https://via.placeholder.com/300.png"
            alt="Profile" />
        </router-link>

        <button class="button create-button">
          Create
        </button>
      </div>
    </div>
  </header>
</template>

<script>
import SearchBar from './SearchBar.vue'

export default {
  name: 'navigation-bar',
  components: {
    SearchBar
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/colors";
@import "../styles/fonts";
@import "../styles/helpers";

$icon-width: 30px;
$icon-font-size: 21px;

.container {
  display: flex;
  flex-direction: row;
  align-items: center;
  background: white;
  height: $bar-height;
}

.content {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
  max-width: $max-component-width;
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 100%;
  justify-content: space-between;
}

.nav-button {
  text-decoration: none;
  color: $primary-text-color;
  height: 100%;
  display: flex;
  box-sizing: border-box;
  align-items: center;
}

.nav-button.router-link-active {
  color: $active-nav-button-color;
  border-bottom: 2px solid $active-nav-button-color;
}

.left-items {
  height: 100%;
  display: flex;
}

.nav-button-icon {
  font-size: $icon-font-size;
}

.search-button {
  margin-left: $padding;
}

.nav-button-label {
  font-weight: $font-weight-semibold;
  font-size: rem(15);
  margin-left: $padding / 2;
}

.icon {
  width: $icon-width;
  height: $icon-font-size;
  left: 50%;
  position: absolute;
  margin-left: -($icon-width / 2);
  color: $active-color;
}

.profile-button {
  width: $icon-width;
  height: $icon-width;
}

.profile-button-image {
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

.right-items {
  display: flex;
  align-items: center;
}

.create-button {
  margin-left: $padding;
}

.search-bar {
  height: $icon-width;
  border-radius: $icon-width / 2;
  background: $background-color;
  margin-right: $padding;
}

@media screen and (max-width: $break-md) {
  .search-bar {
    display: none;
  }
}

@media screen and (min-width: $break-md) {
  .search-button {
    display: none;
  }
}
</style>

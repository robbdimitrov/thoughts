<template>
  <div class="container">
    <div class="left-items">
      <button class="home-button nav-button">
        <i class="nav-button-icon fas fa-home"></i>
        <span class="nav-button-label">Home</span>
      </button>

      <button class="search-button nav-button">
        <i class="nav-button-icon fas fa-search"></i>
        <span class="nav-button-label">Search</span>
      </button>
    </div>

    <i class="icon fas fa-brain"></i>

    <div class="right-items">
      <search-bar class="search-bar"></search-bar>

      <button class="profile-button">
        <img class="profile-button-image"
          src="https://via.placeholder.com/300.png"
          alt="Profile" />
      </button>

      <button class="button create-button">
        Create
      </button>
    </div>
  </div>
</template>

<script>
import SearchBar from './SearchBar.vue'

export default {
  name: 'navigation-bar',
  components: {
    SearchBar
  }
}
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/colors";
@import "../styles/fonts";
@import "../styles/helpers";

$icon-width: 30px;
$icon-font-size: 21px;
$bar-height: 46px;

.container {
  display: flex;
  flex-direction: row;
  align-items: center;
  background: white;
  height: $bar-height;
  justify-content: space-between;
  border-bottom: 1px solid rgba(0, 0, 0, 0.25);
}

.nav-button {
  height: $icon-width;
}

.left-items {
  margin-left: 5%;
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
  color: #1da1f2;
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
  margin-right: 5%;
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

<template>
  <header class="container bottom-shadow">
    <div class="content main-container">
      <div class="left-items">
        <router-link to="/feed" class="nav-button">
          <i class="nav-button-icon fas fa-home"></i>
          <span class="nav-button-label">Home</span>
        </router-link>

        <router-link to="/search" class="nav-button">
          <i class="nav-button-icon fas fa-search"></i>
          <span class="nav-button-label">Search</span>
        </router-link>
      </div>

      <i class="icon fas fa-brain"></i>

      <div class="right-items">
        <div class="profile-button" @click="toggleDropdown">
          <img
            class="profile-button-image"
            src="https://via.placeholder.com/300.png"
            alt="Profile"
          />

          <settings-menu v-if="isDropdownShown" />
        </div>

        <button class="button create-button" @click="showPopup">
          Create
        </button>
      </div>
    </div>

    <div class="overlay" v-if="isPopupShown">
      <thought-box class="popup" />
    </div>
  </header>
</template>

<script>
import SettingsMenu from './SettingsMenu.vue';
import ThoughtBox from './ThoughtBox.vue';

export default {
  name: 'navigation-bar',
  components: {
    SettingsMenu,
    ThoughtBox
  },
  data: function () {
    return {
      isDropdownShown: false,
      isPopupShown: false
    };
  },
  methods: {
    toggleDropdown: function () {
      this.isDropdownShown = !this.isDropdownShown;
      console.log('herro there!');
    },
    showPopup: function () {
      this.isPopupShown = true;
    },
    hidePopup: function () {
      this.isPopupShown = false;
    }
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
  background: $primary-color;
  height: $bar-height;
}

.content {
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 100%;
  justify-content: space-between;
}

.dropdown {
  position: relative;
  width: $content-secondary-width;
  z-index: $z-index-dropdown;
  border-radius: $border-radius-xs;
  left: -$content-secondary-width + $icon-width;
}

.nav-button {
  text-decoration: none;
  color: $primary-text-color;
  display: flex;
  align-items: center;
  margin-right: $padding;
}

.nav-button.router-link-active {
  color: $active-nav-button-color;
  @include active-border;
}

.left-items {
  height: 100%;
  display: flex;
}

.nav-button-icon {
  font-size: $icon-font-size;
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

.overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba($color: #000000, $alpha: 0.5);
  display: flex;
  align-content: center;
  align-items: center;

  .popup {
    width: 100%;
    margin: auto;
    max-width: $content-primary-width;
    height: 160px;
  }
}

@media screen and (max-width: $break-sm) {
  .dropdown {
    position: absolute;
    width: 100%;
    border-radius: 0;
    left: 0;
  }
}
</style>

<template>
  <div class="container bottom-shadow">
    <div class="control-bar main-content">
      <nav class="counters">
        <router-link to="/user" exact class="counter thoughts">
          <span class="counter-label">Thoughts</span>
          <span class="counter-value">140</span>
        </router-link>

        <router-link to="/user/following" class="counter following">
          <span class="counter-label">Following</span>
          <span class="counter-value">70</span>
        </router-link>

        <router-link to="/user/followers" class="counter followers">
          <span class="counter-label">Followers</span>
          <span class="counter-value">250</span>
        </router-link>

        <router-link to="/user/likes" class="counter likes">
          <span class="counter-label">Likes</span>
          <span class="counter-value">98</span>
        </router-link>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: 'control-bar'
}
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";
@import "../styles/colors";

.container {
  background: white;
}

.control-bar {
  height: rem(50);
  align-items: center;
}

.counters {
  height: 100%;
  justify-content: space-around;
}

.counter {
  width: 24%;
  justify-content: center;
  text-decoration: none;
  color: $primary-text-color;
  padding: 0 $padding;
}

.counter.router-link-active {
  border-bottom: 2px solid $active-nav-button-color;
}

.counter-label {
  font-size: rem(14);
  font-weight: $font-weight-semibold;
}

.counter-value {
  font-size: rem(17);
  font-weight: $font-weight-bold;
}
</style>

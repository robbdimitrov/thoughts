<template>
  <div class="container">
    <div class="header">
      <div class="cover"></div>

      <img class="avatar"
        src="https://via.placeholder.com/300.png" />
    </div>

    <div class="control-bar-container bottom-shadow">
      <div class="control-bar">
        <nav class="counters">
          <div class="counter active">
            <span class="counter-label">Thoughts</span>
            <span class="counter-value">140</span>
          </div>

          <div class="counter">
            <span class="counter-label">Following</span>
            <span class="counter-value">70</span>
          </div>

          <div class="counter">
            <span class="counter-label">Followers</span>
            <span class="counter-value">250</span>
          </div>

          <div class="counter">
            <span class="counter-label">Likes</span>
            <span class="counter-value">98</span>
          </div>
        </nav>

        <button class="edit-profile-button outline-button">
          Edit profile
        </button>
      </div>
    </div>

    <div class="content">
      <div class="user-info">
        <span class="name">John Smith</span>
        <span class="username">@johnsmith</span>
        <p class="bio">A secret agent, Forbes man of the year</p>
        <span class="join-date">Joined March 2011</span>
      </div>

      <thought-list class="content-list"></thought-list>
    </div>
  </div>
</template>

<script>
import ThoughtList from '../components/ThoughtList.vue';

export default {
  name: 'user-view',
  components: {
    ThoughtList
  }
}
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";
@import "../styles/colors";

.cover {
  background: lightblue;
  height: 150px;
}

.user-info {
  margin-top: 80px;

  span {
    display: block;
  }
}

.header {
  position: relative;
}

.avatar {
  border: 4px solid white;
  width: 200px;
  height: 200px;
  position: absolute;
  margin-left: 3%;
  bottom: -80px;
}

.content {
  display: flex;
}

.content-list {
  width: $item-list-width;
}

.control-bar-container {
  background: white;
}

.control-bar {
  display: flex;
  height: 60px;
  width: 90%;
  max-width: 860px;
  justify-content: space-between;
  margin-left: auto;
  margin-right: auto;
  align-items: center;
}

.counters {
  margin-left: 10%;
  height: 100%;
}

.counter {
  justify-content: center;
  padding-left: $padding * 1.5;
  padding-right: $padding * 1.5;
}

.counter.active {
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

@media screen and (min-width: $break-md) {
  .cover {
    height: 240px;
  }
}

@media screen and (min-width: $break-lg) {
  .cover {
    height: 300px;
  }
}

@media screen and (max-width: $break-sm) {
  .cover {
    height: 100px;
  }

  .content-list {
    width: 100%;
  }
}
</style>

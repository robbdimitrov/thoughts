<template>
  <div class="container">
    <div class="cover"></div>

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
        <img class="avatar"
          src="https://via.placeholder.com/300.png" />

        <div class="texts">
          <span class="name bold">John Smith</span>
          <span class="username">@johnsmith</span>
          <p class="bio">A secret agent, Forbes man of the year</p>
          <div class="join-date">
            <i class="join-date-icon far fa-calendar-alt"></i>
            <span class="join-date-text">Joined March 2011</span>
          </div>
        </div>
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

$cover-height: 100px;
$avatar-width: 200px;
$spacing: $padding * 2;

.cover {
  background: lightblue;
  height: $cover-height * 1.5;
}

.user-info {
  margin-top: -($avatar-width * 0.9);
  width: $content-secondary-width;
  margin-right: $spacing;

  span {
    display: block;
  }
}

.avatar {
  border: 4px solid white;
  width: $avatar-width;
  height: $avatar-width;
}

.texts {
  margin: $spacing 0;
  color: $primary-text-color;
}

.name {
  font-size: rem(20);
  margin-bottom: $padding / 2;
}

.username {
  margin-bottom: $spacing;
}

.bio {
  margin-bottom: $spacing;
}

.join-date {
  .join-date-icon {
    display: inline-block;
    margin-right: rem(8);
  }

  .join-date-text {
    display: inline-block;
  }
}

.content {
  display: flex;
  justify-content: center;
}

.content-list {
  width: $content-primary-width;
  margin: $spacing 0;
}

.control-bar-container {
  background: white;
}

.control-bar {
  display: flex;
  height: 60px;
  width: 90%;
  max-width: $max-component-width;
  justify-content: space-between;
  margin-left: auto;
  margin-right: auto;
  align-items: center;
}

.counters {
  margin-left: 10%;
  height: 100%;
  color: $primary-text-color;
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
    height: $cover-height * 2.4;
  }
}

@media screen and (min-width: $break-lg) {
  .cover {
    height: $cover-height * 3;
  }
}

@media screen and (max-width: $break-sm) {
  .cover {
    height: $cover-height;
  }

  .content-list {
    width: 100%;
  }
}
</style>

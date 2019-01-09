<template>
  <div class="container">
    <div class="cover"></div>

    <div class="user-wrapper">
      <div class="user">
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
    </div>

    <control-bar></control-bar>

    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import ControlBar from '../components/ControlBar.vue';

export default {
  name: 'user-view',
  components: {
    ControlBar
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/helpers";
@import "../styles/colors";

$cover-height: 100px;
$avatar-width: 100px;
$avatar-width-small: 80px;
$spacing: $padding * 2;

.cover {
  background: lightblue;
  height: $cover-height * 1.5;
}

.avatar {
  margin-top: -$avatar-width * 0.8;
  border: 4px solid white;
  width: $avatar-width;
  height: $avatar-width;
}

.texts {
  font-size: rem(15);
  margin: $spacing 0;
  color: $primary-text-color;
}

.name {
  font-size: rem(21);
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

.edit-profile-button {
  flex-shrink: 0;
}

.content {
  width: 100%;
  max-width: $content-main-width;
  margin: $spacing 0;
  margin-left: auto;
  margin-right: auto;
}

.user-wrapper {
  background: white;
}

.user {
  width: 90%;
  max-width: 320px;
  margin: 0 auto;
  align-items: center;
  text-align: center;
  background: white;
  display: flex;
  flex-direction: column;

  span {
    display: block;
  }
}

@media screen and (max-width: $break-sm) {
  .cover {
    height: $cover-height;
  }

  .avatar {
    margin-top: -$avatar-width-small * 0.5;
    width: $avatar-width-small;
    height: $avatar-width-small;
  }
}
</style>

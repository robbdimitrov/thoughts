<template>
  <div class="container">
    <div class="cover"></div>

    <div class="content main-content">
      <img class="avatar"
        src="https://via.placeholder.com/300.png" />

      <button class="follow-button outline-button">
        Follow
      </button>

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
</template>

<script>
export default {
  name: 'user-header'
}
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/helpers";
@import "../styles/colors";

$cover-height: 100px;
$avatar-width: 100px;
$avatar-width-small: 80px;

.cover {
  background: lightblue;
  height: $cover-height * 1.5;
}

.container {
  background: white;
}

.avatar {
  margin-top: -$avatar-width * 0.6;
  margin-left: $spacing-sm;
  border: 4px solid white;
  width: $avatar-width-md;
  height: $avatar-width-md;
}

.texts {
  font-size: rem(15);
  margin: $spacing-md;
  color: $primary-text-color;
}

.name {
  font-size: rem(21);
  margin-bottom: $padding / 2;
}

.username {
  margin-bottom: $spacing-md;
}

.bio {
  margin-bottom: $spacing-md;
}

.follow-button {
  position: absolute;
  top: $padding * 1.5;
  right: $padding * 1.5;
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
  flex-direction: column;
  position: relative;

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

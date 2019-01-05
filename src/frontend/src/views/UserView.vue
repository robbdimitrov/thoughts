<template>
  <div class="container">
    <img class="avatar"
      src="https://via.placeholder.com/300.png" />

    <div class="cover"></div>

    <div class="control-bar bottom-shadow">
      <nav class="elements">
        <div class="element">
          <span class="counter-label light">Thoughts</span>
          <span class="counter-value">140</span>
        </div>

        <div class="element">
          <span class="counter-label light">Following</span>
          <span class="counter-value">70</span>
        </div>

        <div class="element">
          <span class="counter-label light">Followers</span>
          <span class="counter-value">250</span>
        </div>

        <div class="element">
          <span class="counter-label light">Likes</span>
          <span class="counter-value">98</span>
        </div>
      </nav>

      <button class="edit-profile-button">
        Edit profile
      </button>
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

.cover {
  background: lightblue;
  height: 150px;
}

.avatar {
  border: 4px solid white;
  width: 200px;
  height: 200px;
  position: absolute;
  margin-left: 3%;
  bottom: 40px;
}

.content {
  display: flex;
}

.content-list {
  width: $item-list-width;
}

.control-bar {
  background: white;
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

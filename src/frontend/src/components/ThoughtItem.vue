<template>
  <article class="container">
    <div class="context">
      <i class="context-icon fas fa-retweet"></i>
      <span class="context-label">Jonathan Key retweeted</span>
    </div>

    <div class="wrapper">
      <img class="avatar"
        src="https://via.placeholder.com/300.png" />

      <div class="content">
        <p class="profile-action">
          <strong class="name">John Doe</strong>
          <small class="username">@johndoe</small>
          <small class="time">3h</small>
        </p>

        <p class="text">Hello beautiful world! My first post!</p>

        <div class="buttons">
          <button class="retweet-button">
            <i class="button-icon fas fa-retweet"></i>
            <span class="button-label">2</span>
          </button>

          <button class="like-button">
            <i class="button-icon fas fa-heart"></i>
            <span class="button-label">3</span>
          </button>
        </div>
      </div>
    </div>
  </article>
</template>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/helpers";
@import "../styles/fonts";

$context-icon-width: 16px;

.wrapper {
  display: flex;
}

.context-icon {
  margin-left: ($avatar-width-sm + $padding) - $context-icon-width;
  width: $context-icon-width;
  margin-right: $padding;
}

.context {
  display: inline-block;
  margin-top: $padding;
  color: gray;
  font-size: rem(12);
  font-weight: $font-weight-regular;
}

.buttons > button {
  display: flex;
  align-items: center;
  border: 0;
  padding: 0;
  height: 20px;
}

.profile-action {
  margin: $padding 0 0;
}

.button-label {
  margin-left: 5px;
  font-size: rem(12);
}

.text {
  margin: $padding 0 0 0;
}

.buttons {
  display: flex;
  margin: $padding 0;
}

.avatar {
  width: $avatar-width-sm;
  height: $avatar-width-sm;
  padding: $padding;
}

.button-icon {
  width: 20px;
  height: 15px;
}

.time::before {
  content: "\00b7 ";
}

.like-button {
  margin-left: 2 * $padding;
}

.name::after, .username::after {
  content: " ";
}
</style>

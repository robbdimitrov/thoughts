<template>
  <div class="container">
    <div class="cover"></div>

    <div class="content">
      <img class="avatar"
        src="https://via.placeholder.com/300.png" />
      <div class="texts">
        <p class="title semibold">John Smith</p>
        <p class="subtitle light">@johnsmith</p>
      </div>
    </div>

    <div class="counters">
      <div class="counter">
        <span class="counter-label light">Thoughts</span>
        <span class="counter-value">2</span>
      </div>

      <div class="counter">
        <span class="counter-label light">Following</span>
        <span class="counter-value">70</span>
      </div>

      <div class="counter">
        <span class="counter-label light">Followers</span>
        <span class="counter-value">160</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/helpers";
@import "../styles/fonts";

.cover {
  height: $cover-height;
  background: lightblue;
}

.content {
  display: flex;
  flex-direction: row;
}

.container {
  background: white;
}

.avatar {
  margin: $padding;
  margin-top: -2 * $padding;
  border: 2px solid white;
}

.texts {
  margin: $padding;
  margin-left: 0;
}

.title {
  margin: 0;
}

.subtitle {
  font-size: rem(14);
  margin-top: rem(2);
}

.counters {
  margin: 0 0 $padding;
}
</style>

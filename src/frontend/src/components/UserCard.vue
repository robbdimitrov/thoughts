<template>
  <div class="container">
    <div class="cover"></div>

    <div class="content">
      <img class="avatar"
        src="https://via.placeholder.com/300.png" />
      <div class="labels">
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

.labels {
  margin: $padding;
  margin-left: 0;
}

.title {
  margin: 0;
}

.subtitle {
  margin-top: rem(2);
}

.counters {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  margin: 0 0 $padding;
}

.counter {
  display: flex;
  flex-direction: column;
  text-align: center;
}

.counter-label, .subtitle {
  font-size: rem(14);
}
</style>

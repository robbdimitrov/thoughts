<template>
  <div class="container user-card">
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

.user-card .content {
  display: flex;
  flex-direction: row;
}

.counters {
  margin: 0 0 $padding;
}

.user-card .texts {
  margin: $padding;
  margin-left: 0;
}

.user-card .title {
  margin: 0;
}
</style>

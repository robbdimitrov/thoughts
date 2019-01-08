<template>
  <div class="container">
    <div class="cover"></div>

    <div class="content">
      <img class="avatar"
        src="https://via.placeholder.com/300.png" />
      <button class="follow-button outline-button">
        Follow
      </button>
      <div class="texts">
        <p class="title semibold">John Smith</p>
        <p class="subtitle light">@johnsmith</p>

        <p class="bio">A secret agent, Forbes man of the year</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'user-item'
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";
@import "../styles/colors";

.cover {
  height: $cover-height;
  background: lightblue;
}

</style>

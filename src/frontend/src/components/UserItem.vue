<template>
  <div class="container user-card">
    <div class="cover"></div>

    <div class="content">
      <div class="header">
        <img class="avatar"
          src="https://via.placeholder.com/300.png" />

        <button class="follow-button outline-button">
          Follow
        </button>
      </div>

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

$spacing: $padding * 1.5;

.header {
  display: flex;
  justify-content: space-between;
}

.follow-button {
  margin: $padding;
}

.avatar {
  margin-left: $spacing;
}

.follow-button {
  margin: $spacing $spacing 0 0;
}

.texts {
  margin: $spacing;
}

.bio {
  font-size: rem(14);
  margin-top: rem(10);
  margin-bottom: 20px;
}
</style>

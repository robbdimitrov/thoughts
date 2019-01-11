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

$avatar-width-sm: 40px;

.container {
  box-sizing: border-box;
}

.header {
  display: flex;
  justify-content: space-between;
}

.follow-button {
  margin: $padding;
}

.avatar {
  margin-left: $spacing-sm;
}

.follow-button {
  margin: $spacing-sm $spacing-sm 0 0;
}

.texts {
  margin: $spacing-sm;
}

.bio {
  font-size: rem(14);
  margin-top: rem(10);
}

@media screen and (max-width: $break-sm) {
  .cover {
    display: none;
  }

  .header {
    display: block;
  }

  .content {
    display: flex;
  }

  .avatar {
    width: $avatar-width-sm;
    height: $avatar-width-sm;
    margin-top: $spacing-sm;
  }

  .title, .subtitle {
    width: 75%;
  }

  .follow-button {
    position: absolute;
    right: 0;
  }
}
</style>

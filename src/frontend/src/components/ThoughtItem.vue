<template>
  <div class="content">
    <div class="header">
      <div class="profile-action">
        <img :src="avatar" class="avatar" />
        <p class="name">John Doe</p>
        <p class="username">johndoe</p>
      </div>
      <p class="time">3 hours ago</p>
    </div>

    <div class="text-container">
      <p class="text">Hello beautiful world! My first post!</p>
    </div>

    <div class="footer">
      <button class="like-action">
        <span>Like</span>
        <span>2</span>
      </button>
      <button class="retweet-action">
        <span>Like</span>
        <span>3</span>
      </button>
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background-color: lightgray;
}
</style>

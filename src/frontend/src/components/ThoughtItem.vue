<template>
  <article class="container">
    <img class="avatar"
      src="https://bulma.io/images/placeholders/96x96.png" />
    <div class="content">
      <p class="profile-action">
        <strong class="name">John Doe</strong>
        <small class="username">@johndoe</small>
        <small class="time">3h</small>
      </p>

      <p class="text">Hello beautiful world! My first post!</p>

      <div class="actions">
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
  </article>
</template>

<style lang="scss" scoped>
.container, .actions, button {
  display: flex;
}

.profile-action {
  margin: 10px 0 0;
}

.button-label {
  margin-left: 0.5em;
}

.text {
  margin: 10px 0 0 0;
}

.actions {
  margin: 10px 0;
}

.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  padding: 10px;
}

.button-icon {
  width: 15px;
  height: 15px;
}

.time::before {
  content: "\00b7 ";
}

button {
  border: 0;
  padding: 0;
  height: 20px;
}

.like-button {
  margin-left: 20px;
}

.name::after, .username::after {
  content: " ";
}
</style>

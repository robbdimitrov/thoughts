<template>
  <article class="media">
    <figure class="image is-64x64 media-left">
      <img src="https://bulma.io/images/placeholders/64x64.png"
        class="is-rounded" />
    </figure>

    <div class="media-content">
      <p class="profile-action">
        <strong class="name">John Doe</strong>
        <small class="username">@johndoe</small>
        <small class="time">3h</small>
      </p>
      <p class="text">Hello beautiful world! My first post!</p>

      <div class="level is-mobile">
        <div class="level-left">
          <a class="button level-item">
            <span class="icon">
              <i class="fas fa-retweet"></i>
            </span>
            <span>2</span>
          </a>
          <a class="button level-item">
            <span class="icon">
              <i class="fas fa-heart"></i>
            </span>
            <span>3</span>
          </a>
        </div>
      </div>
    </div>
  </article>
</template>

<style lang="scss" scoped>
.time::before {
  content: "\00b7 ";
}

.button {
  border: 0;
}

.name::after, .username::after {
  content: " ";
}
</style>

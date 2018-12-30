<template>
  <div class="background">
    <div class="media">
      <div class="media-left">
        <figure class="image is-64x64">
          <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image">
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-6">John Smith</p>
        <p class="subtitle is-6">@johnsmith</p>
        <div class="level is-mobile">
          <div class="level-left">
            <div class="level-item">
              <div class="wrapper">
                <span class="counter-label is-size-7">Thoughts</span>
                <span class="counter-value">2</span>
              </div>
            </div>
            <div class="level-item">
              <div class="wrapper">
                <span class="counter-label is-size-7">Following</span>
                <span class="counter-value">70</span>
              </div>
            </div>
            <div class="level-item">
              <div class="wrapper">
                <span class="counter-label is-size-7">Followers</span>
                <span class="counter-value is-size-6">160</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  display: grid;
  grid-template-columns: 1fr;
  text-align: center;
}

.counter-value {
  font-weight: bold;
}
</style>


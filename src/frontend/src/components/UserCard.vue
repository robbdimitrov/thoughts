<template>
  <div class="container">
    <div class="cover"></div>
    <div class="content">
      <img class="avatar" src="https://bulma.io/images/placeholders/96x96.png"
        alt="Placeholder image" />
      <div class="labels">
        <p class="title">John Smith</p>
        <p class="subtitle">@johnsmith</p>
      </div>
    </div>
    <div class="counters">
      <div class="counter">
        <span class="counter-label">Thoughts</span>
        <span class="counter-value">2</span>
      </div>
      <div class="counter">
        <span class="counter-label">Following</span>
        <span class="counter-value">70</span>
      </div>
      <div class="counter">
        <span class="counter-label">Followers</span>
        <span class="counter-value">160</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
$padding: 10px;

$text-weight-light: 300;
$text-weight-regular: 400;
$text-weight-semibold: 500;
$text-weight-bold: 700;

.cover {
  height: 100px;
  background: lightblue;
}

.container {
  background: white;
  overflow: auto;
}

.content {
  display: flex;
}

.avatar {
  width: 64px;
  height: 64px;
  margin: $padding;
  border-radius: 50%;
  margin-top: -20px;
  border: 2px solid white;
}

.labels {
  margin: $padding;
  margin-left: 0;
}

.title {
  font-weight: $text-weight-semibold;
}

.subtitle {
  font-weight: $text-weight-light;
  margin-top: 0.1em;
}

p {
  margin: 0;
}

.counters {
  display: flex;
  justify-content: space-evenly;
  margin: $padding 0 $padding;
}

.counter {
  display: flex;
  flex-direction: column;
  text-align: center;
}

.counter-label {
  font-size: 0.875em;
}

.counter-label {
  font-weight: $text-weight-light;
}

.counter-value {
  font-weight: $text-weight-semibold;
}
</style>

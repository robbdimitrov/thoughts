<template>
  <div class="container flex vertical">
    <div class="cover"></div>

    <div class="content flex horizontal">
      <img class="avatar"
        src="https://bulma.io/images/placeholders/96x96.png" />
      <div class="labels">
        <p class="title semibold">John Smith</p>
        <p class="subtitle light">@johnsmith</p>
      </div>
    </div>

    <div class="counters flex horizontal">
      <div class="counter flex vertical">
        <span class="counter-label light">Thoughts</span>
        <span class="counter-value">2</span>
      </div>

      <div class="counter flex vertical">
        <span class="counter-label light">Following</span>
        <span class="counter-value">70</span>
      </div>

      <div class="counter flex vertical">
        <span class="counter-label light">Followers</span>
        <span class="counter-value">160</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
$padding: 10px;
$avatar-width: 64px;
$cover-height: 80px;

$text-weight-light: 300;
$text-weight-regular: 400;
$text-weight-semibold: 500;
$text-weight-bold: 700;

.cover {
  height: $cover-height;
  background: lightblue;
}

.container {
  background: white;
}

.flex {
  display: flex;
}

.flex.horizontal {
  flex-direction: row;
}

.flex.vertical {
  flex-direction: column;
}

strong, .semibold {
  font-weight: $text-weight-semibold;
}

small, .light {
  font-weight: $text-weight-light;
}

.avatar {
  width: $avatar-width;
  height: $avatar-width;
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
  margin: 0;
}

.subtitle {
  margin-top: 0.1em;
}

.counters {
  justify-content: space-evenly;
  margin: 0 0 $padding;
}

.counter {
  text-align: center;
}

.counter-label, .subtitle {
  font-size: 0.875em;
}
</style>

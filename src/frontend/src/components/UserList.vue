<template>
  <div class="container">
    <user-item class="item"></user-item>
    <user-item class="item"></user-item>
    <user-item class="item"></user-item>
    <user-item class="item"></user-item>
    <user-item class="item"></user-item>
  </div>
</template>

<script>
import UserItem from './UserItem.vue';

export default {
  name: 'user-list',
  components: {
    UserItem
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";

$margin: $padding / 2;
$item-width: 0.5 * $content-main-width - $padding;

.item {
  background: white;
  display: inline-block;
  width: $item-width;
  border-radius: 5px;
  box-sizing: border-box;
  height: 280px;
  margin: $margin;
}

@media screen and (max-width: $content-main-width) {
  .item {
    margin-left: auto;
    margin-right: auto;
    display: block;
    max-width: $item-width;
    width: 100%;
  }
}

@media screen and (max-width: $break-sm) {
  .item {
    width: 100%;
    margin: 0;
    border-radius: 0;
  }
}
</style>

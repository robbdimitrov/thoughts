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
  display: inline-block;
  width: $item-width;
  height: 280px;
  margin: $margin;
}

@media screen and (max-width: $content-main-width) {
  .item {
    margin-left: auto;
    margin-right: auto;
    display: block;
    margin-bottom: $padding;
  }
}

@media screen and (max-width: $break-sm) {
  .item {
    display: inline-block;
    width: 100%;
    height: auto;
    margin: 0;
  }

  .item {
    border-bottom: 1px solid #e6ecf0;
  }

  .item:last-child {
    border-bottom: none;
  }
}
</style>

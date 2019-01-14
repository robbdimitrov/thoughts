<template>
  <div class="container">
    <user-item v-for="item in items" :key="item"
      class="list-item" />
  </div>
</template>

<script>
import UserItem from './UserItem.vue';

export default {
  name: 'user-list',
  components: {
    UserItem
  },
  props: {
    items: Number
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";

$margin: $padding / 2;
$item-width: 0.5 * $content-main-width - $padding;

.list-item {
  display: inline-block;
  width: $item-width;
  height: 280px;
  margin: $margin;
}

@media screen and (max-width: $content-main-width) {
  .list-item {
    margin-left: auto;
    margin-right: auto;
    display: block;
    margin-bottom: $padding;
  }
}

@media screen and (max-width: $break-sm) {
  .list-item {
    display: inline-block;
    width: 100%;
    height: auto;
    margin: 0;
    border-bottom: 1px solid #e6ecf0;
  }

  .list-item:last-child {
    border-bottom: none;
  }
}
</style>

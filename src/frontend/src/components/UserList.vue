<template>
  <div class="container">
    <user-item
      v-for="item in items"
      :key="item"
      class="list-item"
    />
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
@import "../styles/colors";
@import "../styles/helpers";

.container {
  display: grid;
  grid-gap: $padding;
  grid-template-columns: 1fr 1fr;
}

.list-item {
  display: block;
  height: 280px;
}

@media screen and (max-width: $break-sm) {
  .container {
    display: block;
  }

  .list-item {
    height: auto;
    width: 100%;
    @include separator;

    &:last-child {
      border-bottom: none;
    }
  }
}
</style>

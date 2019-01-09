<template>
  <div class="container main">
    <user-card class="user-card"></user-card>
    <div class="content">
      <thought-box class="content-input"></thought-box>
      <thought-list class="content-list"></thought-list>
    </div>
  </div>
</template>

<script>
import ThoughtList from '../components/ThoughtList.vue';
import UserCard from '../components/UserCard.vue';
import ThoughtBox from '../components/ThoughtBox.vue';

export default {
  name: 'feed-view',
  components: {
    ThoughtBox,
    ThoughtList,
    UserCard
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";

.container.main {
  margin: $padding * 2 0;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.user-card {
  width: $content-secondary-width;
  margin-right: 2 * $padding;
  display: block;
}

.content {
  width: $content-primary-width;
}

@media screen and (max-width: $break-lg) {
  .user-card {
    display: none;
  }
}

@media screen and (max-width: $break-sm) {
  .content {
    width: 100%;
  }
}
</style>


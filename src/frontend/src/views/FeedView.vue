<template>
  <div class="container">
    <div>
      <user-card class="user-info"></user-card>
      <thought-list class="list-view"></thought-list>
    </div>
  </div>
</template>

<script>
import ThoughtList from '../components/ThoughtList.vue';
import UserCard from '../components/UserCard.vue';

export default {
  name: 'feed-view',
  components: {
    ThoughtList,
    UserCard
  }
};
</script>

<style lang="scss" scoped>
$list-width: 512px;

.user-info {
  width: 280px;
}

.list-view {
  width: 100%;
}

@media screen and (min-width: $list-width) {
  .list-view {
    widows: $list-width;
  }
}
</style>


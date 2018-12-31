<template>
  <div class="container">
    <user-card class="user-info"></user-card>
    <thought-list class="list-view"></thought-list>
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
$card-width: 280px;

.container {
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.user-info {
  width: $card-width;
  margin-right: 10px;
  display: none;
}

.list-view {
  width: 100%;
  display: block;
}

@media screen and (min-width: $list-width + $card-width + 20px) {
  .user-info {
    display: block;
  }
}

@media screen and (min-width: $list-width + 20px) {
  .list-view {
    width: $list-width;
  }
}
</style>


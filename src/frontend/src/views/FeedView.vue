<template>
  <div class="container">
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
$list-width: 512px;
$card-width: 280px;

.container {
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.user-card {
  width: $card-width;
  margin-right: 10px;
  display: none;
}

.content {
  width: 100%;
}

.content-list {
  display: block;
}

@media screen and (min-width: $list-width + $card-width + 20px) {
  .user-card {
    display: block;
  }
}

@media screen and (min-width: $list-width + 20px) {
  .content {
    width: $list-width;
  }
}
</style>


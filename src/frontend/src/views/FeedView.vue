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
@import "../styles/variables";

$list-width: 512px;
$card-width: 280px;

.container {
  margin-top: $padding;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.user-card {
  width: $card-width;
  margin-right: 2 * $padding;
  display: none;
}

.content {
  width: 100%;
}

@media screen and (min-width: $break-lg) {
  .user-card {
    display: block;
  }
}

@media screen and (min-width: $break-sm) {
  .content {
    width: $list-width;
  }
}
</style>


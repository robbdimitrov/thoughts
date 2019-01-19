<template>
  <div class="container main">
    <user-card class="user-card" />
    <div class="content">
      <thought-box />
      <thought-list :items="3" />
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
  margin: $spacing-md 0;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.user-card {
  width: $content-secondary-width;
  margin-right: $spacing-md;
  display: block;
}

.content {
  width: $content-primary-width;
}

@media screen and (max-width: 820px) {
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


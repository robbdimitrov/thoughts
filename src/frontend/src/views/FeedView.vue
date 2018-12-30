<template>
  <div class="container">
    <div class="columns is-2">
      <div class="column is-4">
        <user-card class="column"></user-card>
      </div>
      <div class="column is-7">
        <thought-list class="column"></thought-list>
      </div>
    </div>
  </div>
</template>

<script>
import ThoughtList from '../components/ThoughtList.vue';
import UserCard from '../components/UserCard.vue';

export default {
  components: {
    ThoughtList,
    UserCard
  }
};
</script>

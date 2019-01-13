<template>
  <div class="container">
    <div class="search-term-bar">
      <span class="search-term">Search term</span>
    </div>

    <div class="scope-nav-bar">
      <div class="scope-nav-item">
        <span class="scope-nav-item-title">
          All
        </span>

        <span class="scope-nav-item-title">
          People
        </span>

        <span class="scope-nav-item-title">
          Tweets
        </span>
      </div>
    </div>

    <div class="content">
      <div class="user-container">
        <div class="user-header">
          <span>People</span>
          <span>View all</span>
        </div>

        <user-list class="user-container" />
      </div>

      <thought-list class="thought-container" />
    </div>
  </div>
</template>

<script>
import ThoughtList from '../components/ThoughtList.vue';
import UserList from '../components/UserList.vue';

export default {
  name: 'search-view',
  components: {
    ThoughtList,
    UserList
  }
};
</script>

<style lang="scss" scoped>

</style>

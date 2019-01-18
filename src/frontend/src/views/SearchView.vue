<template>
  <div class="container">
    <search-term-bar class="search-term-bar" />

    <search-scope-bar class="scope-nav-bar" />

    <div class="content main-content">
      <div class="user-container">
        <div class="user-header">
          <span>People</span>
          <span>View all</span>
        </div>

        <user-list :items="2" />
      </div>

      <thought-list class="thought-container" :items="3" />
    </div>
  </div>
</template>

<script>
import SearchTermBar from '../components/SearchTermBar.vue';
import SearchScopeBar from '../components/SearchScopeBar.vue';
import ThoughtList from '../components/ThoughtList.vue';
import UserList from '../components/UserList.vue';

export default {
  name: 'search-view',
  components: {
    SearchTermBar,
    SearchScopeBar,
    ThoughtList,
    UserList
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";

.content {
  margin-bottom: $spacing-md;
}

.user-header {
  margin-top: $spacing-md;
}

.user-container {
  margin-bottom: $padding;
}
</style>

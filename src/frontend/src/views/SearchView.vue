<template>
  <div class="container">
    <search-bar class="search-bar" />

    <search-scope-bar class="scope-nav-bar" />

    <div class="content main-content">
      <div class="user-container">
        <div class="user-header">
          <span class="user-header-title">People</span>
          <span class="user-header-button">View all</span>
        </div>

        <user-list :items="2" />
      </div>

      <thought-list class="thought-container" :items="3" />
    </div>
  </div>
</template>

<script>
import SearchBar from '../components/SearchBar.vue';
import SearchScopeBar from '../components/SearchScopeBar.vue';
import ThoughtList from '../components/ThoughtList.vue';
import UserList from '../components/UserList.vue';

export default {
  name: 'search-view',
  components: {
    SearchBar,
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
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: $spacing-md;
  margin-bottom: $padding;
}

.user-container {
  margin-bottom: $padding;
}

.search-bar {
  margin-top: -$border-width-sm;
}

.user-header-title {
  font-size: rem(17);
  font-weight: $font-weight-semibold;
}

.user-header-button {
  font-size: rem(14);

  &:hover {
    text-decoration: underline;
  }
}

@media screen and (max-width: $break-md) {
  .user-header {
    margin-left: $padding;
    margin-right: $padding;
  }
}
</style>

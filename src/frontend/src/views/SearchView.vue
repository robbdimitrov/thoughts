<template>
  <div class="container">
    <div class="search-term-bar">
      <div class="search-term-container">
        <span class="search-term">Search term</span>
      </div>
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
@import "../styles/variables";
@import "../styles/fonts";

$search-term-background: #35393C;

.content {
  margin-bottom: $spacing-md;
}

.search-term-bar {
  background: $search-term-background;
  height: 32px;
  padding: 16px 0;
}

.search-term-container {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
  max-width: $max-component-width;
}

.search-term {
  padding-left: 12px;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-size: 27px;
  line-height: 32px;
  color: white;
  font-weight: $font-weight-semibold;
}

.user-container {
  margin-bottom: $padding;
}
</style>

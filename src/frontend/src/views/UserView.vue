<template>
  <div class="container">
    <user-header />
    <control-bar />

    <div class="content main-content">
      <thought-list v-if="isThoughtsShown" :items="3" />
      <user-list v-if="isUsersShown" :items="5" />
    </div>
  </div>
</template>

<script>
import ControlBar from '../components/ControlBar.vue';
import ThoughtList from '../components/ThoughtList.vue';
import UserHeader from '../components/UserHeader.vue';
import UserList from '../components/UserList.vue';

export default {
  name: 'user-view',
  components: {
    ControlBar,
    ThoughtList,
    UserHeader,
    UserList
  },
  computed: {
    isThoughtsShown: function () {
      let location = this.$route.params.location;
      return location === undefined || location === 'likes';
    },
    isUsersShown: function () {
      let location = this.$route.params.location;
      return location === 'following' || location === 'followers';
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";

.content {
  margin-top: $spacing-md;
  margin-bottom: $spacing-md;
}
</style>

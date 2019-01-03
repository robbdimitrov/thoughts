<template>
  <div class="container">
    <div>Home</div>

    <i class="fas fa-brain"></i>

    <div class="right-items">
      <div>Search bar</div>
      <div>Profile</div>
      <div>Create</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'navigation-bar'
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: row;
  background: white;
  height: 46px;
  justify-content: space-between;
  border-bottom: 1px solid rgba(0, 0, 0, 0.25);
}

.right-items {
  display: flex;
  flex-direction: row;
}
</style>

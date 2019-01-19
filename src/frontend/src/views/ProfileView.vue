<template>
  <div class="container">
    <div class="form-content main-content">
      <h1 class="form-title">Edit profile</h1>

      <form>
        <div class="fieldset">
          <i class="fas fa-passport input-icon"></i>

          <input
            type="text" class="form-input"
            id="name" placeholder="Name"
            required
          >
        </div>

        <div class="fieldset">
          <i class="fas fa-user input-icon"></i>

          <input
            type="text" class="form-input"
            id="username" placeholder="Username"
            required
          >
        </div>

        <div class="fieldset">
          <i class="fas fa-envelope input-icon"></i>

          <input
            type="email" class="form-input"
            id="email" placeholder="Email"
            pattern="[^@]+@[^@]+\.[^@]+"
            required
          >
        </div>

        <button type="submit"
          class="button form-button">
          Save changes
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'edit-profile-view'
};
</script>

<style lang="scss" scoped>
form {
  margin-bottom: 0;
}
</style>

<template>
  <div class="container">
    <div class="form-content main-content">
      <h1 class="form-title">Change password</h1>

      <form>
        <div class="fieldset">
          <i class="fas fa-lock input-icon"></i>

          <input type="password" class="form-input"
            id="password" placeholder="New Password"
            minlength="4" maxlength="30" required>

          <button type="button" class="outline-button">
            SHOW
          </button>
        </div>

        <div class="fieldset">
          <i class="fas fa-lock input-icon"></i>

          <input type="password" class="form-input"
            id="password" placeholder="Current Password"
            minlength="4" maxlength="30" required>

          <button type="button" class="outline-button">
            SHOW
          </button>
        </div>

        <button type="submit"
          class="button form-button">
          Save
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'password-view'
}
</script>

<style lang="scss" scoped>
form {
  margin-bottom: 0;
}
</style>

<template>
  <div class="container">
    <div class="content main-content">
      <h1 class="form-title">Login</h1>
      <p class="form-message">Welcome back! Login to access your account.</p>

      <form>
        <div class="fieldset">
          <i class="fas input-icon fa-user"></i>

          <input type="email" class="form-input"
            id="email" placeholder="Email"
            pattern="[^@]+@[^@]+\.[^@]+" required>
        </div>

        <div class="fieldset">
          <i class="fas input-icon fa-lock"></i>

          <input type="password" class="form-input"
            id="password" placeholder="Password"
            minlength="4" maxlength="30" required>

          <button type="button" class="outline-button">
            SHOW
          </button>
        </div>

        <button type="submit"
          class="button form-button">
          Log In
        </button>
      </form>

      <div class="reference">
        <span class="reference-label">Don't have an accout?</span>
        <router-link to="/signup" class="reference-button">
          <span>Register</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login-view'
}
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/fonts";
@import "../styles/helpers";
@import "../styles/colors";

.content {
  background: white;
  margin-top: $spacing-md;
  margin-bottom: $spacing-md;
  padding: $spacing-lg;
  box-sizing: border-box;
}
</style>

<template>
  <div class="container">
    <div class="form-content main-content">
      <h1 class="form-title">Login</h1>
      <p class="form-message">Welcome back! Login to access your account.</p>

      <form>
        <div class="fieldset">
          <i class="fas fa-envelope input-icon"></i>

          <input
            type="email" class="form-input"
            id="email" placeholder="Email"
            pattern="[^@]+@[^@]+\.[^@]+" required
          >
        </div>

        <div class="fieldset">
          <i class="fas fa-lock input-icon"></i>

          <input
            type="password" class="form-input"
            id="password" placeholder="Password"
            minlength="4" maxlength="30" required
          >

          <button type="button" class="visibility-button">
            <i class="fas fa-eye"></i>
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
};
</script>

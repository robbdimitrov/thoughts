<template>
  <div class="container">
    <div class="form-content main-content">
      <h1 class="form-title">Register</h1>
      <p class="form-message">Create an account and join in!</p>

      <form>
        <div class="fieldset">
          <i class="fas fa-passport input-icon"></i>

          <input type="text" class="form-input"
            id="name" placeholder="Name"
            required>
        </div>

        <div class="fieldset">
          <i class="fas fa-user input-icon"></i>

          <input type="text" class="form-input"
            id="username" placeholder="Username"
            required>
        </div>

        <div class="fieldset">
          <i class="fas fa-envelope input-icon"></i>

          <input type="email" class="form-input"
            id="email" placeholder="Email"
            pattern="[^@]+@[^@]+\.[^@]+" required>
        </div>

        <div class="fieldset">
          <i class="fas fa-lock input-icon"></i>

          <input type="password" class="form-input"
            id="password" placeholder="Password"
            minlength="4" maxlength="30" required>

          <button type="button" class="outline-button">
            SHOW
          </button>
        </div>

        <button type="submit"
          class="button form-button">
          Register
        </button>
      </form>

      <div class="reference">
        <span class="reference-label">Already have an accout?</span>
        <router-link to="/login" class="reference-button">
          <span>Login</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'signup-view'
}
</script>

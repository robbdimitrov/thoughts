<template>
  <div class="container">
    <div class="header">
      <!-- TODO: Add close button -->
    </div>

    <div class="content">
      <img
        class="avatar"
        src="https://via.placeholder.com/300.png"
      />

      <form class="input">
        <textarea
          type="text"
          placeholder="What are you thinking?"
          id="thought"
          name="thought"
          class="form-input"
          required
        />

        <button class="button submit-button">
          Create
        </button>
      </form>
    </div>
  </div>
</template>

<script scoped>
export default {
  name: 'thought-box'
};
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/colors";
@import "../styles/helpers";

$avatar-padding: $avatar-width-sm - $avatar-width-xs + $padding;

.container {
  background: $primary-color;
}

form {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin: $padding;
  margin-left: 0;
}

.form-input {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  padding: 6px;
  border-radius: $border-radius-sm;
  @include border-dark;
  resize: none;
  height: 80px;
}

.submit-button {
  margin-top: $padding;
}

.avatar {
  flex-shrink: 0;
  width: $avatar-width-xs;
  height: $avatar-width-xs;
  margin: $padding;
  margin-left: $avatar-padding;
}
</style>

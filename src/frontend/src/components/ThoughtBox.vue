<template>
  <div class="thought-box">
    <div class="header">
      <button class="close-button">
        <i class="fas fa-times"></i>
      </button>

      <button class="button submit-button">
        Create
      </button>
    </div>

    <div class="content">
      <img
        class="avatar"
        src="https://via.placeholder.com/300.png"
      />

      <textarea
        type="text"
        placeholder="What are you thinking?"
        id="thought"
        name="thought"
        class="form-input"
        required
      />

      <span class="counter">10/140</span>
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

.thought-box {
  background: $primary-color;
  border-radius: $border-radius-sm;
  width: 100%;
  max-width: $content-primary-width;
}

.header {
  border-bottom: 1px solid black;
  height: $bar-height;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.content {
  display: flex;
  margin-top: $padding;
}

.close-button {
  margin-left: $padding;
  width: $button-height;
  height: $button-height;
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
  margin: $padding;
  margin-left: 0;
}

.submit-button {
  margin-right: $padding;
}

.avatar {
  flex-shrink: 0;
  width: $avatar-width-xs;
  height: $avatar-width-xs;
  margin: $padding;
}
</style>

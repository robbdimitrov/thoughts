<template>
  <div class="container">
    <img class="avatar"
      src="https://via.placeholder.com/300.png" />
    <form class="input">
      <input type="text"
        placeholder="What are you thinking?"
        id="thought"
        name="thought"
        class="form-input"
        required>
      <button class="form-button">Submit</button>
    </form>
  </div>
</template>

<script scoped>
export default {
  name: 'thought-box'
}
</script>

<style lang="scss" scoped>
@import "../styles/variables";
@import "../styles/colors";

.container {
  display: flex;
  background: #EAEBEB;
  padding: $padding;
}

form {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.form-button {
  display: none;
}

.form-input {
  padding: 8px;
  border-radius: 8px;
  border: 1px solid black;
}

.avatar {
  width: $avatar-width-xs;
  height: $avatar-width-xs;
  border-radius: 50%;
  margin-left: $avatar-width-sm - $avatar-width-xs;
  margin-right: $padding;
}
</style>

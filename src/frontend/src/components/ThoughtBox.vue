<template>
  <div class="container">
    <img class="avatar"
      src="https://bulma.io/images/placeholders/96x96.png" />
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
$avatar-width: 32px;

.container {
  // display: flex;
  background: #EAEBEB;
  padding: 12px;
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
  width: $avatar-width;
  height: $avatar-width;
  border-radius: 50%;
  margin-left: 48px - $avatar-width;
  margin-right: 10px;
}
</style>

<template>
  <div class="thought-box">
    <div class="header">
      <button class="close-button" v-on:click="$emit('close-popup')">
        <i class="fas fa-times"></i>
      </button>

      <button
        class="button submit-button"
        v-bind:disabled="!isMessageValid"
        @click="$emit('create-post', message)"
      >
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
        v-model="message"
        required
      />
    </div>

    <span  class="counter" v-bind:class='{ invalid: message.length > maxLength }'>
      {{message.length}}/{{maxLength}}
    </span>
  </div>
</template>

<script scoped>
export default {
  name: 'thought-box',
  data: function () {
    return {
      message: '',
      maxLength: 140
    };
  },
  computed: {
    isMessageValid: function () {
      return this.message.length > 0 && this.message.length <= this.maxLength;
    }
  }
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
  border-bottom: 1px solid $shadow-color;
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
  width: 100%;
  padding: 6px;
  resize: none;
  height: 90px;
  margin: $padding;
  margin-left: 0;
  background: $selected-color;
  border: 0;
  border-bottom: 2px solid $active-color;
  border-radius:
    $border-radius-sm
    $border-radius-sm
    0 0;

  &::placeholder {
    color: gray;
  }

  &:focus {
    outline-width: 0;

    &::placeholder {
      color: lighten($text-placeholder-color, 20%);
    }
  }
}

.submit-button {
  margin-right: $padding;
}

.counter {
  margin: 0 10px 10px;
  text-align: right;
  display: block;
  color: $detail-text-color;

  &.invalid {
    color: $error-color;
  }
}

.avatar {
  flex-shrink: 0;
  width: $avatar-width-xs;
  height: $avatar-width-xs;
  margin: $padding;
}
</style>

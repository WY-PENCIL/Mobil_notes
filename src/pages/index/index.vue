<template>
  <view class="content">
    <view class="text-area">
      <text class="title">{{ $t("hello") }}</text>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref } from "vue";
const title = ref("Hello");
</script>

<style>
.content {
  /* display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; */
  width: 100vw;
  height: 100vh;
  color: #fff;
  /* background-image: url(https://bing.img.run/m.php) !important;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover; */
}

.logo {
  width: 200rpx;
  height: 200rpx;
  margin-top: 200rpx;
  margin-right: auto;
  margin-bottom: 50rpx;
  margin-left: auto;
}

.text-area {
  display: flex;
  justify-content: center;
}

.title {
  font-size: 36rpx;
  color: #8f8f94;
}
</style>

import { createSSRApp } from "vue";
import App from "./App.vue";
import i18n from "./language";
import { setupStore } from "@/store";
export function createApp() {
  const app = createSSRApp(App);
  app.use(i18n);
  setupStore(app); //全局注册store
  return {
    app,
  };
}

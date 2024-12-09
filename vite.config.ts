import { defineConfig, type UserConfig, type ConfigEnv, loadEnv } from "vite";
import uni from "@dcloudio/vite-plugin-uni";

// https://vitejs.dev/config/
export default defineConfig(
  async ({ mode }: ConfigEnv): Promise<UserConfig> => {
    const env = loadEnv(mode, process.cwd());
    return {
      plugins: [uni()],
      resolve: {
        alias: {
          "@": "/src", // 配置路径别名，方便导入
        },
      },
      css: {
        preprocessorOptions: {
          scss: {},
        },
      },
      //配置反向代理
      server: {
        host: "0.0.0.0", //
        port: +env.VITE_PORT,
        // open: true, // 自动打开浏览器
        proxy: {
          [env.VITE_APP_BASE_API]: {
            target: env.VITE_APP_API_URL, //目标服务器
            changeOrigin: true, // 是否更改源，即是否支持跨域
            rewrite: (path) =>
              path.replace(new RegExp("^" + env.VITE_APP_BASE_API), ""), // 去掉前缀
          },
        },
      },
    };
  },
);

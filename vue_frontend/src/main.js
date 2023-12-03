import { createApp } from "vue";
import { createPinia } from "pinia";
import { autoAnimatePlugin } from "@formkit/auto-animate/vue";
import App from "./App.vue";
import router from "./router";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  components,
  directives,
});

const app = createApp(App);
const pinia = createPinia();

pinia.use(piniaPluginPersistedstate);

app.use(pinia);
app.use(router);

app.use(vuetify).use(autoAnimatePlugin).mount("#app");

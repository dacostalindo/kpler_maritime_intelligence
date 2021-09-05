<template>
  <v-app>
    <kpler-navbar/>
    <v-main>
      <kpler-map/>
      <!-- <router-view /> -->
    </v-main>
  </v-app>
</template>

<script>

import KplerMap from "./components/KplerMap.vue"
import KplerNavbar from "./components/KplerNavbar.vue"
// import KplerDrawer from "./components/KplerDrawer.vue"

export default {
  name: "App",
  components: {
    KplerMap,
    KplerNavbar,
    // KplerDrawer
  },
  data: () => ({
    // drawer: true,
  }),
};
</script>

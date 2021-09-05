<template>
  <v-app>
    <kpler-navbar/>
    <v-main>
      <kpler-map/>
    </v-main>
  </v-app>
</template>

<script>
/* eslint-disable */
import KplerMap from "./components/KplerMap.vue"
import KplerNavbar from "./components/KplerNavbar.vue"

export default {
  name: "App",
  components: {
    KplerMap,
    KplerNavbar,
  },
  data: () => ({
  }),
};
</script>

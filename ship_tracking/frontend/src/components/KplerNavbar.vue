<template>
  <div>
        <v-navigation-drawer
            absolute
            permanent
            right
            class="primary"
            app light
        >
            <template v-slot:prepend>
            <v-list-item two-line>
                <v-list-item-avatar>
                <img src="@/assets/kpler_icon.png">
                </v-list-item-avatar>

                <v-list-item-content>
                <v-list-item-title>Marc Beuret</v-list-item-title>
                <v-list-item-subtitle>Logged In</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
            </template>

            <v-divider></v-divider>

            <v-list dense>
            <v-list-item
                v-for="item in items"
                :key="item.vessel_id"
                @click="addVesselId(item.vessel_id)"
            >
                <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                <v-list-item-title>{{ item.vessel_id }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            </v-list>
        </v-navigation-drawer>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "GMVNavbar",
  data: () => ({
    items: [],
  }),
  created() {
    const path = "http://localhost:5000/vessels";
    axios.get(path, { crossDomain: true }).then((res) => {
        let vessels_ids = res.data;
        vessels_ids.map(v => Object.assign(v, {icon: "mdi-ship-wheel"}))
        this.items = vessels_ids
    });
  },
  methods: {
      addVesselId(vessel_id) {
        this.$store.commit("addVessel", vessel_id)
        console.log(this.$store.getters.vesselToShow)
      }
  }

};
</script>

<style></style>
